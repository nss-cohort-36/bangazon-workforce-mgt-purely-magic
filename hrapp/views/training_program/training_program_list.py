import sqlite3
from hrapp.views import Connection
from hrapp.models import TrainingProgram
from django.shortcuts import render


def training_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                tp.id,
                tp.title,
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
                trainingprogram.title = row['title']
                trainingprogram.start_date = row['start_date']
                trainingprogram.end_date = row['end_date']
                trainingprogram.capacity = row['capacity']

                all_training_programs.append(trainingprogram)

        template = 'training_program/training_program_list.html'  #folder/file name
        context = {
            'all_training_programs': all_training_programs
        }

    return render(request, template, context)
