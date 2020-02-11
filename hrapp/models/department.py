from django.db import models

class Department(models.Model):

    department_name = models.CharField(max_length=50)
    budget = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("department")
        verbose_name_plural = ("departments")

    def __str__(self):
        return self.department_name
