from django.contrib import admin
from django.urls import path
from movie_app import views
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_list_create_view),
    path('api/v1/movies/', views.movie_list_create_view),
    path('api/v1/reviews/', views.review_list_create_view),
    path('api/v1/directors/<int:id>/', views.director_item_view),
    path('api/v1/movies/<int:id>/', views.movie_item_view),
    path('api/v1/reviews/<int:id>/', views.review_item_view),
    path('api/v1/movies/reviews/', views.MoviesReviews),
    path('api/v1/register/', user_views.registration),
    path('api/v1/login/', user_views.authorization)
]
