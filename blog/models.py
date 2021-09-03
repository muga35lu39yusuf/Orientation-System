from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User,null=True,blank =True, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    
    class Meta:
       ordering = ['id']

