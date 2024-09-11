# drywallcalc/importador.py
import csv

class AcessoriosImportador:
    def __init__(self, caminho_arquivo):
        """
        Inicializa o importador com o caminho para o arquivo CSV.

        Args:
            caminho_arquivo (str): Caminho do arquivo CSV de acessórios.
        """
        self.caminho_arquivo = caminho_arquivo

    def importar(self):
        """
        Importa os acessórios do arquivo CSV.

        Returns:
            list: Lista de dicionários representando os acessórios.
        """
        acessorios = []
        with open(self.caminho_arquivo, newline='', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)
            for row in leitor:
                acessorios.append(row)
        return acessorios
