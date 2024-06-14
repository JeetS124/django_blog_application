from django.urls import path
import home.views as home_view


urlpatterns = [
    path('', home_view.BlogHome, name='home'),
]