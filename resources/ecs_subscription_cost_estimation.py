#Written by Guda Pradeep on 4/12/2018
#python -m pip install aliyun-python-sdk-bssopenapi

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkcore.request import CommonRequest
from bs4 import BeautifulSoup as bs

import csv
import datetime


count = 0

# Construct an Aliyun Client for initiating a request
# Set AccessKeyID and AccessKeySevcret when constructing the Aliyun Client
# RAM is a Global Service, and its API ingress is located in the East China 1 (Hangzhou) region. Enter "cn-hangzhou" in "Region"

clt = client.AcsClient('<AccessKey ID>','<Access Key Secret>')

writer = csv.writer(open('ecs_subscription_cost_estimation_output_'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 +'.csv', 'w'))

for row in csv.reader(open('ecs_subscription_cost_estimation_template.csv', 'r')):
    if count == 0:
        writer.writerow(row)
        count += 1

    else:
        request0 = CommonRequest()
        request0.set_accept_format('xml')
        request0.set_domain('business.ap-southeast-1.aliyuncs.com')
        request0.set_method('POST')
        request0.set_version('2017-12-14')
        request0.set_action_name('GetSubscriptionPrice')

        request0.add_query_param('ModuleList.1.ModuleCode', 'InstanceType')
        request0.add_query_param('ModuleList.1.Config', "InstanceType:"+row[1]+",ImageOs:"+row[9])
        request0.add_query_param('ModuleList.2.ModuleCode', 'SystemDisk')
        request0.add_query_param('ModuleList.2.Config', "SystemDisk.Category:"+row[10]+",SystemDisk.Size:"+row[2])
        request0.add_query_param('ModuleList.3.ModuleCode', 'DataDisk')
        request0.add_query_param('ModuleList.3.Config', "DataDisk.Category:"+row[11]+",DataDisk.Size:"+row[3])
        request0.add_query_param('RegionId', 'ap-southeast-1')
        request0.add_query_param('Region', row[8])
        request0.add_query_param('ServicePeriodQuantity', row[6])
        request0.add_query_param('ServicePeriodUnit', row[7])
        request0.add_query_param('SubscriptionType', row[4])
        request0.add_query_param('ProductCode', 'ecs')
        request0.add_query_param('OrderType', row[5])

        response0 = clt.do_action(request0)

        root = bs(response0, features="html.parser")
        pricing = root.find('data')
        tradeprice = pricing.tradeprice
        currency = pricing.currency
        row[12] = float(tradeprice.get_text())
        row[13] = currency.get_text()
        writer.writerow(row)
        print (response0)
        count += 1



