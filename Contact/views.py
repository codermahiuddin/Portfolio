from django.shortcuts import render
from .models import Contact


def ContactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name,email=email,subject=subject,msg=message)
        contact.save()
        successmsg = True
        return render(request,'contact.html', {'successmsg':successmsg,'name':name})
    

    return render(request, 'contact.html')

