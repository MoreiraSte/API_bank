from django.contrib import admin
from django.db.models import Count, QuerySet,Sum
from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Conta)
admin.site.register(models.Transferencia)
admin.site.register(models.Cartoes)
# admin.site.register(models.Faturas)
admin.site.register(models.Emprestimos)
admin.site.register(models.PgtoEmprestimo)
admin.site.register(models.Extrato)





