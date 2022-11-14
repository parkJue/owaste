from django.db import models

# FK XXX


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    start = models.DateField(blank=True, null=True)
    finish = models.DateField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    subject = models.CharField(max_length=200, blank=True, null=True)
    facility = models.CharField(max_length=300, blank=True, null=True)
    mon = models.CharField(max_length=20, blank=True, null=True)
    tue = models.CharField(max_length=20, blank=True, null=True)
    wed = models.CharField(max_length=20, blank=True, null=True)
    thu = models.CharField(max_length=20, blank=True, null=True)
    fri = models.CharField(max_length=20, blank=True, null=True)
    sat = models.CharField(max_length=20, blank=True, null=True)
    sun = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    page1 = models.CharField(max_length=200, blank=True, null=True)
    page2 = models.CharField(max_length=200, blank=True, null=True)
    page3 = models.CharField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    tag = models.CharField(max_length=400, blank=True, null=True)
    region = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    lat = models.CharField(max_length=20, blank=True, null=True)
    lon = models.CharField(max_length=20, blank=True, null=True)
    img = models.TextField(blank=True, null=True)


class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=255)
    nick = models.CharField(max_length=200)
    img = models.CharField(max_length=255, blank=True, null=True)

# FK OOO


class Nkreview(models.Model):

    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    source = models.CharField(max_length=10)
    content = models.TextField()
    reg_date = models.DateField()
    nick = models.CharField(max_length=200)


class Oreview(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    source = models.CharField(max_length=10)
    content = models.TextField()
    register_date = models.DateField()
    update_date = models.DateField(blank=True, null=True)