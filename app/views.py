from django.shortcuts import render

# Create your views here.
def app_hi(request):
    return render(request,'app/vikas.html')
