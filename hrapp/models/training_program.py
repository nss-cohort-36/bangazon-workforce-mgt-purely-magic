from django.db import models

class TrainingProgram(models.Model):

    title = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    trainingProgramId = models.ManyToManyField("Employee", through='TrainingProgramEmployee')

    class Meta:
        verbose_name = ("TrainingProgram")
        verbose_name_plural = ("TrainingPrograms")

    def get_absolute_url(self):
        return reverse("TrainingProgram_detail", kwargs={"pk": self.pk})