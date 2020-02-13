# auth: Caroline Brownlee
# this module handles listing all computers

import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Computer
from ..connection import Connection
from hrapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            
            conn.row_factory =  model_factory(Computer)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                c.id,
                c.make
            FROM hrapp_computer c
            """)

            # When you instruct the sqlite3 package to fetchall(), it takes your SQL string and walks over to the database and executes it. It then takes all of the rows that the database generates, and creates a tuple out of each one. It then puts all of those tuples into a list. (Chapter Documentation, NSS)

            # TUPLE is a collection which is ordered and unchangeable. Allows duplicate members. Parenthesis. (W3 Schools)

            # LIST is a collection which is ordered and changeable. Allows duplicate members. Brackets. (W3 Schools)

            all_computers = db_cursor.fetchall()

        # When a view wants to generate some HTML representations of data, it needs to specify a template to use. [Below], the template variable is holding the path and filename of the template. (Nashville Software School, Ch 3 Documentation)

        template = 'computers/computers_list.html'

        # the dictionary 'all_books' has a single property labeled all_books and its value is the list of book objects that the view generates. // The key name is able to be used in a loop in the template.  (Nashville Software School, Ch 3 Documentation)

        context = {
            'all_computers': all_computers
        }
        # Then the render() method is invoked. That method takes the HTTP request as the first argument, the template to be used as the second argument, and then a dictionary containing the data to be used in the template. (Nashville Software School, Ch 3 Documentation)
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_computer
            (
                make, purchase_date, decommission_date
            )
            VALUES (?, ?, ?)
            """, 
            (form_data['make'], form_data['purchase_date'],
            form_data['decommission_date']))

        return redirect(reverse('hrapp:computers'))
