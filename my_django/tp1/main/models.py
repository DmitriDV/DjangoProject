from django.db import models

class Task(models.Model):
    title = models.CharField('Titre', max_length=200)
    task = models.TextField('Description')

    class Meta:
        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'

def __str__(self):
    return self.title

    