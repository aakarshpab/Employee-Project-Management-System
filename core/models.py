from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=55)
    designation = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=15,decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
       return (self.name)



class Project(models.Model):
    Status_Choices=[
        ('Not started','Not Started'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),]

    project_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date =  models.DateField()
    end_date   = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100,choices=Status_Choices,default='Not started')
    project_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_projects'
     )
    employees = models.ManyToManyField(
        Employee,
        related_name='projects',
        blank=True
    )

    def __str__(self):
       return(self.project_name)