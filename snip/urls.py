from django.urls import path
from snip import views

urlpatterns = [
     path('books/', views.book_list),
      path('', views.ApiOverview, name='home'),
     path('create/', views.add_items, name='add-items'),
     path('all/', views.view_items, name='view_items'),
      path('update/<int:pk>/', views.update_items, name='update-items'),
      path('item/<int:pk>/delete/', views.delete_items, name='delete-items')
    #  path('books/<int:pk>/', views.book_detail),
  
]
