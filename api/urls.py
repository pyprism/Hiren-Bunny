from django.conf.urls import url, include
from api import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'reminder', ReminderViewSet)

urlpatterns = [
    url(r'token/', views.login),
    # url(r'^reminder/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]