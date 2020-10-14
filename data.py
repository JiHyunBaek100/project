import pymongo
from pymongo import MongoClient
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

client=MongoClient()

client= MongoClient('localhost',27017)

db=client['prodb']
coll=db['prodb']

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="/home/bjh/Documents/Develop/chromedriver", options=options)
browser.get("https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?keyword=%EC%A0%84%EC%9E%90%EA%B3%B5%ED%95%99%EA%B3%BC")

time.sleep(3)

#data = browser.find_element_by_css_selector('a[href="#none"]')
aa=list()
comp=list()
payl=list()

data=browser.find_elements_by_class_name('cp-info-in')
company=browser.find_elements_by_class_name('cp_name')
#pay=browser.find_elements_by_class_name('cp-info')

for i in range(1,11):
    pay=browser.find_elements_by_css_selector(f'#list{i} > td:nth-child(4) > div')
    for i in pay:
       payl.append(i.text)

for i in data:
    aa.append(i.text)
for i in company:
    comp.append(i.text)

data={}
for value in zip(comp, aa, payl):
    key = ['company','jobs','pay']
    for k,v in zip(key,value):
        data[k]=v
    print(data)

# doc={"first":data.text}
# coll=db.collection
# coll.insert(doc)

# result=coll.find()
# for i in result:
#     print(i)
# print(data_list.text)
