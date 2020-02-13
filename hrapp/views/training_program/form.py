import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import TrainingProgram
from ..connection import Connection

@login_required
def training_program_form(request):
    if request.method == 'GET':
        template = 'training_program/form.html'
        
        return render(request, template)

    

