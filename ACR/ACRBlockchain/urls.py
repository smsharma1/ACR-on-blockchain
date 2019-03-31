from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    path('submit_appraisal_application',views.submit_appraisal_application,name='submit_appraisal_application'),
    path('get_approved_application',views.get_approved_application,name='get_approved_application'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
]