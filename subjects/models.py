from __future__ import unicode_literals

from django.db import models

class SubjectsInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    subject_code = models.CharField(max_length=5)
    subject_name = models.CharField(max_length=15)
    #department = models.CharField(max_length=15)
    semester = models.IntegerField()
    credit = models.IntegerField()

    def __str__(self):
        return self.subject_code
    class Meta:
        db_table = 'subjects_info'