from django.urls import path

from recomendacion import views

urlpatterns = [
    path('chart/', views.chart, name='chart'),
    path('association_rule/<int:content_id>/', views.get_association_rules_for, name='get_association_rules_for')
]
