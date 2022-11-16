from collections import defaultdict
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from zerowaste.models import Oreview, Shop
from common.models import Profile
from zerowaste.forms import OreviewForm
from django.db.models import Q
from django.contrib.auth import get_user_model


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            Profile.objects.create(user=signed_user)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/owaste/index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# 프로필


@login_required
def profile(request):
    myreview_dict = defaultdict(list)

    myreview_qs = Oreview.objects.filter(
        user_id=request.user.id).select_related("shop")
    for myreview in myreview_qs:
        myreview_dict[myreview.shop].append(myreview)

    # User = get_user_model()
    # login_user = request.user  # User.objects.get(id=request.user.id)
    # shop_qs = Shop.objects.filter(oreview__user=login_user)

    context = {
        'myreview_dict': dict(myreview_dict),
        # 'shop_qs': shop_qs
    }
    return render(request, "common/profile.html", context)

# 비밀번호 변경


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/owaste/index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/change_password.html', {
        'form': form
    })
