import sqlite3
from hrapp.views import Connection
from hrapp.models import TrainingProgram
from django.shortcuts import render, reverse, redirect


def training_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                tp.id,
                tp.name,
                tp.description,
                tp.start_date,
                tp.end_date,
                tp.capacity
            from hrapp_trainingprogram tp
            """)

            all_training_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                trainingprogram = TrainingProgram()
                trainingprogram.id = row['id']
                trainingprogram.title = row['name']
                trainingprogram.description = row['description']
                trainingprogram.start_date = row['start_date']
                trainingprogram.end_date = row['end_date']
                trainingprogram.capacity = row['capacity']

                all_training_programs.append(trainingprogram)

        template = 'training_program/training_program_list.html'  #folder/file nameee
        context = {
            'all_training_programs': all_training_programs
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (
            name, description, start_date, end_date, capacity 
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['description'], form_data['start_date'],
            form_data['end_date'], form_data['capacity']))

    return redirect(reverse('hrapp:training_program'))
