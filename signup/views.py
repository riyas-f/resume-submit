from django.shortcuts import render
from signup.models import Employee 

# Create your views here.

def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        Gender = request.POST.get('Gender')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        position = request.POST.get('position')
        address = request.POST.get('street')
        zipcode = request.POST.get('zip')
        district = request.POST.get('place')
        phone = request.POST.get('phone')
        email = request.POST.get('your_email')
        resume = request.POST.get('resume')
        savedata = Employee(title=title, fname=fname, lname=lname, gender=Gender, dob=dob, position=position, address=address, zipcode=zipcode, district=district, phone=phone, email=email,
                        resume=resume,age=age,
                        )
        
        savedata.save()
        print('usercreated')
        return render(request ,'index.html')

    else:
        return render(request ,'index.html')