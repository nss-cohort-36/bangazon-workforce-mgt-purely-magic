import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Department
from hrapp.models import model_factory
from ..connection import Connection


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Book)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            au.id,
            au.first_name,
            au.last_name,
            d.department_name
            
        FROM hrapp_employee e
        JOIN auth_user au ON e.user_id = au.id
        JOIN hrapp_department d ON e.department_id = d.id
        WHERE l.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()

@login_required
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/employee_details.html'
        context = {
            'employee': employee
        }

        return render(request, template, context)