import sqlite3
# from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Computer
from hrapp.models import model_factory
from ..connection import Connection

def create_computer(cursor, row):
    _row = sqlite3.Row(cursor, row)

    computer = Computer()
    computer.id = _row["computer_id"]
    computer.make = _row["make"]
    computer.purchase_date = _row["purchase_date"]
    computer.decommission_date = _row["decommission_date"]

    return computer


# ...the computer_id variable that you [specify] in the URLs pattern above gets automatically sent as an argument to the book_details view. (Nashville Software School, Chapter Documentation)
def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_computer
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            c.id computer_id,
            c.make,
            c.purchase_date,
            c.decommission_date
        FROM hrapp_computer c
        WHERE c.id = ?
        """, (computer_id,))

        return db_cursor.fetchone()

@login_required
def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)
        template = 'computers/computers_detail.html'
        context = {
            'computer': computer
        }
        
        return render(request, template, context)