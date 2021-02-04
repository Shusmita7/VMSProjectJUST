from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the homepage of user.")


def notice(request):
    return HttpResponse("This is notice page")


def schedule(request):
    return HttpResponse("This is schedule page")


def viewuser(request):
    return HttpResponse("This is View User list page")


def usercost(request):
    return HttpResponse("This is user cost page")


def requests(request):
    return HttpResponse("This is requisition request page")


def driver(request):
    return HttpResponse("This is vehicle page")


def vehicle(request):
    return HttpResponse("This is vehicle page")


def profile(request):
    return HttpResponse("This is profile page")


def updateprofile(request):
    return HttpResponse("This is Update profile page")
