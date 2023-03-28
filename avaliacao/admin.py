from django.contrib import admin
from .models import aluno, avaliacao, treinoA, ficha_de_saude, treinoB
#class alunoAdmin(admin.ModelAdmin):

    #list_display = ['nome', 'rcq', 'imc', 'peso', 'altura', 'cintura', 'quadril']

admin.site.register(aluno)
#admin.site.register(personal)
admin.site.register(treinoA)
admin.site.register(treinoB)



admin.site.register(avaliacao)
admin.site.register(ficha_de_saude)