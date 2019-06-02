from django.db import models

# Create your models here.
class Issues(models.Model):
    status_choices = (
        ('Backlog', 'Backlog'),
        ('To-do', 'To-do'),
        ('Doing', 'Doing'),
        ('Completed', 'Completed'),
        ('QA', 'QA'),
        ('Closed', 'Closed'))
    priority_choices = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'))


    desc = models.TextField()
    status = models.CharField(max_length=10, choices=status_choices)
    priority = models.CharField(max_length=10, choices=priority_choices)
    
    def __str__(self):
        return "{} : {} : {}".format(self.desc, self.status, self.priority)
        