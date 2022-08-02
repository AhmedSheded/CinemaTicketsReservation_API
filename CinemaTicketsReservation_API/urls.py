"""CinemaTicketsReservation_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from tickets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('gusts', views.Viewsets_guest)
router.register('movie', views.Viewsets_movie)
router.register('reservation', views.Viewsets_reservation)
urlpatterns = [
    path('admin/', admin.site.urls),
    # 1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    # 2
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),

    # 3.1 GET POST from rest framework, function based view @api_view
    path('rest/fbv/', views.FVB_List),
    # 3.2 GET PUT DELETE from rest framework, function based view @api_view
    path('rest/fbv/<int:pk>', views.FBV_pk),


    # 4.1 GET POST from rest framework class based view APIView
    path('rest/cbv/', views.CBV_List.as_view()),
    # 4.2 GET PUT DELETE from rest framework class based view APIView
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),


    # 5.1 GET POST from rest framework class based view Mixins
    path('rest/mixins/', views.Mixins_list.as_view()),
    # 5.2 GET PUT DELETE from rest framework class based view Mixins
    path('rest/mixins/<int:pk>', views.Mixins_pk.as_view()),


    # 6.1 GET POST from rest framework class based view Generics
    path('rest/generics/', views.Generics_list.as_view()),
    # 6.2 GET PUT DELETE rest ffamework class based view Genrics
    path('rest/generics/<int:pk>', views.Generics_pk.as_view()),


    # 7 viewsets
    path('rest/viewsets/', include(router.urls)),

    # 8 find movie
    path('fbv/findmovie/', views.find_movie),

    # 9 new reservation
    path('fbv/new_reservation/', views.new_reservation),

    # 10 rest auth url
    path('api-auth', include('rest_framework.urls')),

    # 11 token authentication
    path('api-token-auth', obtain_auth_token),

    # 12 post pk generics post_pk
    path('post/generics/<int:pk>', views.Post_pk.as_view()),
    # path('post/generics/<int:pk>', views.Post_list.as_view())
]
