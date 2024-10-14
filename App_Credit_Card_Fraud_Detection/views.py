from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session
import math, random
import requests
import re
from django.db.models import Avg
import datetime
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import joblib
import pickle
import socket
from django.db.models import Count
from django.db.models import Max
from getmac import get_mac_address as gma # type: ignore
# Create your views here.

def home(request):
    return render(request,'home.html',{})


def View_Customer(request):
    #distinct = User_Transactions.objects.values('Name').annotate(name_count=Count('Name')).filter(name_count=1)
    #show = User_Transactions.objects.filter(Name__in=[item['Name'] for item in distinct])
    #print(show)
    show = User_Transactions.objects.all().values('Name','email_address').distinct()
    return render(request,'View_Customer.html',{'show':show})



def Admin_login(request):
    if request.method == "POST":
        email_id = request.POST['email_id']
        admin_pwd = request.POST['password']
        print(admin_pwd)
        if admin_details.objects.filter(admin_email=email_id).exists():
            ad = admin_details.objects.all().filter(admin_email=email_id)
            for i in ad:
                pwd = i.admin_pwd
                print(pwd)
                if int(pwd)==int(admin_pwd):
                    print('d')
                    
                   
                    
                    digits = "0123456789"
                    OTP = ""
                    for i in range(4) :
                        OTP += digits[math.floor(random.random() * 10)]
                    print(OTP)
                    request.session['OTP'] = OTP
                    print(request.session['OTP'])
                    url = "https://smail.azurewebsites.net/Email.aspx?Title=OTP Verification&emailid={email}&Sub=TestSubject&Msg=OTP  is {OTP}.".format(OTP=OTP,email = email_id)
                    res = requests.post(url)
                    return redirect("/verify")
                else:
                    print('z')
                    messages.error(request, 'Wrong Password')
                    return redirect("/Admin_login")


            #request.session['login'] = "Yes"
            return redirect("/")
        else:
            print('y')
            messages.error(request, 'Email Address is not registered in the system')
    else:
        return render(request, "Admin_login.html", {})
    return render(request,'Admin_login.html',{})


    return render(request,'Admin_login.html',{})


def Fraudulent_Customers(request):
    data = User_Transactions.objects.all().filter(Flagged_Status = 'Flagged')

    return render(request,'Fraudulent_Customers.html',{'data':data})


model = pickle.load(open("model_pkl", "rb"))



