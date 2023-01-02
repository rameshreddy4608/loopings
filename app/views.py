from django.shortcuts import render

# Create your views here.
def loopings(request):
    d={'name':'RAMESHREDDY'}
    return render(request,'loopings.html',d)