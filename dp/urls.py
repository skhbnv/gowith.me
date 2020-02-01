from django.contrib import admin
from django.urls import path
from dp.views import *

urlpatterns = [
    path('event/create/', EventCreateView.as_view()),
    path('location/create/', LocationCreateView.as_view()),
    path('categories/create/', CategoriesCreateView.as_view()),
    path('users/create/', UsersCreateView.as_view()),
    path('images/create/', ImagesCreateView.as_view()),
    # path('comments /create/', CommentsCreateView.as_view()),
    path('list/events/', EventsListView.as_view()),
    path('event/detail/<int:pk>/', EventDetailView.as_view())
]
