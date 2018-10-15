from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=16)


class Students(models.Model):
    student_school_name = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    student_name = models.CharField(max_length=10)
    friend_name_list = models.ManyToManyField("self")