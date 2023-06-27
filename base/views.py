from django.http import HttpResponse

def demoText(request):
    return HttpResponse("Test")