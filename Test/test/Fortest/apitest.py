#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import pymysql

'''
respone=requests.get('http://10.66.30.71:8003/home/hot-car')
print(respone.status_code)
print(respone.text)
'''

url='http://10.66.30.71:8003/users/authorization/sign-in'
headers={"Content-Type":"application/json"}
body={
  "phone": "15705963365",
  "password": "152bf4fe99e450cd2d8f0d7798357cb2c2263f3dc27d9354fa427033ebe397fce704d0c26e34f29d2814b0940360cc241b913b7b880dbc4468c50e44a52f2853704cb2e992c349a7a8723557d2e330ab88d9df4c687fb4ba027e304c92937d11a80818c86c1b01668c629cee3f6b8363e143516ace8d24b32dbdeb0f89eddd22"
}
url1="http://10.66.30.71:8003/orders/my-orders"
body1={"paging":{"pageIndex":1,"pageSize":10},"condition":{"orderType":0}}
#session可是cookies全局有效
rs=requests.session()
respone= rs.post(url,headers=headers,data=json.dumps(body))
respone1=rs.post(url1,headers=headers,data=json.dumps(body1))
print(respone.status_code)
print(respone1.status_code)
print(respone.json())
print(respone1.json())
'''
#在接口返回结果中取某个值
phone=respone.json()['data']['phone']
print(phone)
'''
'''
#获取cookies中的token
token=str(respone.cookies)
#split()：把字符串按指定分隔符分割成多个字符串数据
token = token.split('=')[1]
token = token.split(' ')[0]
print(token)
'''
'''

#链接数据库
mysqldb=pymysql.connect("10.66.1.115","root","setpay@123","gzwl.b2c",charset='utf8')
cursor=mysqldb.cursor()
sql="SELECT id,user_name,phone from sys_user where is_delete='0'"
cursor.execute(sql)
result=cursor.fetchall()
print(result)
print(result[2][1])
'''