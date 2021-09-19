from django.db import models

# Create your models here.
class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=250, blank=False, default='')
    NumeroUC = models.CharField(max_length=250, blank=False, default='')
    UCsCompensacao = models.JSONField(blank=False, default=dict({}))
    Localizacao = models.CharField(max_length=380, blank=False, default='')
    CEP = models.CharField(max_length=40, blank=False, default='')
    Bairro = models.CharField(max_length=100, blank=False, default='')
    Email = models.EmailField(max_length=200, blank=False, default='')
    Telefone = models.CharField(max_length=250, blank=False, default='')
    CPF_CNPJ = models.CharField(max_length=250, blank=False, default='')
    ValorEFormaPagamento = models.TextField(max_length=2500, blank=False, default='')
    Notas = models.TextField(max_length=2500, blank=False, default='')

class DadosConcessionarias(models.Model):
    id = models.AutoField(primary_key=True)
    CargaInstalada = models.FloatField()
    PadraoEntrada = models.TextField(max_length=2500, blank=False, default='')
    TensaoAtendimento = models.TextField(max_length=2500, blank=False, default='')
    TipoConexao = models.TextField(max_length=2500, blank=False, default='')
    PotenciaInstalada = models.FloatField()
    PotenciaModulos = models.FloatField()
    PotenciaInversores = models.FloatField()
    NumeroArranjos = models.IntegerField()
    idCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

class RespostaComercial(models.Model):
    id = models.AutoField(primary_key=True)
    RespostaComercial = models.JSONField(blank=False, default=dict({}))
    idCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

class RespostaTecnica(models.Model):
    id = models.AutoField(primary_key=True)
    RespostaTecnica = models.JSONField(blank=False, default=dict({}))
    idCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)