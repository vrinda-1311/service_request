from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class JobModel(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=[
            ('IT', 'IT'),
            ('HR', 'HR'),
            ('FINANCE', 'FINANCE'),
            ('ADMIN', 'ADMIN'),
        ]
    )

    priority = models.CharField(max_length=50,choices=[
                        ('LOW','LOW'),
                        ('MEDIUM','MEDIUM'),
                        ('HIGH','HIGH')
    ])

    status = models.CharField(max_length=50,
                              choices=[
                                  ('OPEN','OPEN'),
                                  ('IN_PROGRESS','IN_PROGRESS'),
                                  ('RESOLVED','RESOLVED')
                              ])
    
    created_at = models.DateField(auto_now_add=True)