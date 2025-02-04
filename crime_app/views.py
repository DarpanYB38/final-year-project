from django.shortcuts import render
from crime_app.models import *
import requests
from django.shortcuts import render
from collections import defaultdict

def classify_crime(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()

    if 'theft' in title or 'theft' in description:
        return 'Theft'
    elif 'cybercrime' in title or 'cybercrime' in description:
        return 'Cybercrime'
    elif 'assault' in title or 'assault' in description:
        return 'Assault'
    else:
        return 'Other'

def fetch_news(request):
    api_key = '385ec94fea4aee86045e6662bed08bd4'
    keywords = 'crime OR theft OR murder OR robbery OR cybercrime OR assault OR fraud OR kidnapping'
    url = f'https://gnews.io/api/v4/search?q={keywords}&lang=en&country=in&max=100&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    # Debug: Print the API response
    print("API Response:", data)

    articles = data.get('articles', [])

    # Classify and count crime types
    crime_counts = defaultdict(int)
    crime_articles = []
    for article in articles:
        crime_type = classify_crime(article)
        if crime_type != 'Other':
            article['crime_type'] = crime_type
            crime_articles.append(article)
            crime_counts[crime_type] += 1

    # Debug: Print the crime_counts dictionary
    print("Crime Counts:", crime_counts)
    print("Number of filtered crime articles:", len(crime_articles))

    return render(request, 'fetch_news.html', {
        'articles': crime_articles,
        'crime_counts': crime_counts
    })

def crime_list(request):
    crimes = Crime.objects.all()
    return render(request, 'crime_list.html', {'crimes': crimes})