from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

'''
视图函数需要一个参数，类型应该HttpRequest
'''
def do_normalmap(request):
    print("In normalmap")
    daiye = HttpResponse("屌你老母")
    return daiye
    #return HttpResponse("This is normalmap")

def withparam(request, year, month):
    return HttpResponse("This is with param {0}, {1}".format(year,month))

def do_app(request):
    print("In teacher app")
    return HttpResponse("叼勾你")

def do_param2(request,page_number):
    print("In do_param2")
    return HttpResponse("Page Number is {0}".format(page_number))

def extremParam(r,name):
    return HttpResponse("My name is {0}".format(name))

def revParse(r):
    return HttpResponse("Your request URL is {0}".format(reverse("askname")))