from django.urls import path,include
from .views import HomeView, ArticalDetailView,PostView


urlpatterns = [
    # path('',views.home,name = "home")
    ## Since we are using class based views, this will have to be changed.
    path('',HomeView.as_view(),name = "home"),
    path('artical/<int:pk>',ArticalDetailView.as_view(),name="articaldetails"),
    path('artical/Createpost',PostView.as_view(),name = 'CreatePosts')
]
