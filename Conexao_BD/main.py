import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="50.116.86.45",
        user="argqor30_aluno",
        password="aluno_fatec",
        database="argqor30_professor"  # ajuste se seu banco tiver outro nome
    )

def mostrar_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    print("Clientes cadastrados:")
    for cliente in clientes:
        print(cliente)
    cursor.close()
    conexao.close()

def exibir_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    print("Tabelas no banco:")
    for tabela in tabelas:
        print(f"- {tabela[0]}")
    cursor.close()
    conexao.close()

def buscar_clientes_por_nome(parte_nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    consulta = "SELECT * FROM Clientes WHERE nome LIKE %s"
    cursor.execute(consulta, ("%" + parte_nome + "%",))
    resultados = cursor.fetchall()
    print(f"Clientes com '{parte_nome}' no nome:")
    for cliente in resultados:
        print(cliente)
    cursor.close()
    conexao.close()

def buscar_funcionarios_detalhes(parte_nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = """
    SELECT 
        f.nome AS funcionario,
        p.nome AS projeto,
        t.descricao AS tarefa,
        t.status,
        t.prazo
    FROM Funcionarios f
    LEFT JOIN Equipes e ON f.id = e.funcionario_id
    LEFT JOIN Projetos p ON e.projeto_id = p.id
    LEFT JOIN Tarefas t ON f.id = t.funcionario_id AND p.id = t.projeto_id
    WHERE f.nome LIKE %s
    ORDER BY f.nome, p.nome, t.prazo
    """
    
    cursor.execute(consulta, ("%" + parte_nome + "%",))
    resultados = cursor.fetchall()

    if resultados:
        print(f"Funcionários com '{parte_nome}' no nome e seus projetos/tarefas:\n")
        for funcionario, projeto, tarefa, status, prazo in resultados:
            print(f"Funcionário: {funcionario}")
            print(f"  Projeto: {projeto if projeto else 'Nenhum'}")
            print(f"    Tarefa: {tarefa if tarefa else 'Sem tarefas atribuídas'}")
            if tarefa:
                print(f"    Status: {status} | Prazo: {prazo}")
            print("-" * 50)
    else:
        print("Nenhum resultado encontrado.")

    cursor.close()
    conexao.close()

print("\nConexão com Banco de Dados - Opções\n")
print("1 - Exibir Tabelas")
print("2 - Mostrar Clientes")
print("3 - Buscar Cliente por Nome")
print("4 - Buscar Funcionario")
print("0 - Sair do Programa\n")

op = int(input("Selecione uma opção: "))

while op != 0:
    if op == 0:
        exit()
    elif op == 1:
        exibir_tabelas()
        break
    elif op == 2:
        mostrar_clientes()
        break
    elif op == 3:
        val = input("Digite o nome do cliente: ")
        buscar_clientes_por_nome(val)
        break
    elif op == 4:
        val = input("Digite o nome do funcionário: ")
        buscar_funcionarios_detalhes(val)
        break
    else:
        print("Opção Inválida.")