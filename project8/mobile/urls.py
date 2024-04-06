from django.urls import path
from mobile.views import*
app_name='anything'

urlpatterns = [
    path('sumsung/',sumsung,name='sumsung'),
    path('oppo/',oppo,name='oppo'),
]
