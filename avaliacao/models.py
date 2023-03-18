from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class aluno(models.Model):

    #cadastro do aluno
    nome = models.CharField(max_length=55, blank=False, null=False, verbose_name="Nome do Aluno")
    matricula = models.CharField(max_length=7, unique=True, null=True, blank=True, verbose_name="Matricula")
    email = models.EmailField(blank=True, null=True)
    cpf = models.CharField(max_length=15, blank=False, null=False, unique=True, verbose_name="CPF")
    phone = models.CharField(max_length=15, blank=False, null=False, unique=True, verbose_name="Telefone")
    profissao = models.CharField(max_length=36, blank=False, null=False, verbose_name="Profissão")
    data = models.DateField(default=datetime.today(), blank=False, null=False, verbose_name="Data do Cadastro")
    obs = models.TextField(max_length=255, blank=True, null=True, verbose_name="Observações")

    def save(self, *args, **kwargs):
        if not self.matricula:
            # obter as iniciais "KL"
            iniciais = "KL"
            # obter o próximo número sequencial
            ultima_matricula = aluno.objects.order_by('-matricula').first()
            numero_sequencial = int(ultima_matricula.matricula[2:]) + 1 if ultima_matricula else 1
            # criar a nova matrícula
            self.matricula = '{}{:03d}'.format(iniciais, numero_sequencial)
        super().save(*args, **kwargs)


    def __str__(self): return f'{self.nome, self.matricula}'

#class financeiro(models.Model):
#    #Controle Financeiro
#    PLANO_CHOICES = (
#        ("M", "Mensal"),
#        ("T", "Trimestral"),
#        ("S", "Semestral")
#    )

#    nome = models.ForeignKey('aluno', on_delete=models.DO_NOTHING, default=1, verbose_name="Aluno")
#    plano = models.CharField(choices=PLANO_CHOICES, max_length=3, blank=False,  null=False, verbose_name="Sexo")
#    data_pgto = models.DateField(default=datetime.today(), verbose_name="Data do Pagamento")
#    vencimento = models.DateField(blank=True,  null=True, verbose_name="Vencimento")

#   def save(self, *args, **kwargs):
#        if self.plano == "M":
#            self.vencimento = datetime.today() + timedelta(days=30)

#        elif self.plano == "T":
#            self.vencimento = datetime.today() + timedelta(days=90)

#        else:
#            self.vencimento = datetime.today() + timedelta(days=180)

#        super().save(*args, **kwargs)


#################################################################################################################

