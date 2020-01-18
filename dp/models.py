from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Events(models.Model):
    event_id = models.CharField(verbose_name='event_id', db_index=True, unique=True, max_length=64)
    eventArticle = models.CharField(verbose_name='event_article', max_length=64)
    eventLocation = models.CharField(verbose_name='event_location', max_length=64)
    EVENT_CATEGORIES = (
        (1, 'Концерт'),
        (2, 'Спорт'),
        (3, 'Кино'),
        (4, 'Выставка'),
        (5, 'Движ'),
    )
    eventCategory = models.IntegerField(verbose_name='category_id', choices=EVENT_CATEGORIES)
    user = models.ForeignKey(User, verbose_name='tags', on_delete=models.CASCADE)



