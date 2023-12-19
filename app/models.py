from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    def __int__(self):
        return self.dept_no
    def __str__(self):
        return self.dept_name
    


class Emp(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    dept_no=models.ForeignKey(Dept, on_delete=models.CASCADE)
    sal=models.IntegerField()
    job=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default='employe@gmail.com')

    def __int__(self):
        return self.emp_no
    def __str__(self):
        return self.ename
    def __str__(self):
        return self.sal
    def __str__(self):
        return self.job
    def __int__(self):
        return self.dept_no
    







