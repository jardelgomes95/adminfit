from django import forms
from .models import avaliacao, aluno, treinoA
from crispy_forms.bootstrap import InlineField


class avaliacaoForm(forms.Form):
    class Meta:
        model: avaliacao
        fields: ['nome', 'sexo', 'idade', 'peso', 'altura', 'ativo', 'cintura', 'quadril',
              'torax', 'ombro', 'abdomen', 'biceps', 'bicesps', 'coxa', 'panturrilha',
              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']


class treinoAForm(forms.Form):
    class Meta:
        model = treinoA
        fields = '__all__'


