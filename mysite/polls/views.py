from django.shortcuts import render

# Create your views here.
def index(request):
  return(request, 'polls/demo_site.html')
