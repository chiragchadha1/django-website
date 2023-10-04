from django.urls import path
from . import views

app_name = 'football' # to distinguish from other possible apps
urlpatterns = [
	path('', views.home, name='home'), # we have to write a view called home
]