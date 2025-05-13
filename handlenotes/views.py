from django.shortcuts import render, redirect
from django.http import response
from .models import HandleNotes
from .forms import HandleNotesForm, StockForm
import requests
import datetime
import random
from .models import NewsArticle
from django.utils import timezone
from .models import News, Ticker

# Create your views here.


def index(request):
    if request.method =="POST":
        form = HandleNotesForm(request.POST) 
        form.save()
        
        
    form = HandleNotesForm()  
    existing_notes= HandleNotes.objects.all()             # Erstellt das Formular
    return render(request, "index.html", {"form": form, "existing_notes": existing_notes})    # Übergibt das Formular an index.html

    
    
def add_note(request):
    if request.method == "POST":
        form = HandleNotesForm(request.POST)                # Erstellt das Formular mit eingegebenen Daten
        if form.is_valid():
            form.save()                                     # Speichert die Daten in der DB
            return redirect('notes_list')                   # Nach dem Speichern zur Notizen-Liste weiterleiten
    else:
        form = HandleNotesForm()                            # Neues leeres Formular laden

    existing_notes= HandleNotes.objects.all()
    return render(request, "add_note.html", {"test":"test", "form": form, "existing_notes": existing_notes})  # Formular an HTML übergeben

def get_news(requests):
    # news_data = News.objects.all()
    # context = {"news_list": news_data}    
    # list_of_news, list_of_timestamps, new_urls, new_thumbnail, snipetList = fetch_and_store_news()
    # context = {"news_list":zip(list_of_news, new_urls, new_thumbnail, snipetList)}
    
    news_data = News.objects.order_by("-timestamp").first()
    latest_timestamp = int(news_data.timestamp)/1000
    latest_timestamp_datetime = datetime.datetime.fromtimestamp(latest_timestamp)
    current_time = datetime.datetime.now()
    time_delta_in_second = current_time - latest_timestamp_datetime
    
    if time_delta_in_second.seconds > 86400:
        news_list, timestamp, newsurls, thumbnail, snippetList = fetch_and_store_news()
            
        save_news_to_db(news_list, timestamp, newsurls, thumbnail, snippetList)
    
    news_data = News.objects.all()
    context = {"news_list": news_data}
    return render(requests, "news.html", context)


def fetch_and_store_news():
    url = "https://google-news13.p.rapidapi.com/business"
    querystring = {"lr": "en-US"}
    
    
    headers = {
        "x-rapidapi-key": "76d2dd48e8msh592f8bc9b6421bdp1ff7b2jsn3e9a688ada91",
        "x-rapidapi-host": "google-news13.p.rapidapi.com"
    }
    
    '''

    headers = {
    "x-rapidapi-key": "c4e9df0a1amshd32e9943d56e520p12fd4djsncc550df2cae5",
    "x-rapidapi-host": "google-news13.p.rapidapi.com"
    }
    '''
    
    response = requests.get(url, headers=headers, params=querystring)
    
    
    
    data = response.json()
    news_list = []
    timestamps = []
    newsurls = []
    thumbnails = []
    snipetList = []
    
    
    for news_item in data['items']:
        news_list.append(news_item['title'])
        timestamps.append(news_item['timestamp'])
        newsurls.append(news_item['newsUrl'])
        snipetList.append(news_item['snippet'])
        
        if "images" in news_item:
            thumbnails.append( news_item['images']['thumbnailProxied'])
            # thumbnails.append(news_item['images']['thumbnail']) 
        else:
            thumbnails.append("https://dummyimage.com/qvga")

    return news_list, timestamps, newsurls, thumbnails, snipetList
    
    
    
def save_news_to_db(news_list, timestamps, newsurls, thumbnails, snnipetList):
    
    for nws, timestamp, nurl, thumb, snippet in zip(news_list, timestamps, newsurls, thumbnails, snnipetList):
        News.objects.create( news = nws, snippet = snippet, thumbnail =thumb,timestamp = int(timestamp), newsurl = nurl )
        
        
        
def get_stock(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('getStock')  # reload page afte saving
        
    # if Ticker.ticker.active == False:
    #     Ticker.ticker.active == True
        
        # return redirect('getStock')  # reload page afte saving

    ticker = tuple(Ticker.objects.filter(active=True).values_list('ticker', flat=True))
    domain = tuple(Ticker.objects.filter(active=True).values_list('domain', flat=True))
    # stock_price = {elem: getStockData(elem) for elem in ticker}
    # domains = {k:v for k,v in zip(ticker, domain)}
    stockprices = [getStockData(t) for t in ticker]
    res = zip(ticker, domain, stockprices)
    context = {
        'res': res,
        'form': form        
    }
    return render(request, 'stock.html', context)


def getStockData(ticker):
	return random.randint(100,400)

	url = "https://yahoo-finance127.p.rapidapi.com/finance-analytics/" + ticker

	headers = {
	"x-rapidapi-key":"76d2dd48e8msh592f8bc9b6421bdp1ff7b2jsn3e9a688ada91",
	"x-rapidapi-host": "yahoo-finance166.p.rapidapi.com",

		"x-rapidapi-host": "yahoo-finance127.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)
	data = response.json()
	return data["currentPrice"]["raw"]


def remove_stock(request, ticker_name):
    Ticker.objects.filter(ticker=ticker_name).update(active=False)
    return redirect('getStock')