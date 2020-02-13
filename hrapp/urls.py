from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employee/', employee_list, name='employee'),
    path('departments/', department_list, name='departments'),
    path('computers/', computer_list, name='computers'),
]
