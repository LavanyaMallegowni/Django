from django.shortcuts import render

# Create your views here.
def rose(request):
  d={'name':'sanny','age':56}
  return render(request,'index.html',context=d)


def apple(request):
  return render(request,'index.html')
