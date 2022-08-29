from Services.File import File


class Task1:
    file = File

    # Inicia a atividade proposta
    def start(self):
        fileName = input("\n\nDigite o nome do arquivo: ")

        # Lê o arquivo
        readFile = self.file.readFile(self.file, fileName)

        if readFile.all():
            print("File not found.")
            exit()

        # Escreve o resultado em arquivo
        result = self.file.writeFile(self.file, readFile, fileName)

        print(result)
