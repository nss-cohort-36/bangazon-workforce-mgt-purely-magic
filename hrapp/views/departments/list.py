import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection
from hrapp.models import model_factory


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Department)
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

            all_departments = db_cursor.fetchall()

        template = 'departments/list.html'
        context = {
            'all_departments': all_departments
        }

        return render(request, template, context)