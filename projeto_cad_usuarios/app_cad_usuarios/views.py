from django.shortcuts import render, redirect
from .models import Usuario


def home(request):
    return render(request, "usuarios/home.html")


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    novo_usuario.save()

    usuarios = {
        "usuarios": Usuario.objects.all()
    }
    return render(request, "usuarios/usuarios.html", usuarios)


def editar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    return render(request, "usuarios/update.html", {"usuario": usuario})


def update(request, id_usuario):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.nome = novo_usuario.nome
    usuario.idade = novo_usuario.idade
    usuario.save()
    return redirect(usuarios)


def delete(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()
    return redirect(usuarios)
