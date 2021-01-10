from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_form/',views.student_form, name='student_form'),
    path("student_info/<int:id>",views.student_info, name='student_info'),
    path("student_update/<int:id>",views.student_update, name='student_update'),
    path("student_delete/<int:id>",views.student_delete, name='student_delete'),

]
