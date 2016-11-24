from __future__ import unicode_literals
import hashlib
from django.db import models
from django.utils.translation import ugettext_lazy as _
from subjects.models import SubjectsInfo


class TeachersInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher_code = models.CharField(max_length=15)
    teacher_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    REQUIRED_FIELDS = ('password',)
    USERNAME_FIELD = ('email')

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def get_password(self, base_password):
        hash_password = hashlib.md5(base_password).hexdigest()
        return hash_password

    def is_stuff(self):
        return True

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = 'teachers_info'


class ClassManagement(models.Model):
    semester = models.IntegerField()
    batch = models.IntegerField()
    section = models.CharField(max_length=5)
    subject = models.ForeignKey(SubjectsInfo,db_column='subject')
    teacher = models.ForeignKey(TeachersInfo,db_column='teacher')

    class Meta:
        db_table = 'class_management'
