from django.shortcuts import render
from  django.http import HttpResponse
from pymongo import MongoClient
# Create your views here.

def jhyun(request):
    return render(request,'proj/fpr.html')

def mongolist(request):
    data=request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        prodb=client.prodb
        contact_list=list(prodb.collection.find({}))
        data['first']=contact_list
    return render(request,'proj/fpr.html',context=data)