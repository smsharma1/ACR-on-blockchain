from django.shortcuts import render
from django.http import HttpResponse
from .forms import CardForm, CustomUserCreationForm, Ratee_submit_appraisal_application, LeaveRecord, Appraisal, MarkAttendance
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.template import Context, loader 
import requests, json, urllib, base64, datetime


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def card_upload(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            url = 'http://172.27.20.177:3000/api/wallet/import'
            r = ''
            print("Files", request.FILES.get('document'))
            r = requests.post(url, files={'temp.card': request.FILES.get('document')})
            if r.status_code != 200:
                print(r.content, "error on transaction")
                return HttpResponse(str(r.status_code) + "error on transaction")
            else:
                newformobject = form.save()
                return HttpResponse("card imported successfully")
    else:
        form = CardForm()
    return render(request, 'form.html',{'form':form})


def submit_appraisal_application(request):
    if(request.user.user_type == 1):
        if request.method == 'POST':
            return HttpResponse("Hello, world. You're at the polls index.")
        else:
            form = Ratee_submit_appraisal_application()
            return render(request,'form.html',{'form':form})
    else:
        return HttpResponse("Sorry you are not Ratee")

def get_approved_application(self):
    return HttpResponse("Hello, world. You're at the polls index.") 

def add_leave_record(request):
    if(request.user.user_type == 7):
        if request.method == 'POST':
            # print(request.POST.get("Leave_id"))
            leaverecord = LeaveRecord(request.POST)
            newleaverecordobject = leaverecord.save() 
            payload = {
                "$class": "org.army.LeaveRecord",
                "leaveId": str(newleaverecordobject.id),
                "from": "2019-04-15T18:11:08.865Z",
                "to": "2019-04-15T18:11:08.865Z",
                "officer": "resource:org.army.Officer#" + str(newleaverecordobject.OfficerID)
                }
            url = 'http://172.27.20.177:3000/api/org.army.LeaveRecord'
            headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            if r.status_code != 200:
                print(r.content, "error on transaction")
                return HttpResponse(str(r.status_code) + "error on transaction")
            else:
                return HttpResponse("Leave recorded successfully")
        else:
            form = LeaveRecord()
            return render(request,'form.html',{'form':form})
    else:
        return HttpResponse("Sorry you are not Clerk")

def mark_attendance(request):
    if(request.user.user_type == 7):
        if request.method == 'POST':
            payload = {
                "$class": "org.army.MarkAttendance",
                "attendance": {} ,
                "officer": "resource:org.army.Officer#" + request.POST.get("OfficerID"),
                "transactionId": "",
                "timestamp": ""
                }
            url = 'http://172.27.20.177:3000/api/org.army.MarkAttendance'
            headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            if r.status_code != 200:
                print(r.content, "error on transaction")
                return HttpResponse(str(r.status_code) + "error on transaction")
            else:
                return HttpResponse("Marked attendance successfully")
        else:
            form = MarkAttendance()
            return render(request,'form.html',{'form':form})

    else:
        return HttpResponse("Sorry you are not Clerk")


def add_appraisal(request):
    if(request.user.user_type == 7):
        if request.method == 'POST':
            payload = {
                "$class": "org.army.Appraisal",
                "AppID": request.POST.get("AppID"),
                "description": "NONE",
                "status": "NONE",
                "RateeId": request.POST.get("RateeID"),
                "IOId": request.POST.get("IOID"),
                "ROId": request.POST.get("ROID"),
                "SROId": request.POST.get("SROID"),
                "AOId": request.POST.get("AOID"),
                "ClerkId": request.POST.get("ClerkID"),
                "officer": "resource:org.army.Officer#"+request.POST.get("RateeID")
                }
            url = 'http://172.27.20.177:3000/api/org.army.Appraisal'
            headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            if r.status_code != 200:
                print(r.content, "error on transaction")
                return HttpResponse(str(r.status_code) + "error on transaction")
            else:
                return HttpResponse("Created Appraisal successfully")
        else:
            form = Appraisal()
            return render(request,'form.html',{'form':form})
    else:
        return HttpResponse("Sorry you are not Clerk")


def ratee_home():
    template = loader.get_template("ratee.html")
    return HttpResponse(template.render())
    # return HttpResponse("Hello, world. You're at the polls index.")

def IO_home():
    return HttpResponse("Hello, world. You're at the polls index.")

def RO_home():
    return HttpResponse("Hello, world. You're at the polls index.")

def SRO_home():
    return HttpResponse("Hello, world. You're at the polls index.")

def AO_home():
    return HttpResponse("Hello, world. You're at the polls index.")

def Admin_home():
    return HttpResponse("Hello, world. You're at the polls index.")

def Clerk_home():
    template = loader.get_template("clerk.html")
    return HttpResponse(template.render())
    # return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    # if request.user.is_authenticated():
    if (request.user.user_type == 1):
        return ratee_home()
        ##TODO redirect
    elif (request.user.user_type == 2):
        return IO_home()
        ##TODO redirect
    elif (request.user.user_type == 3):
        return RO_home()
        ##TODO redirect
    elif (request.user.user_type == 4):
        return SRO_home()
        ##TODO redirect
    elif (request.user.user_type == 5):
        return AO_home()
        ##TODO redirect
    elif (request.user.user_type == 6):
        return Admin_home()
        ##TODO redirect
    elif (request.user.user_type == 7):
        return Clerk_home()
        ##TODO redirect
    else:
        return HttpResponse(("Invalid user type " + request.user.user_type))
    # else:
    #     return HttpResponse("No user logged in")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")