def adicionar_tarefa(lista_tarefas, tarefa):
    """Adiciona uma nova tarefa na lista de tarefas"""
    lista_tarefas.append(tarefa)
    print(f"=> Tarefa '{tarefa}' adicionada com sucesso.")
    return lista_tarefas


def listar_tarefas(lista_tarefas):
    """Exibe todas as tarefas cadastradas em formato de lista"""
    print('\n')
    print("-" * 50)
    print(f"{' '*15}Lista de tarefas")
    print("-" * 50)
    if not lista_tarefas:
        print("Você não tem tarefa cadastrada.")
    else:
        n = 1
        for tarefa in lista_tarefas:
            print(f"{n} - {tarefa}")
            n += 1
            print("-" * 50)


def deletar_tarefa(lista_tarefas, tarefa):
    """Deleta uma tarefa da lista a partir do número informado"""
    lista_tarefas.pop((tarefa - 1))
    return lista_tarefas


def exibir_menu():
    """Exibe o menu principal com as opções disponíveis"""
    print("-" * 50)
    print("Escolha uma opção: \n1. Adicionar tarefa\n" \
            "2. Ver tarefas\n" \
            "3. Deletar tarefa\n"
            "4. Sair")
    print("-" * 50)


# ---------------- PROGRAMA PRINCIPAL ---------------- #
"""Gerenciador de tarefas simples com opções de adicionar, listar e deletar"""

# Inicialização das variáveis
lista_tarefas = []
continuar = True

#Cabeçalho do programa
print('\n')
print("-" * 50)
print("Bem-vinde ao seu gerenciador de tarefas!".upper())
print("-" * 50)

# Loop principal do programa
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == '1':
        nova_tarefa = input("Insira a tarefa: ")
        lista_tarefas = adicionar_tarefa(lista_tarefas, nova_tarefa)

    elif opcao == '2':
        listar_tarefas(lista_tarefas)

    elif opcao == '3':
        if not lista_tarefas:
            print("Não há tarefas para deletar.")
        else:
            try:
                tarefa = int(input("Insira o número da tarefa que deseja deletar: "))
                if tarefa <= 0 or tarefa > len(lista_tarefas):
                    print("Número inválido! Tente novamente.")
                else:
                    deletar_tarefa(lista_tarefas, tarefa)
                    print("Tarefa deletada com sucesso.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    elif opcao == '4': 
        continuar = False
    else:
        print("Opção inválida, tente novamente.")
    print('\n')

print("Programa encerrado. Suas tarefas finais:", lista_tarefas)
