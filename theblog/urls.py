
from django.urls import path
from .views import HomeView , ArticaleDetailview, AddPostView



urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticaleDetailview.as_view(), name='article-detail' ),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    

]
