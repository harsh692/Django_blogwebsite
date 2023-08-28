from django.urls import path,include
from .views import HomeView, ArticalDetailView,PostView,Update_View,Delete_View, Category_View, CategoryViewTwo, CategoryPageView


urlpatterns = [
    # path('',views.home,name = "home")
    ## Since we are using class based views, this will have to be changed.
    path('',HomeView.as_view(),name = "home"),
    path('artical/<int:pk>',ArticalDetailView.as_view(),name="articaldetails"),
    path('artical/Createpost',PostView.as_view(),name = 'CreatePosts'),
    path('artical/update/<int:pk>',Update_View.as_view(),name="UpdateViewPost"),
    path('artical/delete/<int:pk>',Delete_View.as_view(),name='DeleteViewPost'),
    path('artical/category',Category_View.as_view(),name='CreateCategory'),

    path('artical/ViewCategory/<str:cats>',CategoryViewTwo,name='categoryTwo'),
    path('artical/categories_page',CategoryPageView,name='categoryPage'),
    # path('like/<int:pk>',LikeView,name='like_post'),
]
