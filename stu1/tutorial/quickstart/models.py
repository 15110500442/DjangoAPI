from django.db import models

# Create your models here.
class Students(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    birthday = models.DateField()
    id_type = models.CharField(max_length=10)
    id_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    native_place = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    enrollment_time = models.DateField()
    hobby = models.TextField()
    abbr_name = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'student'