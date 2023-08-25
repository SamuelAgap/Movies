from django.contrib import admin

from filmes.models import Movie, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", "created_date")



@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", "age", "created_date", )
    list_editable = ("age", )

