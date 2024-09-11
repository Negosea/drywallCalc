# drywallcalc/material.py

class Material:
    def __init__(self, nome, unidade, preco_por_unidade):
        """
        Representa um material de drywall.

        Args:
            nome (str): Nome do material.
            unidade (str): Unidade de medida (ex: 'metro', 'unidade', etc.).
            preco_por_unidade (float): Preço do material por unidade.
        """
        self.nome = nome
        self.unidade = unidade
        self.preco_por_unidade = preco_por_unidade

    def calcular_custo(self, quantidade):
        """
        Calcula o custo total de acordo com a quantidade necessária.

        Args:
            quantidade (float): Quantidade necessária do material.

        Returns:
            float: Custo total.
        """
        return quantidade * self.preco_por_unidade
