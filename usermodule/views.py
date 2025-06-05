from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render,redirect
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User_signup
from django.contrib.auth.forms import AuthenticationForm
from .models import *

# Create your views here
def homepage(request):
     return render(request,"homepage.html")


def user(request):
    return render(request, "Modules/user.html")


def rest(request):
    return render(request, "Modules/rest.html")


def agent(request):
    return render(request, "Modules/agent.html")


def admin(request):
    return render(request, "Modules/admins.html")

def emp_signup(request):
     return render(request,"employe_signup.html")

#USER-----------------------------------------------------------------------------------------------------------------------

def user_signup(request):
    if request.method == "POST":
        username = request.POST['user_name']
        mail = request.POST['email']
        password1 = request.POST['pass']
        password2 = request.POST['pass1']
        phone = request.POST['Phonenum']
        gender = request.POST['gender']
        address = request.POST['Address']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/user_signup')

        user = User.objects.create_user( username=username,email=mail,password=password1)
        applicants = User_signup.objects.create(user=user, Phone=phone, Gender=gender, type="user", Address=address)
        user.save()
        applicants.save()
        return HttpResponse("Done")
    return render(request, "User_signup.html")
def userhomepage(request):
    return render(request, "userhomepage.html")
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['user_name']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = User_signup.objects.get(user=user)

                if user1.type == "user":
                    login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect("userhomepage")
            else:
                form = True
                messages.error(request, 'Invalid username or password. Please try again.')
                return render(request, "user_login.html", {'form': form})

    return render(request, "user_login.html")
