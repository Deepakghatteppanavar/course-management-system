from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models import signup,register

# Create your views here
class HomeView(View):
    def get(self,request):
        return render(request, 'home.html')

class AboutView(View):
    def get(self,request):
        return render(request, 'about.html')
    
class LoginView(View):
    def get(self,request):
        return render(request, 'loginpage.html')

    def post(self,request):
        username=request.POST['username']
        pass1=request.POST['pass']
        # print(username,pass1)
        users = signup.objects.filter(username=username)

        print(users)
        if users.exists() and users[0].password==pass1:
            return redirect('register')
        elif not users.exists():
            return HttpResponse("your account is not yet created please create your account and login ")
        else:
            return HttpResponse("username or password is incorrect")

class SignupView(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        uname=request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            return HttpResponse("password and confirm password are mismatched")
        else:
            my_string = str(email)
            my_string1 = str(pass1)

            my_user = signup.objects.create(username=uname,password=pass1,email=email)
            my_user.save()
            return redirect('loginpage')

class RegView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        first = request.POST['first']
        last=request.POST['last']
        mother_name=request.POST['mother_name']
        father_name=request.POST['father_name']
        address=request.POST['address']
        phone=request.POST['phone']
        gender=request.POST['gender']
        dob=request.POST['dob']
        pincode=request.POST['pincode']
        course=request.POST['course']
        email = request.POST['email']
        my_user = register.objects.create(first=first, last=last, mother_name=mother_name,father_name=father_name,address=address,phone=phone,
                                          gender=gender, dob=dob, pincode=pincode, course=course, email=email)
        t=my_user.save()
        return render(request,'table.html')

class TableView(View):
    def get(self,request):
        return render(request,'table.html')


def orderView(request):
    if request.method == 'GET':
        students = register.objects.all()
        return render(request, 'table.html', {'student': students})
    else:
        return HttpResponse("hello")
    
class navbarView(View):
    def get(self,request):
        return render(request,'navbar.html')