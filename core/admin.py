from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from core.models.controle import Categoria, Conta, UserProfile


class PerfilUsuarioInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UsuarioAdmin(UserAdmin):
    inlines = (PerfilUsuarioInLine,)


class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria


class ContaAdmin(admin.ModelAdmin):
    model = Conta

admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Conta, ContaAdmin)
