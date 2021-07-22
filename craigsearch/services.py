from .models import SearchQuery, SearchResult

import requests
from bs4 import BeautifulSoup

def get_region_searchresults(searchquery):
    results = {}
    
    for a in searchquery.area.areas.split(","):
        
        url = "https://" + a + ".craigslist.org/search/" + searchquery.category + "?query=" + searchquery.querystring
        
        tempres = get_searchresults(url)
        
        results.update(tempres)
        
    return results
    
    

def get_searchresults(url):
    # service to return retrieve and return list of search result objects
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    results = {}

    for row in soup.find_all('li', class_='result-row'):

        price = row.a.get_text() 
        
        # get id (for img url) from field ex: #3:00T0T_6lP1KtM7gcrz_0j80t2
        
        imgid = ""
        imgurl = ""
        
        if row.a.get("data-ids"):
            # get first if there are multiple images
            imgid = row.a.get("data-ids").split(",",1)[0]
            
            # strip extra data
            imgid = imgid.split(":",1)[1]
            
            # build thumbnail string
            imgurl = "https://images.craigslist.org/"+imgid+"_300x300.jpg"
        
        url = row.h3.a.get("href")
        dataid = row.h3.a.get("data-id")
        title = row.h3.a.get_text()
        
        r = SearchResult()

        r.title = title
        r.url = url
        r.price = price
        r.image = imgurl

        print(r)
        
        results[url] = r
        
    return results
        
