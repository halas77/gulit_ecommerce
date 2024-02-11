from django.urls import path
from .views import detail, example, detailed


app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('sample/', example, name='example'),
    path('sample/<int:id>/', detailed, name='detailed'),

]
