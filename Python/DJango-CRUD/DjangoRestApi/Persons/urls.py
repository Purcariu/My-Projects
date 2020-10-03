from django.conf.urls import url, include
from Persons import views 
 
urlpatterns = [
    url(r'^api/persons$', views.person_list),
    url(r'^api/persons/(?P<id>[0-9]+)$', views.person_detail)
]
