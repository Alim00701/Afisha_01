from django.contrib import admin
from django.urls import path
from movie_app import views
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_list_create_view),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewModelViewSet.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieItemAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', views.ReviewItemAPIView.as_view()),
    path('api/v1/movies/reviews/', views.MoviesReviews),
    path('api/v1/register/', user_views.RegisterAPIView.as_view()),
    path('api/v1/login/', user_views.AuthAPIView.as_view()),
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', views.DirectorItemAPIView.as_view())
]
