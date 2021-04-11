from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the homepage of accountant.")


def notice(request):
    return HttpResponse("This is notice page for accountant")


def logBook(request):
    return HttpResponse("This is log book page for accountant.")
