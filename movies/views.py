from django.shortcuts import render, redirect
from .models import Movie
from datetime import date
from urllib.request import urlopen
import urllib.request as urlrq
import certifi
from bs4 import BeautifulSoup
from django.http import HttpResponse

# Create your views here.



def simple_function(request):
    deleteDB()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def todays_movies(request):
    siol()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def index(request):
    movie = Movie.objects.all().order_by("-my_movie_genree","my_imdb_rate")
    print("-----")
    # muvi()
    if request.method == "POST":
        new_movie = Movie(
            title = request.POST["title"]
        )
        new_movie.save()
        return redirect("/")

    return render(request, "indexx.html", {"movies": movie})

def delete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect("/")


# def muvi():
#     today = date.today()
#     today = today.strftime("%Y%m%d")
#     print(today)

def siol():
    today = date.today()
    my_today_date_YYYYmmdd = today.strftime("%Y%m%d")
    url = "https://tv-spored.siol.net/kategorija/film/datum/" + my_today_date_YYYYmmdd

    html = urlrq.urlopen(url, cafile=certifi.where()) 
    bs = BeautifulSoup(html.read(),'html.parser')

    my_mains = bs.findAll("main", {"class": "table-list"})
    # print(my_mains)
    for my_main in my_mains:
        my_channel_link = my_main.select_one("div.table-list-header a div.col-11 h2").get_text(strip=True)
        my_movies = my_main.find("div", {"class" : "table-list-rows"}).findAll("a", {"class": "row"})

        my_list_channels_lower = ['cinemax','cinemax 2','cinestar tv 1','fox','fox crime','fox movies','hbo','hbo 2','hbo 3','hrt 1','hrt 2','hrt 3','kanal a','kino','pop tv','planet','planet 2','rtl 2 hrvaška','rtl hrvaška','rtl ii','tv 1000','tv slo 1','tv slo 2','tv slo 3','tv3']
        
        if my_channel_link.lower() in my_list_channels_lower:
            print(my_channel_link)
            for my_movie in my_movies:

                my_movie_url = "https://tv-spored.siol.net" + my_movie["href"]
                print(my_movie_url)
                my_html_articles = urlrq.urlopen(my_movie_url, cafile=certifi.where())
                bs2 = BeautifulSoup(my_html_articles.read(), "html.parser")

                #MOVIE NAME
                try:
                    my_movie_name = my_movie.find("div", {"class": "col-9"}).get_text()
                except:
                    my_movie_name = ""
                #MOVIE TIME
                try:
                    my_movie_time = my_movie.find("div", {"class": "col-1"}).get_text()
                except:
                    my_movie_time = ""
                #MOVIE GENREE
                try:
                    my_movie_genree = my_movie.find("div", {"class": "col-2 right"}).get_text()
                except:
                    my_movie_genree = ""

                #BS2
                #movie ORIGINAL NAME
                try:    
                    my_original_title = bs2.select_one("span.original-title").get_text()
                except: 
                    my_original_title = ""


                #movie DURATION
                try:
                    my_article_duration = bs2.select_one("article p.event-meta span:nth-of-type(2)").get_text(strip=True)
                except:
                    my_article_duration = ""
                #movie PLOT
                try:
                    my_article_plot_main = bs2.select_one("article p:nth-of-type(2)").get_text().strip().replace("/n","").replace("/t","")
                    my_article_plot_2 = bs2.select_one("article p.content:nth-of-type(4)").get_text().strip().replace("\r\n","")
                    my_article_plot_3 = bs2.select_one("article p.content:nth-of-type(5)").get_text().strip().replace("\"","-").replace("\r\n","")
                except:
                    my_article_plot = ""
                #movie DIRECTOR
                try:
                    my_article_director = bs2.select_one("article p[itemprop=director]").get_text(strip=True).replace("Režija:","")
                    # article > p:nth-child(8) > span
                except:
                    my_article_director = ""
                #movie CAST
                try:
                    #my_article_cast = bs2.select_one("article p[class=meta]").get_text(strip=True).replace("Igrajo:","").replace(",",", ")
                    my_article_cast = bs2.select_one("article p:nth-child(10)").get_text(strip=True).replace("Igrajo:","").replace(",",", ")
                    print("-------CAST: " + my_article_cast)

                except:
                    my_article_cast = ""
                #movie IMDb RATE 
                try:
                    my_imdb_rate = bs2.select_one("article p.event-meta").contents[7]#index("IMDB:")
                    my_imdb_rate_index_Imdb = bs2.select_one("article p.event-meta").contents[7].index("IMDB:")
                    my_imdb_rate_index_Pipe = bs2.select_one("article p.event-meta").contents[7].index("|")
                    my_imdb_rate = my_imdb_rate[my_imdb_rate_index_Imdb + 6 : 16 + my_imdb_rate_index_Pipe]
                    my_imdb_rate = float(my_imdb_rate.replace(",","."))
                except:
                    my_imdb_rate = 0

                if my_original_title == "":
                    my_original_title = my_movie_name

                print(my_movie_name, my_movie_time, my_movie_genree, my_original_title)

                new_movie = Movie(
                    title = my_movie_name,
                    my_movie_time = my_movie_time,
                    my_movie_genree = my_movie_genree,
                    my_original_title = my_original_title,
                    my_article_duration = my_article_duration,
                    my_article_plot_main = my_article_plot_main,
                    my_article_plot_2 = my_article_plot_2,
                    my_article_plot_3 = my_article_plot_3,
                    my_article_director = my_article_director,
                    my_article_cast = my_article_cast,
                    my_imdb_rate = my_imdb_rate,
                    my_channel_link = my_channel_link,
                    my_date = my_today_date_YYYYmmdd
                    )
                new_movie.save()


def deleteDB():
    Movie.objects.all().delete()


#deleteDB() 
#siol()