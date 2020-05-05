from django.urls import path

from .views import PublisherV, AuthorV, BookV

urlpatterns = [
    path('publisher', PublisherV.as_view()),
    path('publisher/<int:pk>', PublisherV.as_view()),
    path('author', AuthorV.as_view()),
    path('author/<int:pk>', AuthorV.as_view()),
    path('book', BookV.as_view()),
    path('book/<int:pk>', BookV.as_view()),
]
