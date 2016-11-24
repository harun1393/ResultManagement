from __future__ import unicode_literals

from django.db import models



class StudentsInfo(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    batch = models.IntegerField()
    department = models.CharField(max_length=5)
    section = models.CharField(max_length=5)

    class Meta:
        db_table = 'students_info'

    def __str__(self):
        return str(self.student_id)


