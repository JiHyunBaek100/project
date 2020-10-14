from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Hello jihyun")

def taskstring(request):
    result='Rest API string!'
    return HttpResponse(result, content_type="text/plain")

def form(request):
    return render(request,'restapi/requestform.html')

def responsewithhtml(request):
    #data={'first':'Jihyun','second':'Baek'}
    data=dict()
    data['first']=request.GET['first']
    data['second']=request.GET['second']
    return render(request,'restapi/responsewithhtml.html',context=data)

def template(request):
    return render(request,'restapi/template.html')