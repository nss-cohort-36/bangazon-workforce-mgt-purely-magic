import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department, Employee
from hrapp.models import model_factory
from ..connection import Connection

def employee_department_list(department_id):
    with sqlite3.connect(Connection.db_path) as conn:

        conn.row_factory = model_factory(Employee)

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            d.id department_Id,
            d.department_name,
            d.budget,
            e.first_name,
            e.last_name,
            e.start_date,
            e.department_id
        FROM hrapp_department d 
        JOIN hrapp_employee e ON d.id = e.department_id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchall()
        


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id department_Id,
            d.department_name,
            d.budget,
            e.first_name,
            e.last_name,
            e.start_date,
            e.department_id
        FROM hrapp_department d 
        JOIN hrapp_employee e ON d.id = e.department_id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()

@login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)
        department_employees = employee_department_list(department_id)

        template = 'departments/detail.html'
        context = {
            'department': department,
            'department_employees': department_employees
        }

        return render(request, template, context)

# orig work

# import sqlite3
# from django.urls import reverse
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from hrapp.models import Department, Employee
# from hrapp.models import model_factory
# from ..connection import Connection

# def create_single_department(cursor, row):
#     _row = sqlite3.Row(cursor, row)

#     department = Department()
#     department.id = _row["department_id"]
#     department.name = _row["department_name"]
#     department.budget = _row["budget"]

#     department.employees = []

#     employee = Employee()
#     employee.id = _row["employee_id"]
#     employee.first_name = _row["first_name"]
#     employee.last_name = _row["last_name"]
#     employee.start_date = _row["start_date"]
#     employee.last_name = _row["last_name"]
#     employee.department_id = _row["department_id"]
#     employee.employee_id = _row["employee_id"]

#     return (department, employee)



# def get_department(department_id):
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = create_single_department
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         SELECT
#             d.id department_Id,
#             d.department_name,
#             d.budget,
#             e.first_name,
#             e.last_name,
#             e.start_date,
#             e.id employee_id,
#             e.department_id
#         FROM hrapp_department d 
#         JOIN hrapp_employee e ON d.id = e.department_id
#         WHERE d.id = ?
#         """, (department_id,))

#         return db_cursor.fetchone()

# @login_required
# def department_details(request, department_id):
#     if request.method == 'GET':
#         department = get_department(department_id)

#         this_department_groups = {}

#         for employee in department[0].employees:
#             this_department_groups[department_id].employees.append(employee)

#         template = 'departments/detail.html'
#         context = {
#             'department': this_department_groups.values()
#         }

#         return render(request, template, context)