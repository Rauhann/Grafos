import os
import numpy as np
from datetime import datetime


class File:

    # Faz leitura de arquivo no sistema e gera o array Numpy
    def readFile(self, fileName):
        file = self.__getDataFolder(self) + fileName

        if self.__checkFileExists(self, file):
            with open(file, 'rb') as f:
                nRows = sum(1 for line in f)
            with open(file, 'rb') as f:
                data = np.genfromtxt(f, dtype="int32", max_rows=nRows)
            return data
        return False

    # Método que cria o arquivo e retorna o resultado tanto para o terminal, quanto para a escrita no arquivo em
    # data/output/"nome do arquivo"
    def writeFile(self, arrayNumpy, fileName):
        output = open(self.__getDataFolder(self) + 'output\\' + fileName, 'a+')
        row, col = arrayNumpy.shape
        dateHeader = datetime.now()
        dateHeaderFormatted = dateHeader.strftime('%d/%m/%Y %H:%M')

        result = "Executado em: " + dateHeaderFormatted + \
                 "\nnome_instancia: " + fileName + \
                 "\nqtd_linhas: " + str(row) + \
                 "\nqtd_colunas: " + str(col) + \
                 "\n\n"
        output.writelines(result)

        return result

    # Verifica se arquivo existe na pasta data
    def __checkFileExists(self, file):
        return os.path.exists(file)

    # Devolve a pasta default de arquivos
    def __getDataFolder(self):
        basepath = os.path.dirname(os.path.abspath(__file__))
        return basepath.replace('Services', '') + 'data\\'
