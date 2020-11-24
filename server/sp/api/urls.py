from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register(r'alerts', views.AlertViewSet)
router.register(r'notifications', views.NotificationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('covid19/', views.covidApiHome),
    path('citizens/', views.ListCitizens.as_view()),
    path('citizens/new/', views.CreateCitizen.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)