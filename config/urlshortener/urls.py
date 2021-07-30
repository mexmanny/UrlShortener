'''
Custom urls for shortener app
'''

from django.urls import path
# Import the views
from .views import home_view, redirect_url_view

appname = "shortener"


urlpatterns = [
    # Home view
    path("shortener/", home_view, name="home"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]