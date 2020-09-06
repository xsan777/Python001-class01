from django.urls import path,re_path,register_converter
from . import views,converters
register_converter(converters.IndexConverter,'index')
urlpatterns = [

    path('', views.login_url),
    # path('<str:result>', views.estimate_url),
    # path('<index:index>',views.index_url),
]