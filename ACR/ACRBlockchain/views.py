from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserCreationForm, Ratee_submit_appraisal_application
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.template import Context, loader 

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def submit_appraisal_application(request):
    if request.method == 'POST':
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        form = Ratee_submit_appraisal_application()
        return render(request,'form.html',{'form':form})

def get_approved_application(self):
    return HttpResponse("Hello, world. You're at the polls index.") 

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
    return HttpResponse("Hello, world. You're at the polls index.")

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