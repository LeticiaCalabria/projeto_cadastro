from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("usuarios/", views.usuarios, name="listagem_usuarios"),
    path("editar/<int:id_usuario>", views.editar, name="editar"),
    path("update/<int:id_usuario>", views.update, name="update"),
    path("delete/<int:id_usuario>", views.delete, name="delete")
]