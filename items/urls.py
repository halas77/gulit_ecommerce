from django.urls import path
from .views import detail, example, detailed, product_view


app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('sample/', example, name='example'),
    path('sample/<int:id>/', detailed, name='detailed'),
    path('test/', product_view, name='product') 

]