def all_Resfoods(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    restuarents1 = resturent_signup.objects.all()
    return render(request, "all_resfoods.html",{'restuarents1':restuarents1})
def all_foods1(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    allfoods=Add_Food.objects.all()
    return render(request, "AllFoods_user.html",{'allfoods':allfoods})
def refood(request,pk):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    # restuarents1 = resturent_signup.objects.filter(id=pk)
    allfoods=Add_Food.objects.filter(user_id=pk)
    return render(request, "AllFoods_user.html",{'allfoods':allfoods})

def order(request,pk):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    food = Add_Food.objects.filter(id=pk)
    return render(request,"order.html",{'food':food})
def order1(request,pk):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    if request.method == "POST":
        val=request.POST['count']
        usera = request.user
        user1 = User_signup.objects.get(user=usera)
        food=Add_Food.objects.get(id=pk)
        res=food.user
        ord=Order.objects.create(user=user1,quantity=val,food=food,res=res,ordered="False")
        ord.save()
        allorders=Order.objects.filter(user=user1)
        totcost = sum(int(it.food.cost) * int(it.quantity) for it in allorders)
        noitems=sum(int(it.quantity) for it in allorders)
        food = Order.objects.filter(user=user1)

    return render(request, "order1.html", {'food': allorders,'totcost':totcost,'noitems':noitems})

def orderdel(request,pk):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    food = Order.objects.filter(id=pk)
    food.delete()
    return render(request,"order.html")

def deletefood(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    food = Order.objects.filter(id=pk)
    food.delete()
    return render(request,"order.html")
def order2(request,pk):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    if request.method == "POST":
        val=request.POST['count']
        usera = request.user
        user1 = User_signup.objects.get(user=usera)
        food=Add_Food.objects.get(id=pk)
        res=food.user
        ord=Order.objects.create(user=user1,quantity=val,food=food,res=res,ordered="False")
        ord.save()
    #     allorders=Order.objects.filter(user=user1)
    #     totcost = sum(int(it.food.cost) * int(it.quantity) for it in allorders)
    #     noitems=sum(int(it.quantity) for it in allorders)
    #     food = Order.objects.filter(user=user1)
    #
    # return render(request, "order1.html", {'food': allorders,'totcost':totcost,'noitems':noitems})
    return render(request, "order1.html")
def placeorder(request,pk):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    food = Add_Food.objects.filter(id=pk)
    return render(request,"order1.html",{'food':food})

def contactus(request):
    return render(request, "contactus.html")
def orderplaced(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    user1 = User_signup.objects.get(user=request.user)
    food = Order.objects.filter(user=user1)
    for i in food:
        book=UserOrder(user=i.user,food=i.food,quantity=i.quantity,res=i.res,ordered=i.ordered)
        book.save()
    food.delete()
    return render(request, "orderplaced.html")

def orders(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    user1 = User_signup.objects.get(user=request.user)
    # food = UserOrder.objects.filter(user=user1)
    food = UserOrder.objects.all()
    return render(request, "userorders.html",{'food': food})
def history(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    user1 = User_signup.objects.get(user=request.user)
    # food = UserOrder.objects.filter(user=user1)
    food = UserOrder.objects.all()
    return render(request, "Userhistory.html",{'food': food})
def back(request):
    return render(request, "userhomepage.html")

def restorder(request):
    if not request.user.is_authenticated:
        return redirect("/resturent_login")
    id=resturent_signup.objects.get(user=request.user)
    food = UserOrder.objects.all()
    return render(request, "resOrders.html", {'food': food})
def all_orders(request):
    if not request.user.is_authenticated:
        return redirect("/employe_login")
    # id=resturent_signup.objects.get(user=request.user)
    food = UserOrder.objects.all()
    return render(request, "all_orders.html", {'food': food})
def logouts(request):
    logout(request)
    return redirect('/')

#REST---------------------------------------------------------------------------------------------------------------------
def rest_signup(request):
    if request.method == "POST":
        username = request.POST['user_name']
        mail = request.POST['email']
        password1 = request.POST['pass']
        password2 = request.POST['pass1']
        phone = request.POST['Phonenum']
        img = request.FILES['image1']
        address = request.POST['Address']
        a = request.POST['restName']
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/rest_signup')

        user = User.objects.create_user( username=username,email=mail,password=password1)
        applicants = resturent_signup.objects.create(user=user, Phone=phone, type="rest",status="pending", Address=address,image1=img, RestName=a)
        user.save()
        applicants.save()
        return HttpResponse("Done")
    return render(request, "rest_signup.html")
def resturenthomepage(request):
    return render(request, "resturenthomepage.html")
def resturent_login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            user1 = resturent_signup.objects.get(user=user)
            if user1.type == "rest" or user1.status != "pending":
                login(request, user)
                return redirect("resturenthomepage")
        else:
            alert = True
            return render(request, "resturent_login.html", {"alert": alert})
    return render(request, "resturent_login.html")
def Add_food(request):
    if not request.user.is_authenticated:
        return redirect("/resturent_login")
    return render(request, "Add_food.html")
def Add_food1(request):
    if not request.user.is_authenticated:
        return redirect("/resturent_login")
    if request.method == "POST":
        usera = request.user
        user1 = resturent_signup.objects.get(user=usera)
        category = request.POST['category']
        name = request.POST['name']
        region = request.POST['region']
        non = request.POST['VEG']
        price = request.POST['price']
        img = request.FILES['image']
        food = Add_Food.objects.create(user=user1,Category=category, Name=name,  region=region,vnv=non,cost=price,image=img)
        food.save()
        return HttpResponse("DONE")
    return render(request, "Add_food.html")
def all_foods(request):
    if not request.user.is_authenticated:
        return redirect("/resturent_login")
    us=request.user
    restuarents1 = resturent_signup.objects.get(user=us)
    allfoods=Add_Food.objects.filter(user=restuarents1)
    return render(request, "all_foods.html",{'allfoods':allfoods})
def sent(request):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    if request.method == "POST":
        name = request.POST['name']
        mail = request.POST['email123']
        contact = request.POST['con']
        text = request.POST['mess']
        user1=request.user
        feedback1 = feedback.objects.create(usname=name, mail=mail, cont=contact,mess=text)
        feedback1.save()
        return render(request, "contactus.html")
    return render(request, "contactus.html")

def feedbacks(request):
    feeds = feedback.objects.all()
    return render(request,"allfeedbacks.html",{'feeds':feeds})
#Employee---------------------------------------------------------------------------------------------------------------------
def emp_signup(request):
    if request.method == "POST":
        username = request.POST['user_name']
        mail = request.POST['email']
        password1 = request.POST['pass']
        password2 = request.POST['pass1']
        phone = request.POST['Phonenum']
        gender= request.POST['gender']
        address = request.POST['Address']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('emp_signup')

        user = User.objects.create_user( username=username,email=mail,password=password1)
        applicants = employe_signup.objects.create(user=user, Phone=phone, type="employee",status="pending", Address=address, Gender=gender)
        user.save()
        applicants.save()
        return HttpResponse("Done")
    return render(request, "employe_signup.html")
def employehomepage(request):
    return render(request, "employehomepage.html")
def employe_login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            user1 = employe_signup.objects.get(user=user)
            if user1.type == "employee" or user1.status != "pending":
                login(request, user)
                return redirect("employehomepage")
        else:
            alert = True
            return render(request, "employe_login.html", {"alert": alert})
    return render(request, "employe_login.html")

def all_restuarents(request):
    if not request.user.is_authenticated:
        return redirect("/employe_login")
    restuarents1 = resturent_signup.objects.all()
    return render(request, "all_restaurents.html",{'restuarents1':restuarents1})




#Admin---------------------------------------------------------------------------------------------------------------------
def admin_login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user.is_superuser:
            login(request, user)
            return redirect("adminhomepage")
        else:
            alert = True
            return render(request, "admin_login.html", {"alert": alert})
    return render(request, "admin_login.html")
def ad_resturents(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    restuarents=resturent_signup.objects.all()
    return render(request, "Admin/ad_resturents.html",{'restuarents':restuarents})
def ad_Agents(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    employees=employe_signup.objects.all()
    return render(request, "Admin/ad_Agents.html",{'employees':employees})
def ad_Users(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    users=User_signup.objects.all()
    return render(request, "Admin/ad_Users.html",{'users':users})
def adminhomepage(request):
    return render(request, "adminhomepage.html")
# def adduserdata(request):
#     if request.method == 'POST':
#         username = request.POST['user_name']
#         pass1 = request.POST['pass']
#         pass2 = request.POST['pass1']
#         mail=request.POST['email']
#         phone=request.POST['phonenum']
#         if pass1 == pass2:
#             if User.objects.filter(username=username).exists():
#                 # messages.info(request, 'OOPS! Username already taken.')
#                 return render(request, 'register.html')
#             else:
#                 user = User.objects.create_user(username=username, password=pass1,email=mail,phone=phone)
#                 user.save()
#                 # messages.info(request, 'Account created Successfully')
#                 return render(request, 'homepage.html')
#         else:
#             messages.info(request, 'Password does not match')
#             return render(request, 'signup.html')
# def login1(request):
#     if request.method=='POST':
#         username=request.POST['user_name']
#         pass1=request.POST['password']
#         print(username,pass1)
#         user=authenticate(username=username,password=pass1)
#         print(user)
#         if user is not None:
#             login(request,user)
#             if username == "Admin" and user.check_password("ADMIN"):
#                 # Redirect to the appropriate homepage for the admin
#                 return redirect('adminhomepage')
#             elif len(username)==10:
#                 return redirect('userhomepage')
#             elif len(username)==4:
#                 return redirect('employehomepage')
#             elif len(username)==5:
#                 return redirect('resturenthomepage')
#             else:
#                 return redirect('homepage')
#         else:
#             # return HttpResponse("ram")
#             return render(request,'login.html')
#     else:
#
#         return render(request,'login.html')






# def Logins(request):
#     if  request.user.is_authenticated:
#         return redirect("/")
#     else:
#         if request.method == "POST":
#             username = request.POST['user_name']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             print(user)
#             if user is not None:
#                 user1 = resturent_signup.objects.get(user=user)
#                 if user1.type == "user":
#                     login(request, user)
#                     return redirect("userhomepage")
#                 elif user1.type == "employee":
#                     login(request, user)
#                     return redirect("employehomepage")
#                 elif user1.type == "rest":
#                     login(request, user)
#                     return redirect("resturenthomepage")
#             elif user is not None:
#                 user1 = resturent_signup.objects.get(user=user)
#                 if user1.type == "user":
#                     login(request, user)
#                     return redirect("userhomepage")
#                 elif user1.type == "employee":
#                     login(request, user)
#                     return redirect("employehomepage")
#                 elif user1.type == "rest":
#                     login(request, user)
#                     return redirect("resturenthomepage")
#             elif user is not None:
#                 user1 = employe_signup.objects.get(user=user)
#                 if user1.type == "user":
#                     login(request, user)
#                     return redirect("userhomepage")
#                 elif user1.type == "employee":
#                     login(request, user)
#                     return redirect("employehomepage")
#                 elif user1.type == "rest":
#                     login(request, user)
#                     return redirect("resturenthomepage")
#
#             else:
#                 thank = True
#                 return render(request, "user_login.html", {"thank": thank})
#     return render(request, "user_login.html")


    # if  request.user.is_authenticated:
    #     return redirect("/")
    # else:
    #     if request.method == "POST":
    #         username = request.POST['user_name']
    #         password = request.POST['password']
    #         user = authenticate(username=username, password=password)
    #         print(user)
    #         if user is not None:
    #             user1 = User_signup.objects.get(user=user)
    #
    #             if user1.type == "user":
    #                 login(request, user)
    #                 return redirect("userhomepage")
    #         else:
    #             thank = True
    #             return render(request, "login.html", {"thank": thank})
















