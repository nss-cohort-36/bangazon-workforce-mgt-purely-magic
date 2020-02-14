import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import model_factory
from ..connection import Connection

@login_required
def department_form(request):
    if request.method == 'GET':
        template = 'departments/form.html'

        return render(request, template)