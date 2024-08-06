from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.core.mail import send_mail

# Create your views here.
def home(request):
    # return HttpResponse("This is Home Page")
    context = {'name':'Boss','course':'Django'}
    return render(request,'home.html',context)
def about(request):
    # return HttpResponse("This is ABout Page")
    return render(request,'about.html')
def project(request):
    # return HttpResponse("This is project Page")
    return render(request,'projects.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name,email,phone,desc)
        # ins = Contact(name=name, email=email, phone=phone, desc=desc)
        # ins.save()
        print("Db is written")
        send_mail(
            "Details",
            f"""
                Name: {name},
                Email: {email}
                Phone: {phone}
                Description: {desc}
            """,
            "290anamika@gmail.com",
            ["madhusudhanar2020@gmail.com"],
            fail_silently=False,
        )
    # return HttpResponse("This is contact Page")
    return render(request,'contact.html')

# def path(request):

#     context = {
#         'heading':"Django tutorial 1",
#         'content': "CHECKING    "
#     }
#     return HttpResponse("Path Page")