from django.db import models
import requests
import json
HOST = "http://localhost/ecommerce/public/api/content"
# Create your models here.
class Item(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    @classmethod
    def getFromApi(cls):
        data = requests.get(HOST)
        return data.json()
        
    @classmethod
    def createFromJson(cls, data):
        list_data = [cls(id=i['id'],name=i['name'],description=i['description']) for i in data]
        return list_data
        
    