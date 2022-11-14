# Movie 데이터 저장
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owaste.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from zerowaste.models import Campaign


campaign = Campaign()
campaign_list = []

with open('캠페인정보.csv', encoding='utf8') as csv_file_sub_categories:
    rows = csv.reader(csv_file_sub_categories)
    next(rows, None)
    for row in rows:
        campaign_name = row[0]
        campaign_start = row[1]
        campaign_finish = row[2]
        campaign_img = row[3]
        campaign_link = row[4]

        campaign = Campaign(campaign_name=campaign_name, campaign_start=campaign_start, campaign_finish=campaign_finish, campaign_img=campaign_img, campaign_link=campaign_link)
        campaign_list.append(campaign)
# print(campaign_list)
# print(len(campaign_list))
Campaign.objects.bulk_create(campaign_list)
Campaign.objects.all().count()