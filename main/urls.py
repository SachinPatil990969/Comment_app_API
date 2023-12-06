from django.urls import path
from .views import *

urlpatterns = [
    path('Comments/', CommentList, name='CommentList'),
    path('Comments/<int:id>/', CommentDetail, name='CommentDetail'),
]
