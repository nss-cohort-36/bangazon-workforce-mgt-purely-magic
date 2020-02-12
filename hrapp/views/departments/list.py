import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                d.id department_id,
                d.department_name,
                d.budget,
                e.first_name,
                e.last_name,
                e.start_date,
                e.department_id
            FROM hrapp_department d 
            JOIN hrapp_employee e ON d.id = e.department_id;
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.id = row['department_id']
                department.department_name = row['department_name']
                department.budget = row['budget']
                department.first_name = row['first_name']
                department.last_name = row['last_name']
                department.start_date = row['start_date']
                department.department_id = row['department_id']

                all_departments.append(department)

        template = 'departments/list.html'
        context = {
            'all_departments': all_departments
        }

        return render(request, template, context)