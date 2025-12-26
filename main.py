import json

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(tarefas):
    titulo = input("Digite a tarefa: ")
    tarefas.append({
        "titulo": titulo,
        "concluida": False
    })
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "✖"
        print(f"{i} - [{status}] {t['titulo']}")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    indice = int(input("Digite o índice da tarefa concluída: "))

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("✅ Tarefa marcada como concluída!")
    else:
        print("❌ Índice inválido")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida")

menu()
