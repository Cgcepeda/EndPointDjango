from django.urls import include, path
from rest_framework import routers
from . import views
from .serializers import TransactionResource


router = routers.DefaultRouter()
router.register(r'reviews', views.ReviewsViewSet)
router.register(r'propertytypes', views.PropertyTypesViewSet)
router.register(r'states',views.StatesViewSet)
router.register(r'categories',views.CategoriesViewSet)
router.register(r'cities',views.CitiesViewSet)
router.register(r'properties',views.PropertiesViewSet)
router.register(r'transaction',views.TransactionViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('transaction_propertytypes/', include(TransactionResource.urls()))
]