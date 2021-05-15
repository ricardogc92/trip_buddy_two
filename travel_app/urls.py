from django.urls import path
from . import views

urlpatterns=[
    path('new', views.new),
    path('create', views.create),
    path('<int:trip_id>', views.show),
    path('edit/<int:trip_id>', views.edit),
    path('update/<int:trip_id>', views.update),
    path('destroy/<int:trip_id>', views.delete),
    path('join/<int:trip_id>', views.join),
    path('cancel/<int:trip_id>', views.cancel),
]