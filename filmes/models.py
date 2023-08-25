from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="NOME DO FILME")
    actor = models.ManyToManyField("Actor", verbose_name="NOME DO ATOR") #Actor está entre aspas porque, como o código é sequencial, ele ainda não existe, apenas la em baixo
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ("name", )

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name="NOME DO ATOR")
    age = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
        ordering = ("name",)

    def __str__(self):
        return self.name
