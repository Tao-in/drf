from django.conf.urls import url
from .views import *
ulpatterns=[
    url(r'books$',BookListView.as_view()),
    url(r'books/(?P<pk>\d+)$',BookView.as_view())
]