def Generate_Payment_link(request):
    if request.method == "POST":
        P_id = request.POST['P_id']
        print(P_id)
        fullname = request.POST['fullname']
        email_id = request.POST['Email_Address']
        phonenumber = request.POST['Phone_number']
        cardNo = request.POST['cardno']
        cvv = request.POST['cvv']
        date = request.POST['date']
        
        Amount = request.POST['Amount']
        Country = request.POST['Country']

        Ip_address = request.POST['ip_address']
        current_time = datetime.datetime.now()
        current_time = str(current_time).split()
        print(current_time)
        date = current_time[0]
        time = current_time[1]
        print('date',date)
        print('time',time)

        #Billing Address
        Street_address1 = request.POST['Street_address1']
        Zipcode1 = request.POST['Zipcode1']
        City1 = request.POST['City1']
        State1 = request.POST['State1']

        #Shipping Address
        Street_address2 = request.POST['Street_address2']
        Zipcode2 = request.POST['Zipcode2']
        City2 = request.POST['City2']
        State2 = request.POST['State2']
        
        classes = ['Declined Transaction', 'Under-Review Transaction','Flagged Transactions', 'Fraud', 'Complete Transactions']
        data = User_Transactions.objects.all().filter(id = P_id)
        for i in data:
            dates = i.created_link_date
            times = i.created_link_time
            exempt_rules = i.exempt_rules
            country = i.country

            print('exempt_rules',exempt_rules)
            date_list = str(dates).split('-')
            print('data',i.created_link_date)
            print('data',i.created_link_time)
            print(str(dates).split('-'))
            print(str(times).split(':'))

        


        data = User_Transactions.objects.all().filter(id = P_id).update(Name = fullname,CINO = cardNo,expiry_date = date,payment_Date=date, payment_Time=time,email_address =email_id ,phonenumber= phonenumber)
        #Checking valid credit card number
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False
        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNo[i]) - ord('0')
            if (isSecond == True):
                d = d * 2

            nSum += d // 10
            nSum += d % 10
            isSecond = not isSecond
        if (nSum % 10 == 0):
            print('true')

            if exempt_rules == 'No':

                ##Under-Review Transaction
                #1.If a person's email or cnic has been used with more than 3 credit cards
                Credit_cards = User_Transactions.objects.all().filter(Name = fullname).values('CINO').distinct().count()
                print('Credit_cards',Credit_cards)
                if int(Credit_cards) < 4:
                    f1 = 0
                    print('Credit_cards valid')
                else:
                    f1 = 1
                    print('Credit_cards invalid')
            
        



                #2.Transaction amount is greater than $300
                if int(Amount) < 25000:
                    print('valid')
                    f2 = 0
                else:
                    f2 = 1
                    print('invalid')

        

                #3.If 7 or more transactions have been made in a 24-hour period.
                data = User_Transactions.objects.all().filter()
                date_from = datetime.datetime.now() #- datetime.timedelta(days=1)
                print(date_from)
                transactions = User_Transactions.objects.all().filter(Name=fullname, payment_Date__gte=date_from).count()
                print('created_documents',transactions)
                if int(transactions) >= 5:
                    print('valid')
                    f3 = 0
                else:
                    f3 = 1
                    print('invalid')

                
        


                #4. Checking if Billing Address and Shipping Address

                if (Street_address1.lower().strip() == Street_address2.lower().strip()) and (Zipcode1.lower().strip() == Zipcode2.lower().strip()) and (City1.lower().strip() == City2.lower().strip()) and (State1.lower().strip() == State2.lower().strip()):
                    print('valid')
                    f4 = 0
                else:
                    f4 = 1
                    print('invalid')

            
        


                ##Declined Transaction:

                #1.If the Customer Country (Billing or Shipping) do not match the country set by the admin.
                #Check_country = User_Transactions.objects.filter(id = P_id,country = Country)
                #print(Check_country)
                #for i in Check_country:
                #    country = i.country
                #    print(i.country)
                if Country == country:
                    print('valid')
                    f5 = 0
            
                else:
                    f5 = 1
                    print('invalid')

        
                #2.If the customer is using a vpn to make transaction.
                hostname = socket.gethostname()
                ## getting the IP address using socket.gethostbyname() method
                ip_address = socket.gethostbyname(hostname)
                ## printing the hostname and ip_address
                print(f"Hostname: {hostname}")
                print(f"IP Address: {ip_address}")
                mac_address = gma()
                print('mac_address',mac_address)
                ip = User_Transactions.objects.all().filter(ip_address = ip_address,mac_address = mac_address,Flagged_Status = 'Flagged')
                print('ip',ip)
                if User_Transactions.objects.all().filter(ip_address = ip_address,mac_address = mac_address,Flagged_Status = 'Flagged').exists():
                    messages.info(request, 'Your transaction is Declined')
                    return redirect('/')
                    print('ip valid')
                    f6 = 1
                else:
                    print('ip invalid')
                    f6 = 0
                
             
        
            



                #3.Transaction frequency is not normal (unusual pattern).
                Freq = User_Transactions.objects.all().filter(Name=fullname).aggregate(Avg('Amount'))
                print(Freq)
                Average_amount = Freq.get('Amount__avg')
                print(Average_amount)
                print(Freq.get('Amount__avg'))
                if int(Amount) <= int(Average_amount):
                    print('valid')
                    f7 = 0
                else:
                    f7 = 1
                    print('invalid') 

              
        


                ##Flagged Transactions:
                #1.If the customer Ip Adress, Mac Adress or email Adress is flagged already in our system for fraudulent activity.
                data = User_Transactions.objects.all().filter(Name = fullname).filter(Flagged_Status = 'Fraud').exists()
                print('data',data)
                if data != 'True':
                    print('valid')
                    f8 = 0
                else:
                    f8 = 1
                    print('invalid')

               



                #2. If the customer email Adress is from an unusual domain.
                domain_list = ['gmail.com','outlook.com','yahoo.com','csu.edu']
                email_ids = email_id.split('@')
                print(email_ids[1])
                if email_ids[1] in domain_list:
                    print('valid')
                    f9 = 0
                else:
                    f9 = 1
                    print('invalid')

                if f1 == 1 or f2 == 1 or f3 == 1 or f4 == 1 or f5 == 1 or f9 == 1:
                    User_Transactions.objects.filter(id=P_id).update(Flagged_Status='Flagged')
                    #print("Transaction flagged as under review")
                else:
                    # Optionally, reset the status if no flagging condition is met
                    User_Transactions.objects.filter(id=P_id).update(Flagged_Status=None)
                    #print("Transaction passed all checks") 
        

                
                prediction = model.predict([[int(f1),int(f2),int(f3),int(f4),int(f5),int(f6),int(f7),int(f8),int(f9)]])
                class_num = prediction[0]
                print(prediction[0])
                class_name = classes[class_num]
                print('class_name',class_name)
                #User_Transactions.objects.all().filter(id = P_id).update(Type_of_transaction = class_name,Status = 'Not Fraud' )
                if class_name == "Complete Transactions":
                    User_Transactions.objects.all().filter(id = P_id).update(ip_address = ip_address,mac_address = mac_address,Status = 'Completed',Type_of_transaction = class_name,Flagged_Status = 'None')
                    #message = 'You transactions is a' + class_name
                    messages.success(request, 'Payment Done Successfully')  # Change to success
                    #messages.error(request, 'Payment Done Succesfully')
                elif class_name == "Flagged Transactions":
                    User_Transactions.objects.all().filter(id = P_id).update(ip_address = ip_address,mac_address = mac_address,Status = 'Pending',Type_of_transaction = class_name,Flagged_Status = 'Flagged')
                    messages.error(request, 'You transactions is a' + ' ' + class_name)
                else:
                    User_Transactions.objects.all().filter(id = P_id).update(ip_address = ip_address,mac_address = mac_address,Status = 'Pending',Type_of_transaction = class_name,Flagged_Status = 'None' )
                    message = 'You transactions is a' + class_name
                    messages.error(request, 'You transactions is a' + ' ' + class_name)
                #messages.error(request, 'You transactions is a' + ' ' + class_name)
                #messages.error(request, 'Payment Done Succesfully')
                return redirect('/')

            else:
                data = User_Transactions.objects.all().filter(id = P_id).update(Name = fullname,CINO = cardNo,expiry_date = date,payment_Date=date, payment_Time=time,email_address =email_id ,phonenumber= phonenumber)
                messages.error(request, 'Payment Done Succesfully')













 

        else:
            messages.error(request, 'Wrong card number,Please try again')
            print('false')
            
            return render(request,'Generate_Payment_link.html',{'id':P_id,'fullname':fullname,'email_id':email_id,'phonenumber':phonenumber,'Street_address1':Street_address1,'Zipcode1':Zipcode1,'City1':City1,'State1':State1,'Street_address2':Street_address2,'Zipcode2':Zipcode2,'City2':City2,'State2':State2,'Amount':Amount,'Country':Country,'Ip_address':Ip_address})


        



        


    return render(request,'Generate_Payment_link.html',{})

