from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import SearchQuery
from .services import get_region_searchresults


# for scraping
import requests
from bs4 import BeautifulSoup



def index(request):
    searchquery_list = SearchQuery.objects.order_by('category','querystring')
    context = {'searchquery_list': searchquery_list}
    return render(request, 'craigsearch/index.html', context)

def searchresults(request, searchquery_id):
    searchquery = get_object_or_404(SearchQuery, pk=searchquery_id)
    
    results = get_region_searchresults(searchquery)

    context = {'searchquery': searchquery, 'searchresult_list': results.values()}
    return render(request, 'craigsearch/results.html', context)
