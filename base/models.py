from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created = models.DateField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering=['complete']
