from django.shortcuts import render

# Create your views here.
def sendemail(request):
    return render(request, 'email.html',{'title':'Send Email'})   