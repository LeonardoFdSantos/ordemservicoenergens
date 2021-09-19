from rest_framework import serializers
from clientes.models import Clientes
from clientes.models import DadosConcessionarias
from clientes.models import RespostaComercial
from clientes.models import RespostaTecnica

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = (
                'id',
                'Nome',
                'NumeroUC',
                'UCsCompensacao',
                'Localizacao',
                'CEP',
                'Bairro',
                'Email',
                'Telefone',
                'CPF_CNPJ',
                'ValorEFormaPagamento',
                'Notas')

class DadosConcessionariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosConcessionarias
        fields = (
            'id',
            'CargaInstalada',
            'PadraoEntrada',
            'TensaoAtendimento',
            'TipoConexao',
            'PotenciaInstalada',
            'PotenciaModulos',
            'PotenciaInversores',
            'NumeroArranjos',
            'idCliente')

class RespostaComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaComercial
        fields = (
            'id',
            'RespostaComercial',
            'idCliente'
        )

class RespostaTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaTecnica
        fields = (
            'id',
            'RespostaTecnica',
            'idCliente'
        )