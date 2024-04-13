from django.urls import path

from .views import SearchEngineView

app_name = "search_engine"
urlpatterns = [
    path("", SearchEngineView.as_view(), name="search"),
]
