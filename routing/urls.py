from django.urls import path
from .views import shortest_path_view, esp_event_view, dashboard_text

urlpatterns = [
    path('shortest-path/', shortest_path_view, name='shortest-path'),
    path('esp-event/', esp_event_view, name='esp-event'),
    path('dashboard.txt', dashboard_text, name='dashboard-text'),
    path('dashboard.txt/', dashboard_text),  # 슬래시 실수 대응
]