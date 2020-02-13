import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
from hrapp.models import model_factory
from ..connection import Connection


@login_required
def employee_form(request):
    if request.method == 'GET':
        departments = get_departments()
        template = 'employees/forms.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)