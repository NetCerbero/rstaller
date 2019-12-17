from django.conf.urls import url
from analitica import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/get_statistics', views.get_statistics, name='get statistics'),
	url(r'^api/events_on_conversions', views.events_on_conversions, name='events_on_conversions'),
    url(r'^api/ratings_distribution', views.ratings_distribution, name='ratings_distribution'),
	url(r'^api/top_content', views.top_content, name='top_content'),
]