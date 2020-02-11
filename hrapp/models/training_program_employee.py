from django.db import models

class TrainingProgramEmployee(models.Model):
    """
    Creates the join table for the many to many relationship between training programs and employees
    Author: Caroline Brownlee and Charles Jackson
    methods: none
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training_program = models.ForeignKey("Training Program", on_delete=models.CASCADE)