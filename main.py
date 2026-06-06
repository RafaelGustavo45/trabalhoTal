print("Tarefa 7: Sala de aula (Versão Dicionários)")

alunos = []

# --- FUNÇÕES DE ESTATÍSTICA ---

def menor_valor(lista):
    aluno_min = min(lista, key=lambda x: x['media'])
    return f"{aluno_min['media']:.2f} (Aluno: {aluno_min['nome']})"

def maior_valor(lista):
    aluno_max = max(lista, key=lambda x: x['media'])
    return f"{aluno_max['media']:.2f} (Aluno: {aluno_max['nome']})"

def media_geral(lista):
    soma_medias = sum(aluno['media'] for aluno in lista)
    return soma_medias / len(lista)

def taxa_aprovados(lista):
    aprovados = sum(1 for aluno in lista if aluno['situacao'] == "Aprovado")
    return (aprovados / len(lista)) * 100

def quantidade_por_situacao(lista):
    stats = {"Aprovado": 0, "Reprovado": 0, "Recuperação": 0, "Pendente": 0}
    for aluno in lista:
        stats[aluno['situacao']] += 1
    return f"\nAprovados: {stats['Aprovado']}\nReprovados: {stats['Reprovado']}\nEm recuperação: {stats['Recuperação']}\nPendentes: {stats['Pendente']}"

# --- FUNÇÕES DE UTILIDADE ---

def listarNumerado(lista):
    if not lista:
        print("\n--- Nenhum aluno cadastrado ---")
        return False
    for i, e in enumerate(lista, 1):
        print(f"{i}. {e['nome']}")
    return True

def listarRecuperacao(lista):
    return [aluno for aluno in lista if aluno['situacao'] == "Recuperação"]

def calcular_nota_recuperacao(media_semestre, media_minima=7.0):
    nota_necessaria = (media_minima * 2) - media_semestre
    return max(0, min(10, nota_necessaria))

def ordenar_pela_nota(lista):
    return sorted(lista, key=lambda aluno: aluno['media'], reverse=True)

# --- LOOP PRINCIPAL ---

while True:
    print("\n--- MENU ---")
    print("1- Cadastrar aluno | 2- Registrar notas | 3- Listar | 4- Sair | 5- Estatísticas | 6- Simular Recup. | 7- Ordenar pela nota")

    try:
        op = int(input("Digite a opção: "))
    except ValueError: 
        continue

    if op == 4: 
        break

    if op == 1:
        nome = input("Digite o nome: ").strip()
        if any(a['nome'].lower() == nome.lower() for a in alunos):
            print("Erro: Este aluno já está cadastrado!")
        else:
            alunos.append({
                'nome': nome, 
                'notas': [0.0, 0.0, 0.0], 
                'media': 0.0, 
                'situacao': "Pendente"
            })
            print(f"Aluno {nome} cadastrado!")

    elif op == 2:
        if listarNumerado(alunos):
            idx = int(input("Selecione o número: ")) - 1
            if 0 <= idx < len(alunos):
                notas = []
                for i in range(1, 4):
                    while True:
                        n = float(input(f"Nota {i} (0-10): "))
                        if 0 <= n <= 10:
                            notas.append(n); break
                
                media = sum(notas) / len(notas)
                situacao = "Aprovado" if media >= 7 else ("Recuperação" if media >= 5 else "Reprovado")
                
                alunos[idx].update({'notas': notas, 'media': media, 'situacao': situacao})
                print(f"Média: {media:.2f} ({situacao})")

    elif op == 3:
        print(f"\n{'Nome':<15} | {'Média':<6} | {'Situação'}")
        for a in alunos:
            print(f"{a['nome']:<15} | {a['media']:<6.2f} | {a['situacao']}")

    elif op == 5:
        if alunos:
            print("\n--- ESTATÍSTICAS ---")
            print("Menor média:", menor_valor(alunos))
            print("Maior média:", maior_valor(alunos))
            print(f"Média geral: {media_geral(alunos):.2f}")
            print(quantidade_por_situacao(alunos))
            print(f"Taxa de aprovados: {taxa_aprovados(alunos):.2f}%")

    elif op == 6:
        alunos_rec = listarRecuperacao(alunos)
        if alunos_rec:
            listarNumerado(alunos_rec)
            idx = int(input("Selecione: ")) - 1
            aluno = alunos_rec[idx]
            print(f"Para {aluno['nome']}, precisa de: {calcular_nota_recuperacao(aluno['media']):.2f}")

    elif op == 7:
        for a in ordenar_pela_nota(alunos):
            print(f"{a['nome']:<15} | {a['media']:<6.2f}")
