from django.shortcuts import render

# Create your views here.
def home (request):
    return HttpResponse("Hello jihyun")

def taskstring(request):
    result='Rest API string!'
    return HttpResponse(result, content_type="text/plain")