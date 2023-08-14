from django.db import models

class EmpDetails(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=15)
    exp = models.IntegerField()


class Salaryinfo(models.Model):
    eid = models.IntegerField()
    basic = models.IntegerField()
    lop = models.IntegerField()
    bonus = models.IntegerField()
    
