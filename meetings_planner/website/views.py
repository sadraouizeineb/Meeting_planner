from django.shortcuts import render

from meetings.models import Meeting

# Create your views here.
# def home_view(request):
#    return render(request,"home.html")

# def about_view(request):
#   return render(request,"about.html")


def home_view(request):
   context={'nbre_meeting': Meeting.objects.count()}
   return render(request,"home.html",context=context)

def about_view(request):
  return render(request,"about.html")