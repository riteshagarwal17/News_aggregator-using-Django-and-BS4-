import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
requests.packages.urllib3.disable_warnings()

def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('article', {"class": "sc-1pw4fyi-5 RkwFH"})
    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        title = artcile.find('h4', {"class": "sc-1qoge05-0 eoIfRA"}).text
        News3 = artcile.find('img', {"class": "dv4r5q-2 iaqrWM"})
        if News3 is None:
            image_src = temp
        else:
            image_src = News3['srcset'].split(' ')[0]
            temp = image_src
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()

    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,

    }
    return render(request, "news/home.html", context)

