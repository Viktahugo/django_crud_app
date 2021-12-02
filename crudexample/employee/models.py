from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=20)
    eemail = models.EmailField()
    eecontact = models.CharField(max_length=10)
    class Meta:
        db_table = "employee"