def base(request):
    return render(request,'base.html',{})

def verify(request):
    if request.method == "POST":
        otp = request.POST['otp']
        #email_id = request.session['type_id']
        otps = request.session['OTP']
        if int(otp)==int(otps):
            print(otp,otps)
            request.session['type_id'] = 'Admin'
            print(request.session['type_id'])
            request.session['UserType'] = 'Admin'
            request.session['login'] = "Yes"
            #request.session['UserType'] = 'Admin'
            return redirect('/')
        else:
            messages.error(request, 'Wrong OTP')



    return render(request,'verify.html',{})


def Logout(request):
    Session.objects.all().delete()
    return redirect("/")








def User_Registeration(request):
    if request.method=="POST":
        name=request.POST['fullname']
        age=request.POST['Age']
        address=request.POST['Address']
        phonenumber=request.POST['phonenumber']
        gender = request.POST['Gender']
        Email = request.POST['Email']
        password = request.POST['Password']
        City = request.POST['City']
        State = request.POST['State']
        Country = request.POST['Country']
        obj=User_Details(name=name,age=age,address=address,phonenumber=phonenumber,gender=gender,Email=Email,password=password,City=City,State=State,Country=Country)
        obj.save()
        return redirect('/User_Login')
    else:
        return render(request,'User_Registeration.html',{})

