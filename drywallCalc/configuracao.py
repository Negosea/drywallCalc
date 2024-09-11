# drywallcalc/configuracao.py

class ConfiguracaoProjeto:
    def __init__(self, altura_parede=3.0, espacamento_perfis=0.6):
        """
        Configurações gerais do projeto.

        Args:
            altura_parede (float): Altura padrão da parede em metros.
            espacamento_perfis (float): Espaçamento entre perfis em metros.
        """
        self.altura_parede = altura_parede
        self.espacamento_perfis = espacamento_perfis

    def ajustar_altura_parede(self, nova_altura):
        """
        Ajusta a altura da parede.

        Args:
            nova_altura (float): Nova altura da parede em metros.
        """
        self.altura_parede = nova_altura

    def ajustar_espacamento_perfis(self, novo_espacamento):
        """
        Ajusta o espaçamento entre perfis.

        Args:
            novo_espacamento (float): Novo espaçamento em metros.
        """
        self.espacamento_perfis = novo_espacamento
