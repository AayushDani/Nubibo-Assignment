from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.TextField()
    description = models.TextField()

    priority_options = (
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),   
    )
    priority = models.CharField(max_length=6, choices=priority_options, default='LOW')

    status_options = (
        ('PENDING', 'PENDING'),
        ('ON_PROGRESS', 'ON_PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
        ('SUSPENDED', 'SUSPENDED'),
    )
    status = models.CharField(max_length=11, choices=status_options, default='PENDING')
    date_added = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tasks"


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    event_types = (
        ('Creation', 'Creation'),
        ('Updation', 'Updation'),
        ('Deletion', 'Deletion')
    )
    event_type = models.TextField(choices=event_types)
    time_of_event = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task.name + "-> " + self.event_type

    class Meta:
        verbose_name_plural = "Events"
