from django.urls import path
from .  import views, include
from my_app import views

urlpatterns = [ 
    path('', include('my_app.urls'))
    path('admin/', views.home, name='admin.site.urls')
]