def User_Login(request):
    if request.method == "POST":
        C_email = request.POST['email_id']
        C_password = request.POST['password']
        if User_Details.objects.filter(Email=C_email, password=C_password).exists():
            users = User_Details.objects.all().filter(Email=C_email, password=C_password)
            messages.info(request, 'logged in')
            request.session['UserId'] = users[0].id
            request.session['type_id'] = 'User'
            request.session['UserType'] = users[0].name
            request.session['login'] = "Yes"
            return redirect("/")
        else:
            messages.info(request, 'Not Registered Please Register')
            return redirect("/User_Registeration")
    else:
        return render(request,'User_Login.html',{})

def Create_Payment_Link(request):
    if request.method == "POST":
        users = User_Transactions.objects.all()
        next_id = users.aggregate(Max('id'))['id__max'] + 1 if users else 1
        print(next_id)
        email = request.POST['email']
        Amount = request.POST['Amount']
        Country = request.POST['Country']
        rules = request.POST['Rules']
        print(gma())
        
        # datetime object containing current date and time
        current_time = datetime.datetime.now()
        current_time = str(current_time).split()
        print(current_time)
        current_time = datetime.datetime.now()
        current_time = str(current_time).split()
        print(current_time)
        date = current_time[0]
        time = current_time[1]
        print('date',date)
        print('time',time)

        #url = "https://smail.azurewebsites.net/Email.aspx?Title=OTP Verification&emailid={email}&Sub=TestSubject&Msg=OTP  is {OTP}.".format(OTP=OTP,email = email_id)
        #res = requests.post(url)
        
        date_from = datetime.datetime.now()
        #print("date and time =", dt_string)
        link = User_Transactions(Amount=Amount,country=Country,created_link_date=date_from,created_link_time=time,exempt_rules = rules,email_address = email,Status = 'Pending')
        link.save()

        last_record = User_Transactions.objects.all().values().last()
        print(last_record['id'])
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        Ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        print("Mac Address:",gma())
        print(f"Hostname: {hostname}")
        print(f"IP Address: {Ip_address}")
        return render(request,'Generate_Payment_link.html',{'id':last_record['id'],'Amount' : last_record['Amount'],'Country': last_record['country'],'Ip_address':Ip_address})

        '''for i in last_record:
                                    print(i.id)'''
    else:
        users = User_Transactions.objects.all()
        next_id = users.aggregate(Max('id'))['id__max'] + 1 if users else 1
        print(next_id)
        return render(request,'Create_Payment_Link.html',{})

def View_Details(request,user_name):
    print(user_name)
    data = User_Transactions.objects.all().filter(email_address = user_name)
    print(data)
    return render(request,'View_Details.html',{'data':data})

def Update_status(request, id):
    try:
        data = User_Transactions.objects.get(id=id)  # Use .get() to fetch a single object
    except User_Transactions.DoesNotExist:
        messages.error(request, "Transaction not found")
        return redirect('/View_Customer')  # Redirect or handle the case when the transaction is not found

    return render(request, 'Update_status.html', {'data': data})

"""def Update_status(request,id):
    data = User_Transactions.objects.all().filter(id = id)
    print(data)
    return render(request,'Update_status.html',{'data': data})"""

def Flag_update(request):
    if request.method == "POST":
        t_id = request.POST.get('P_id')  # Using .get() to safely fetch values
        fullname = request.POST.get('fullname')
        Phone_number = request.POST.get('Phone_number')
        Country = request.POST.get('Country')
        Email_Address = request.POST.get('Email_Address')
        Amount = request.POST.get('Amount')
        Flagged_Status = request.POST.get('Flagged_Status')  # Ensure this is fetched correctly
        
        if Flagged_Status:  # Check if Flagged_Status is actually provided
            data = User_Transactions.objects.filter(id=t_id).update(Flagged_Status=Flagged_Status)
            messages.success(request, 'Status Updated Successfully')
        else:
            messages.error(request, "Flagged Status not provided")
        
        return redirect('/View_Customer')
    
    return render(request, 'Flag_update.html', {})

"""
def Flag_update(request):
    if request.method == "POST":
        t_id = request.POST['P_id']
        fullname = request.POST['fullname']
        Phone_number = request.POST['Phone_number']
        Country = request.POST['Country']
        Email_Address = request.POST['Email_Address']
        Amount = request.POST['Amount']
        Flagged_Status = request.POST['Flagged_Status']
        data = User_Transactions.objects.all().filter(id = t_id).update(Flagged_Status=Flagged_Status)
        messages.success(request, 'Status Updated Sucessfully')
        return redirect('/View_Customer')
    else:
        return render(request,'Flag_update.html',{})"""