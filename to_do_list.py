import json
import os
import sys

# Detecta se está rodando como .exe (PyInstaller) ou como script normal
if getattr(sys, 'frozen', False):
    PASTA = os.path.dirname(sys.executable)  # pasta do .exe
else:
    PASTA = os.path.dirname(os.path.abspath(__file__))  # pasta do .py

ARQUIVO = os.path.join(PASTA, "tarefas.json")

# FUNÇÕES AUXILIARES -----------------------------------------------------------------------

def limpar_terminal():
    os.system('cls')

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    return []

def atualizar_id(tarefas):
    i = 1
    for tarefa in tarefas:
        tarefa['id'] = i
        i += 1

# MAIN FUNÇÕES -----------------------------------------------------------------------

def ver_tarefas():
    dados = carregar_tarefas()
    for tarefa in dados:
        if tarefa['concluida'] == False:
            print(f"{tarefa['tarefa']} - [ ]")
        else:
            print(f"{tarefa['tarefa']} - [X]")

def adicionar_tarefa():
    tarefa_pra_adicionar = input("Digite a tarefa que você deseja adicionar: ")
    dados_tarefas = carregar_tarefas()
    nova_tarefa ={"id": len(dados_tarefas) + 1, "tarefa": tarefa_pra_adicionar, "concluida": False}
    dados_tarefas.append(nova_tarefa)
    salvar_tarefas(dados_tarefas)
    
def salvar_tarefas(tarefa):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefa, arquivo, indent=4, ensure_ascii=False)


def remover_tarefa():
    ver_tarefas()
    escolha_remover = input("\nEscolha a tarefa para ser retirada.\n\n")
    escolha_remover_upper = escolha_remover.upper()
    
    dados = carregar_tarefas()
    for tarefas in dados:
        tarefa_upper = str(tarefas['tarefa']).upper()
        if tarefa_upper == escolha_remover_upper:
            dados.remove(tarefas)
            atualizar_id(dados)
            salvar_tarefas(dados)
            print("\nTarefa removida!")
            return
    print("\nTarefa não encontrada")

    
def marcar_tarefas():
    ver_tarefas()
    escolha_marcar = input("\nEscolha a tarefa para ser marcada.\n\n")
    escolha_marcar_upper = escolha_marcar.upper()
    
    dados = carregar_tarefas()
    for tarefas in dados:
        tarefa_upper = str(tarefas['tarefa']).upper()
        if tarefa_upper == escolha_marcar_upper:
            if tarefas['concluida'] == True:
                tarefas['concluida'] = False
            else:
                tarefas['concluida'] = True         
            salvar_tarefas(dados)
            print("\nTarefa alterada!")
            return
    print("\nTarefa não encontrada")


# LOOP DE ESCOLHAS -----------------------------------------------------------------------

saiu = False

while saiu == False: 
    limpar_terminal()

    print("Bem vindo ao banco pessoal, o que deseja fazer?\n")
    escolha = input("Verificar tarefas\n"
    "Adicionar tarefas\n"
    "Remover Tarefas\n"
    "Marcar Tarefas\n" \
    "Sair\n")

    print("\n")
    escolhaUpper = escolha.upper()
    match escolhaUpper:
        case"VERIFICAR":
            ver_tarefas()
        case"ADICIONAR":
            adicionar_tarefa()
        case"REMOVER":
            remover_tarefa()
        case"MARCAR":
            marcar_tarefas()
        case"SAIR":
            saiu = True
        case"":
            print("Escolha uma das opções")
            break

    if(escolhaUpper != "SAIR"):
        enter = input("\nVoltar - pressione ENTER\n\n")