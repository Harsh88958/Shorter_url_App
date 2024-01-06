# Imports
from django.urls import path, include
from . import views
from urlshorter.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"urlapi/", UrlPagination)

urlpatterns = [
    # index.html page URL
    path("", views.shorten_url, name="shorten_url"),
    path("all/", views.alldata, name="all"),
    path("urlapi/", include(router.urls)),
    # JWT Access Token URL
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # JWT Refresh Token URL
    path("token/refresh/", TokenRefreshView.as_view(), name="token_obtain_pair"),
    # Short URL redirect URL
    path("<str:short_url>/", views.redirect_url, name="redirect_url"),
    # Search And sort URL
    path("api/table/", TableViewSet.as_view(), name="table-api"),
]


# <----------------------- User and Password ----------------------->
# user:admin
# Password:12345

# <----------------------- All EndPoints ----------------------->
# IndexPage = http://127.0.0.1:8000
# JWTToken = http://127.0.0.1:8000/token/
# All Data With Pagination =  http://127.0.0.1:8000/urlapi/?page=1,
# Search = http://127.0.0.1:8000/api/table/?search=5/ht767   (Enter id or short URL)
# highest and lowest no of click = http://127.0.0.1:8000/api/table/?no_of_count=asc/dsc
