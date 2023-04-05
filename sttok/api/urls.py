from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegUserView.as_view()),
    path('cart/', CartList.as_view()),
    path('cart/<int:pk>', CartDestroy.as_view()),
    path('author/',AuthorListcre.as_view()),
    path('author/<int:pk>', AuthorDestroyUpdate.as_view()),
    path('country/', CountryListcre.as_view()),
    path('country/<int:pk>', CountryDestroyUpdate.as_view()),
    path('product/',ProductListcre.as_view()),
    path('product/<int:pk>', ProductDestroyUpdate.as_view()),
    path('order/<int:pk>', OrderDestroyUpdate.as_view()),
    path('order/', OrderListcre.as_view()),
]