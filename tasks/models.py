from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=64, blank=False, null=False, default=None)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.task_name}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'