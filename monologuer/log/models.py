from django.db import models

NAME_LENGTH = 80

class Log(models.Model):
    owner = models.CharField(max_length=NAME_LENGTH)


class LogEntry(models.Model):
    # maybe have owner be id number
    models.ManyToOneRel(Log, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField()