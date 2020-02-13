import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Department
from hrapp.models import model_factory
from ..connection import Connection


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.first_name,
            e.last_name,
            d.department_name
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id
        WHERE e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()

@login_required
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/employee_detail.html'
        context = {
            'employee': employee
        }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting an employee
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_employee
                WHERE id = ?
                """, (employee_id,))

            return redirect(reverse('hrapp:employees'))