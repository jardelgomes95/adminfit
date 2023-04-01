from django.shortcuts import render
from .models import aluno, avaliacao, exercicio, treinoA, ficha_de_saude, treinoB #treinoC, treinoD, treinoE
from django.contrib import messages         # mensagens do django
from django.urls import reverse_lazy     # retorno após submeter
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView      # class based view
from .forms import avaliacaoForm, treinoAForm


class alunoCreateView(CreateView):
    model = aluno
    template_name = 'create/aluno.html'
    fields = ['nome', 'email', 'cpf', 'phone', 'profissao', 'obs']

    def get_success_url(self):
        messages.success(self.request, 'ALUNO CADASTRADO COM SUCESSO')
        return reverse_lazy('lista_aluno')

class alunoListView(ListView):
    model = aluno
    template_name = 'list/list_aluno.html'
    paginate_by = 20

class alunoUpdateView(UpdateView):
    model = aluno
    template_name = 'update/update_aluno.html'
    fields = ['nome', 'email', 'cpf', 'phone', 'profissao', 'obs']

    def get_success_url(self):
        messages.success(self.request, 'DADOS DO ALUNO ATUALIZADOS COM SUCESSO')
        return reverse_lazy('lista_aluno')

class alunoDetailView(DetailView):
    model = aluno
    template_name = 'detail/detail_aluno.html'




####AVALIAÇÃO#####

class avaliacaoCreateView(CreateView):
    model = avaliacao
    #form_class = avaliacaoForm
    template_name = 'create/avaliacao.html'
    fields = ['nome', 'sexo', 'idade', 'peso', 'altura', 'ativo', 'cintura', 'quadril',
              'torax', 'ombro', 'abdomen', 'biceps', 'bicesps', 'coxa', 'panturrilha',
              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']


    def get_success_url(self):
        messages.success(self.request, 'AVALIAÇÃO CADASTRADA COM SUCESSO')
        return reverse_lazy('lista_avaliacao')

class avaliacaoListView(ListView):
    model = avaliacao
    template_name = 'list/list_avaliacao.html'
    paginate_by = 20

class avaliacaoUpdateView(UpdateView):
    model = avaliacao
    template_name = 'update/update_avaliacao.html'
    fields = ['nome', 'sexo', 'idade', 'peso', 'altura', 'ativo', 'cintura', 'quadril',
              'torax', 'ombro', 'abdomen', 'biceps', 'bicesps', 'coxa', 'panturrilha',
              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']

    def get_success_url(self):
        messages.success(self.request, 'AVALICAÇÃO ATUALIZADA COM SUCESSO')
        return reverse_lazy('lista_alunos')

class avaliacaoDetailView(DetailView):
    model = avaliacao
    template_name = 'detail/detail_avaliacao.html'



#### Treino #####

class treinoCreateView(CreateView):
    model = treinoA
    #form_class = treinoAForm
    template_name = 'create/treino.html'
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'TREINO CADASTRADO COM SUCESSO')
        return reverse_lazy('lista_treino')

class treinoListView(ListView):
    model = treinoA
    template_name = 'list/list_treino.html'
    paginate_by = 20

class treinoUpdateView(UpdateView):
    model = treinoA
    template_name = 'form_page/update_avaliacao.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'TREINO ATUALIZADO COM SUCESSO')
        return reverse_lazy('lista_treino')


class treinoDetailView(DetailView):
    model = treinoA
    template_name = 'detail/detail_treino.html'


#class treinoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    #model = treinoA
    #template_name = 'detalhar/pdfaluno.html'


#####Ficha de Saúde#######

class fichaCreateView(CreateView):
    model = ficha_de_saude
    template_name = 'create/ficha.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'FICHA CADASTRADO COM SUCESSO')
        return reverse_lazy('lista_ficha')

class fichaListView(ListView):
    model = ficha_de_saude
    template_name = 'list/list_ficha.html'
    paginate_by = 20

class fichaUpdateView(UpdateView):
    model = ficha_de_saude
    template_name = 'form_page/update_ficha.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'FICHA ATUALIZADO COM SUCESSO')
        return reverse_lazy('lista_ficha')


class fichaDetailView(DetailView):
    model = ficha_de_saude
    template_name = 'detail/detail_ficha.html'