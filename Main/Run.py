from Tasks.Task1 import Task1


class Run:
    # Aqui o usuário seleciona a atividade proposta pelo professor, indicando o numero inteiro ID
    def start(self):
        print("ID .......... TITLE")
        print("1 .......... ATV1")
        task = int(input("Choose task id: "))
        self.chooseTask(task)

    # Método que identifica a atividade e instancia a classe. Após isso, chama o método start
    def chooseTask(self, task):
        baseClass = None

        match task:
            case 1:
                baseClass = Task1()
            case _:
                print("\nInvalid option!")
                exit()

        return baseClass.start()
