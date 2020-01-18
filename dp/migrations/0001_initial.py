# Generated by Django 3.0.2 on 2020-01-18 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(db_index=True, max_length=64, verbose_name='event_id')),
                ('eventArticle', models.CharField(max_length=64, verbose_name='event_article')),
                ('eventLocation', models.CharField(max_length=64, verbose_name='event_location')),
                ('eventCategory', models.IntegerField(choices=[(1, 'Концерт'), (2, 'Спорт'), (3, 'Кино'), (4, 'Выставка'), (5, 'Движ')], verbose_name='category_id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='tags')),
            ],
        ),
    ]