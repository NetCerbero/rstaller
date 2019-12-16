#from django.shortcuts import render

# Create your views here.
import operator
from decimal import Decimal
from math import sqrt

import numpy as np
from django.db.models import Avg, Count
from django.http import JsonResponse

from analitica.models import Rating
from colector.models import Colector
from recomendacion.models import SeededRecs
from recs.popularity_recommender import PopularityBasedRecs
from item.models import Item


def get_association_rules_for(request, content_id, take=6):
    data = SeededRecs.objects.filter(source=content_id) \
               .order_by('-confidence') \
               .values('target', 'confidence', 'support')[:take]

    return JsonResponse(dict(data=list(data)), safe=False)



def filtrando(data,ids):
    print(data,ids)
    return [{'id': str(e['id']),'name': e['name']} for e in data if str(e['id']) in ids]


def chart(request, take=10):
    sorted_items = PopularityBasedRecs().recommend_items_from_log(take)
    ids = [i['content_id'] for i in sorted_items]

    #ms = {m['id']: m['name'] for m in Item.createFromJson(Item.getFromApi()).objects.filter(id__in=ids).values('name', 'id')}
    data_api = Item.getFromApi()
    aqui = filtrando(data_api,ids)
    print(aqui)
    ms = {m['id']: m['name'] for m in aqui}
    print(ms)
    sorted_items = [{'content_id': i['content_id'],'name': ms[i['content_id']]} for i in sorted_items if i['content_id'] in ms]
    data = {
        'data': sorted_items
    }

    return JsonResponse(data, safe=False)