from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^search-form/$', views.search_form, name="search_form"),
    url(r'^search/$', views.search, name="search"),
    url(r'^checkedout/$', views.checkedout, name="checkedout"),
]
