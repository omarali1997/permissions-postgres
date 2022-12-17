from django.urls import path
from .views import SnackListView,SnackDetailView,PostListView,PostDetailView

urlpatterns=[
    path('',SnackListView.as_view(),name='snack_list'),
    path('<int:pk>',SnackDetailView.as_view(),name='snack_detail'),

    path('posts/',PostListView.as_view(),name='Post_list'),
    path('posts/<int:pk>',PostDetailView.as_view(),name='Post_detail'),

    
]