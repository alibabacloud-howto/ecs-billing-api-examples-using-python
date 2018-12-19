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

writer = csv.writer(open('ecs_payasyougo_cost_estimation_output_'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 +'.csv', 'w'))

for row in csv.reader(open('ecs_payasyougo_cost_estimation_template.csv', 'r')):
    if count == 0:
        writer.writerow(row)
        count += 1

    else:
        request0 = CommonRequest()
        request0.set_accept_format('xml')
        request0.set_domain('business.ap-southeast-1.aliyuncs.com')
        request0.set_method('POST')
        request0.set_version('2017-12-14')
        request0.set_action_name('GetPayAsYouGoPrice')

        request0.add_query_param('ModuleList.1.ModuleCode', 'InstanceType')
        request0.add_query_param('ModuleList.1.Config', "InstanceType:"+row[1]+",ImageOs:"+row[7])
        request0.add_query_param('ModuleList.1.PriceType', 'Hour')
        request0.add_query_param('ModuleList.2.ModuleCode', 'SystemDisk')
        request0.add_query_param('ModuleList.2.Config', "SystemDisk.Category:"+row[8]+",SystemDisk.Size:"+row[2])
        request0.add_query_param('ModuleList.2.PriceType', 'Hour')
        request0.add_query_param('ModuleList.3.ModuleCode', 'DataDisk')
        request0.add_query_param('ModuleList.3.Config', "DataDisk.Category:"+row[9]+",DataDisk.Size:"+row[3])
        request0.add_query_param('ModuleList.3.PriceType', 'Hour')
        request0.add_query_param('RegionId', 'ap-southeast-1')
        request0.add_query_param('Region', row[6])
        request0.add_query_param('SubscriptionType', row[4])
        request0.add_query_param('ProductCode', 'ecs')

        response0 = clt.do_action(request0)

        root = bs(response0, features="html.parser")
        pricing = root.find('data')
        costafterdiscount_all = pricing.find_all("costafterdiscount")
        currency = pricing.currency
        total_price = float(costafterdiscount_all[0].get_text()) + float(costafterdiscount_all[1].get_text()) + float(costafterdiscount_all[2].get_text())
        row[10] = total_price
        row[11] = total_price * float(row[5]) * 24
        row[12] = currency.get_text()
        writer.writerow(row)
        print (response0)
        count += 1





