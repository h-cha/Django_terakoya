from django.db import models

# Create your models here.

class Input(models.Model):
    q_num = models.IntegerField()
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    a4 = models.IntegerField()
    a5 = models.IntegerField()
    
    def __str__(self):
        return '<問題番号：' + str(self.q_num) + ' ,(1):' + str(self.a1) + ' , (2):' + str(self.a2) + ' , (3):' + \
    str(self.a3) + ' , (4):' + str(self.a4) + ' , (5):' + str(self.a5) + '>'

class Question(models.Model):
    q_num = models.IntegerField()
    q1 = models.CharField(max_length=300)
    q2 = models.CharField(max_length=300)
    q3 = models.CharField(max_length=300)
    q4 = models.CharField(max_length=300)
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    a4 = models.IntegerField()
    a5 = models.IntegerField()
    
    def __str__(self):
        return '<問題番号：' + str(self.q_num) + ' ,(1):' + str(self.a1) + ' , (2):' + str(self.a2) + ' , (3):' + \
    str(self.a3) + ' , (4):' + str(self.a4) + ' , (5):' + str(self.a5) + '>'  