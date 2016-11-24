from __future__ import unicode_literals
from django.db import models
from subjects.models import SubjectsInfo
from students.models import StudentsInfo




class ResultsInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    subject_id = models.ForeignKey(SubjectsInfo, db_column='subject_id')
    student_id = models.ForeignKey(StudentsInfo, db_column='student_id')
    department = models.CharField(max_length=10)
    semester = models.IntegerField()
    mid_number = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    final_number = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)

    class Meta:
        db_table = 'results_info'

    def __str__(self):
        return str(self.student_id)




