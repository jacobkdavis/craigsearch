from django.db import models


class SearchArea(models.Model):
    name = models.CharField(max_length=50)
    areas = models.CharField(max_length=1200, default='')
    
    def __str__(self):
        return self.name


class SearchQuery(models.Model):
    area = models.ForeignKey(SearchArea, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=200)
    querystring = models.CharField(max_length=200)
    
    def __str__(self):
        return self.area.name + " : " + self.category + " : " + self.querystring
    
class SearchResult(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
