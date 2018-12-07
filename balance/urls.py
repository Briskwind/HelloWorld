from django.conf.urls import url

from balance import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),

]
