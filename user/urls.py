from django.urls import path

from .views import (
	CustomAuthToken,
	UserRegisterView,
	UserListView,
)


urlpatterns = [
	path('login/', CustomAuthToken.as_view()),
	path('register/', UserRegisterView.as_view()),
	path('list/', UserListView.as_view()),
	path('list/<int:pk>/', UserListView.as_view()),

]