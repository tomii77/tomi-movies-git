from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    my_movie_time = models.CharField(max_length=1000)
    my_movie_genree = models.CharField(max_length=100)
    my_original_title = models.CharField(max_length=100)

    my_article_duration = models.CharField(max_length=20)
    my_article_plot_main = models.CharField(max_length=1000)
    my_article_plot_2 = models.CharField(max_length=1000)
    my_article_plot_3 = models.CharField(max_length=1000)
    my_article_director = models.CharField(max_length=100)
    my_article_cast = models.CharField(max_length=1000)
    my_imdb_rate = models.CharField(max_length=5)
    
    my_channel_link = models.CharField(max_length=30)
    my_date = models.DateField(max_length=30)





    def __str__(self):
        return self.title