from django.urls import path, include

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('log/', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
]
