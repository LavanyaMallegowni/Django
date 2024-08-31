from django.shortcuts import render

# Create your views here.
def loop(request):
  d = {'name':'laanya','mbn':[233423,436456]}
  return render(request,'looping.html',d)

def condition(request):
  return render(request,'lavi.html')