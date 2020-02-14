import sqlite3
# from django.urls import reverse
from django.shortcuts import render, redirect, reverse
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

    # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_computer
                WHERE id = ?
                """, (computer_id,))

            return redirect(reverse('hrapp:computers'))