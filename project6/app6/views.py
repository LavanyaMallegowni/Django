from django.shortcuts import render

# Create your views here.
def flowers(request):
  d = {'name':'lavanya'}
  return render(request,'jasmine.html',d)

def loop(request):
  d = {'age':34,'name':'pavan'}
  return render(request,'loop.html',d)

