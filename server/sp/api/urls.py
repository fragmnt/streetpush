from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register(r'alerts', views.AlertViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('covid19/', views.covidApiHome),
    path('covid19/resources/', views.covidResources),
    path('covid19/timeline/', views.covidTimeseries),
]

# urlpatterns = format_suffix_patterns(urlpatterns)