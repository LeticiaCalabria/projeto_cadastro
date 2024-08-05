from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if Usuario.objects.filter(nome=self.nome, idade=self.idade).exists():
            pass
        else:
            super(Usuario, self).save(*args, **kwargs)
