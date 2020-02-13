from django.urls import path, include
from .views import *


app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employees'),
    path('training_programs/', training_program_list, name='training_program'),
    path('departments/', department_list, name='departments'),
    path('computers/', computer_list, name='computers'),
    path('computers/form', computer_form, name='computer_form'),
    path('employees/form', employee_form, name='employee_form'),
    path('training_program/form', training_program_form, name='training_program_form'),
    path('employees/<int:employee_id>/', employee_details, name='employee_detail'),
    
    path('computers/<int:computer_id>/', computer_details, name='computer_details'),
]
#url, method, name