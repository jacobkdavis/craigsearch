from django.db import models


class SearchArea(models.Model):
    name = models.CharField(max_length=50)
    #description = models.CharField(max_length=200)
    areas = models.CharField(max_length=1200, default='')
    
    def __str__(self):
        return self.name


class SearchQuery(models.Model):
    area = models.ForeignKey(SearchArea, on_delete=models.SET_NULL, null=True)
    #region = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200)
    querystring = models.CharField(max_length=200)
    #description = models.CharField(max_length=200)
    
    def __str__(self):
        #return self.region + ":" + self.category + ":" + self.querystring
        return self.area.name + " : " + self.category + " : " + self.querystring

    
    #s = SearchQuery(region="williamsport", category="sss", querystring="letterpress")
    
class SearchResult(models.Model):
    #searchquery = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
