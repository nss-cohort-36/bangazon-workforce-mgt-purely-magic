import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Department, Employee
from ..connection import Connection
from hrapp.models import model_factory

def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["department_id"]
    department.name = _row["department_name"]
    department.budget = _row["budget"]

    department.employees = []

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    employee.last_name = _row["last_name"]
    employee.department_id = _row["department_id"]
    employee.employee_id = _row["employee_id"]

    return (department, employee)


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_department
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                d.id department_id,
                d.department_name,
                d.budget,
                e.first_name,
                e.last_name,
                e.start_date,
                e.department_id,
                e.id employee_id
            FROM hrapp_department d 
            JOIN hrapp_employee e ON d.id = e.department_id;
            """)

            all_departments = db_cursor.fetchall()

            department_groups = {}

            for (department, employee) in all_departments:

                if department.id not in department_groups:
                    department_groups[department.id] = department
                    department_groups[department.id].employees.append(employee)

                else:
                    department_groups[department.id].employees.append(employee) 

        template = 'departments/list.html'
        context = {
            'all_departments': department_groups.values()
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_department
            (
                department_name, budget
            )
            VALUES (?, ?)
            """,
            (form_data['department_name'], form_data['budget']))

        return redirect(reverse('hrapp:departments'))