from django.db import models

class Department(models.Model):
    '''
    description: This class creates a department and its properties
    author: John Long
    properties:
      department_name: This property will contain the name of the department an employee will work in.
      budget: This property contains the budget for the department in integer form so as to be usable for future math methods as needed.
    '''

    department_name = models.CharField(max_length=50)
    budget = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("department")
        verbose_name_plural = ("departments")

    def __str__(self):
        return self.department_name
