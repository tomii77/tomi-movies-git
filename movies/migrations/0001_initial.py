# Generated by Django 4.1.2 on 2022-11-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('my_movie_time', models.CharField(max_length=1000)),
                ('my_movie_genree', models.CharField(max_length=100)),
                ('my_original_title', models.CharField(max_length=100)),
                ('my_article_duration', models.CharField(max_length=20)),
                ('my_article_plot_main', models.CharField(max_length=1000)),
                ('my_article_plot_2', models.CharField(max_length=1000)),
                ('my_article_plot_3', models.CharField(max_length=1000)),
                ('my_article_director', models.CharField(max_length=100)),
                ('my_article_cast', models.CharField(max_length=1000)),
                ('my_imdb_rate', models.CharField(max_length=5)),
                ('my_channel_link', models.CharField(max_length=30)),
                ('my_date', models.DateField(max_length=30)),
            ],
        ),
    ]
