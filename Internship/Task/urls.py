from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('sum/<int:number1>/<int:number2>', views.Sum.as_view()),
    path('<int:number1>/subtracted_by/<int:number2>', views.difference.as_view()),
    path('<int:number1>/multiplied_by/<int:number2>', views.multiplication.as_view()),
    path('<int:number1>/divided_by/<int:number2>', views.Division.as_view()),
]