class avaliacao(models.Model):
    #Avaliação Física
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino")

    )
    nome = models.ForeignKey('aluno', on_delete=models.DO_NOTHING, default=1, verbose_name="Aluno")
    dt_avaliacao = models.DateField(default=datetime.today(), verbose_name="Data da Avaliação")
    px_avaliação = models.DateField(default=datetime.today() + timedelta(days=90), verbose_name="Data da Próxima Avaliação")
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=3, blank=False,  null=True, verbose_name="Sexo")
    idade = models.IntegerField(null=True, blank=False, verbose_name="Idade")
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False, verbose_name="Altura")
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Peso (Kg)")
    imc = models.FloatField(null=True, blank=True, verbose_name="IMC")
    ativo = models.BooleanField(null=True, blank=True, verbose_name="Já Fez Atividade Física")
    cintura = models.IntegerField(null=True, blank=True, verbose_name="Medida Cintura (cm)")
    quadril = models.IntegerField(null=True, blank=True, verbose_name="Medida Quadril (cm)")
    torax = models.IntegerField(null=True, blank=False, verbose_name="Tórax (cm)")
    ombro = models.IntegerField(null=True, blank=False, verbose_name="Ombro (cm)")
    abdomen = models.IntegerField(null=True, blank=False, verbose_name="Abdomên (cm)")
    biceps = models.IntegerField(null=True, blank=False, verbose_name="Biceps Relaxado (cm)")
    bicesps = models.IntegerField(null=True, blank=False, verbose_name="Biceps Contraído (cm)")
    coxa = models.IntegerField(null=True, blank=False, verbose_name="Coxa (cm)")
    panturrilha = models.IntegerField(null=True, blank=False, verbose_name="Panturrilha (cm)")
    rcq = models.FloatField(null=True, blank=True, verbose_name="RCQ")

    #parte 3
    d1 = models.IntegerField(null=True, blank=True, verbose_name="Subescapular")
    d2 = models.IntegerField(null=True, blank=True, verbose_name="Tricipital")
    d3 = models.IntegerField(null=True, blank=True, verbose_name="Peitoral")
    d4 = models.IntegerField(null=True, blank=True, verbose_name="Axilar Média")
    d5 = models.IntegerField(null=True, blank=True, verbose_name="Supra-Ilíaca")
    d6 = models.IntegerField(null=True, blank=True, verbose_name="Cutânea Abdominal")
    d7 = models.IntegerField(null=True, blank=True, verbose_name="Femural Médio")
    #d_soma = models.FloatField(null=True, blank=True, verbose_name="Soma Dobras", editable=False)
    #dc1 = models.FloatField(null=True, blank=True, verbose_name="Dobras Cutâneas 1", editable=False)
    #dc2 = models.FloatField(null=True, blank=True, verbose_name="Dobras Cutâneas 2", editable=False)
    #dc3 = models.FloatField(null=True, blank=True, verbose_name="Dobras Cutâneas 3", editable=False)
    #dctotal = models.FloatField(null=True, blank=True, verbose_name="Densidade Corporal", editable=False)
    gordura = models.FloatField(null=True, blank=True, verbose_name="gordura em %")



    def save(self, *args, **kwargs):

        #Calculando o imc
        imc = self.peso / (self.altura * self.altura)   # calculo de imc
        self.imc = imc

        self.rcq = self.cintura / self.quadril  #calculo relação cintura quadril

        dc = self.d1 + self.d2 + self.d3 + self.d4 + self.d5 + self.d6 + self.d7 #soma das dobras cutâneas

        if self.sexo == 'F':
            dc1 = 1.0970
            dc2 = (0.00046971 * dc) + (0.00000056 * dc ** 2)
            dc3 = 0.00012828 * self.idade
        else:
            dc1 = 1.11200000
            dc2 = (0.00043499 * dc) + (0.00000055 * dc ** 2)
            dc3 = 0.0002882 * self.idade

        dct = dc1 - dc2 - dc3  #densidade corporal
        self.gordura = round(((4.95 / dct) - 4.50) * 100, 2)  #% de gordura corporal
        super(avaliacao, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return f'{self.nome}'


######################################### - Bloco de Ficha de Saúde - ###################################################


class ficha_de_saude(models.Model):

    VERDADEIRO_CHOICES = (
    ("S", "Sim"),
    ("N", "Não"),
    ("NI", "Não Informado"),
    )

    BEBIDA_CHOICES = (
        ("S", "Sempre que Posso"),
        ("O", "Ocasionalmente"),
        ("R", "Raramente"),
        ("N", "Não Bebo")
    )

    nome = models.ForeignKey('aluno', on_delete=models.DO_NOTHING, default=1, verbose_name="Aluno")
    diabetes = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Diabetes")
    hipertensao = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Hipertensão")
    artrite = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrite")
    artrose = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrose")
    reumatismo = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Reumatismo")
    doencas_cardiacas = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Doenças Cardiacas")
    avc = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Já Sofreu AVC")
    fuma = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Tabagismo")



    bebe = models.CharField(max_length=2, choices=BEBIDA_CHOICES, blank=False, null=True, verbose_name="Bebe")
    insulina = models.BooleanField(null=False, blank=False, verbose_name="Insulina")
    antidepressivos = models.BooleanField(null=False, blank=False, verbose_name="Antidepressivos")
    antihistaminicos = models.BooleanField(null=False, blank=False, verbose_name="Anti-Histaminicos (Alergia)")
    betabloqueadores = models.BooleanField(null=False, blank=False, verbose_name="Betabloqueadores (Hipertensão)")
    analgesicos = models.BooleanField(null=False, blank=False, verbose_name="Analgésicos")
    ansiolitico = models.BooleanField(null=False, blank=False, verbose_name="Ansiolítico (Ansiedade)")
    suplementos_vit = models.BooleanField(null=False, blank=False, verbose_name="Suplementos Vitamínicos")
    observacoes = models.TextField(max_length=255, blank=True, null=True, verbose_name="Observações")

    class Meta:
        verbose_name_plural = "Fichas de Saúde"

    def __str__(self):
       return f'{self.nome}'

############################################################### --- ###################################################################


class exercicio(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nome do Exercicio")
    repeticoes = models.CharField(max_length=16, blank=True, null=True, verbose_name="Repetições")

    class Meta:
        verbose_name_plural = 'Cadastro de Exercicios'

    def __str__(self):
        return f'{self.nome}'
################################################################### --- ################################################################

class treinoA(models.Model):
    nome = models.ForeignKey('aluno', on_delete=models.DO_NOTHING, default=None, verbose_name="Aluno")
    aexc_1 = models.CharField(max_length=100, blank=False, null=True, verbose_name="1")
    rep1 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_2 = models.CharField(max_length=100, blank=False, null=True, verbose_name="2")
    rep2 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_3 = models.CharField(max_length=100, blank=False, null=True, verbose_name="3")
    rep3 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_4 = models.CharField(max_length=100, blank=False, null=True, verbose_name="4")
    rep4 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_5 = models.CharField(max_length=100, blank=False, null=True, verbose_name="5")
    rep5 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_6 = models.CharField(max_length=100, blank=False, null=True, verbose_name="6")
    rep6 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_7 = models.CharField(max_length=100, blank=False, null=True, verbose_name="7")
    rep7 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_8 = models.CharField(max_length=100, blank=False, null=True, verbose_name="8")
    rep8 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_9 = models.CharField(max_length=100, blank=False, null=True, verbose_name="9")
    rep9 = models.CharField(max_length=6, blank=False, null=True, verbose_name='RP')
    aexc_10 = models.CharField(max_length=100, blank=False, null=True, verbose_name="10")
    rep10 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_11 = models.CharField(max_length=100, blank=False, null=True, verbose_name="11")
    rep11 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_12 = models.CharField(max_length=100, blank=False, null=True, verbose_name="12")
    rep12 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_13 = models.CharField(max_length=100, blank=False, null=True, verbose_name="13")
    rep13 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_14 = models.CharField(max_length=100, blank=False, null=True, verbose_name="14")
    rep14 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_15 = models.CharField(max_length=100, blank=False, null=True, verbose_name="15")
    rep15 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_16 = models.CharField(max_length=100, blank=False, null=True, verbose_name="16")
    rep16 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_17 = models.CharField(max_length=100, blank=False, null=True, verbose_name="17")
    rep17 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_18 = models.CharField(max_length=100, blank=False, null=True, verbose_name="18")
    rep18 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_19 = models.CharField(max_length=100, blank=False, null=True, verbose_name="19")
    rep19 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_20 = models.CharField(max_length=100, blank=True, null=True, verbose_name="20")
    rep20 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_21 = models.CharField(max_length=100, blank=True, null=True, verbose_name="21")
    rep21 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_22 = models.CharField(max_length=100, blank=True, null=True, verbose_name="22")
    rep22 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_23 = models.CharField(max_length=100, blank=True, null=True, verbose_name="23")
    rep23 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_24 = models.CharField(max_length=100, blank=True, null=True, verbose_name="24")
    rep24 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_25 = models.CharField(max_length=100, blank=True, null=True, verbose_name="25")
    rep25 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_26 = models.CharField(max_length=100, blank=True, null=True, verbose_name="26")
    rep26 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_27 = models.CharField(max_length=100, blank=True, null=True, verbose_name="27")
    rep27 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_28 = models.CharField(max_length=100, blank=True, null=True, verbose_name="28")
    rep28 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_29 = models.CharField(max_length=100, blank=True, null=True, verbose_name="29")
    rep29 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')
    aexc_30 = models.CharField(max_length=100, blank=True, null=True, verbose_name="30")
    rep30 = models.CharField(max_length=6, blank=True, null=True, verbose_name='RP')


    obs = models.TextField(max_length=400, blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f'{self.nome}'



#class personal(models.Model):
#    nome_personal = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome do Personal')
#    numero_cref = models.CharField(max_length=10, blank=True, null=True, verbose_name='Número do CREF')