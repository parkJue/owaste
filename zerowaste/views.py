from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Shop
from .models import Nkreview
from django.db.models import Q


info_list = Shop.objects.all().order_by('id')
search_list = Shop.objects.all().order_by('id')
Nkreview_list = Nkreview.objects.all().order_by('id')


def base(request):
    return render(
        request,
        'zerowaste/base.html'
    )

# --------------- 검색 --------------------


def search(request):
    global info_list
    global search_list
    search_key = request.GET.get('search_key')
    print(search_key)
    if search_key:
        search_list = info_list.filter(
            Q(name__icontains=search_key))  # 이름으로 찾기
        print('search_list', search_list)
    # search_list들을 info_list라는 이름으로 shop_search에 넘김
    return render(request, "zerowaste/shop_search.html", {'info_list': search_list})


def info(request):
    all = []
    category_one = request.GET.get('category', None)
    subject_list = request.GET.getlist('subject', None)
    facility_list = request.GET.getlist('facility', None)

    q = Q()
    if category_one:
        # q &= Q(category__in=category_one)
        q.add(Q(category=category_one), q.AND)
    # if subject_list:
    #     q.add(Q(subject__in=subject_list), q.AND)
    if subject_list:
        for i in range(0, len(subject_list)):
            q.add(Q(subject__icontains=subject_list[i]), q.AND)
    if facility_list:
        for i in range(0, len(facility_list)):
            q.add(Q(facility__icontains=facility_list[i]), q.AND)

    print(q)
    products = Shop.objects.filter(q)
    for product in products:
        all.append(product)
    print('all : ', all)
    return render(request, 'zerowaste/shop_search.html', {'all': all})


def shop_detail(request, id):
    shop_detail = get_object_or_404(Shop, pk=id)
    # id와 똑같은 Nkreview 불러오기
    review_detail = Nkreview.objects.filter(shop=id)
    return render(request, 'zerowaste/shop_detail.html', {'shop_detail': shop_detail, 'review_detail':review_detail})
