from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ApartmentListView, ApartmentDetailView, ApartmentDeleteView, create_apartment, apartment_update

app_name = 'apartments'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/', ApartmentListView.as_view(), name='apartment_list'),
    path('apartment_detail/<pk>/',
         ApartmentDetailView.as_view(), name='apartment_detail'),
    path('create_apartment', create_apartment, name='create_apartment'),
    path('apartment_update/<pk>/',
         apartment_update, name='apartment_update'),
    path('delete_apartment/<pk>/', ApartmentDeleteView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
