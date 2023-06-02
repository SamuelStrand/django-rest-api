from django.db import models


# Create your models here.

class Posts(models.Model):
    user_id = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):  # TODO <objec}t 1>
        return f'{self.user_id}  {"Выполнено" if self.completed else "Не выполнено"} {self.title[0:50:1]}'
