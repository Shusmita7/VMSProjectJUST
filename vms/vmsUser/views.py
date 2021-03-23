from django.shortcuts import render
from django.http import HttpResponse


def userHome(request):
    return HttpResponse("Hello, world. You're at the homepage of user.")


def notice(request):
    return HttpResponse("This is notice page")


def requisition(request):
    return HttpResponse("This is requisition page")


def forChairman(request):
    return HttpResponse("This is the Chairman special page")


def usercost(request):
    return HttpResponse("This is cost page")


def profile(request):
    return HttpResponse("This is profile page")


def updateprofile(request):
    return HttpResponse("This is Update profile page")
