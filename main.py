print("Tarefa 7: Sala de aula")

alunos = []

# --- FUNÇÕES DE ESTATÍSTICA ---

def menor_valor(lista):
    # Encontra o aluno com a menor média
    # O parâmetro 'key' diz para o min() comparar o índice 4 (média) de cada sub-lista
    aluno_min = min(lista, key=lambda x: x[4])
    return f"{aluno_min[4]:.2f} (Aluno: {aluno_min[0]})"

def maior_valor(lista):
    # Encontra o aluno com a maior média
    aluno_max = max(lista, key=lambda x: x[4])
    return f"{aluno_max[4]:.2f} (Aluno: {aluno_max[0]})"

def media_geral(lista):
    # Soma todas as médias (índice 4) e divide pelo total de alunos
    soma_medias = sum(aluno[4] for aluno in lista)
    return soma_medias / len(lista)

def taxa_aprovados(lista):
    aprovados = 0
    total = len(lista)

    for aluno in lista:
        situacao= aluno[5]
        if situacao == "Aprovado":
            aprovados += 1


    return (aprovados/total)*100
            

def quantidade_por_situacao(lista):
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    pendente = 0

    for aluno in lista:
        situacao = aluno[5]
        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Reprovado":
            reprovados += 1
        elif situacao == "Recuperação":
            recuperacao += 1
        elif situacao == "Pendente":
            pendente += 1
         
    return f"\nAprovados: {aprovados}\nReprovados: {reprovados}\nEm recuperação: {recuperacao}\nPendentes: {pendente}"

# --- FUNÇÕES DE UTILIDADE ---

def listarNumerado(lista):
    if not lista:
        print("\n--- Nenhum aluno cadastrado ---")
        return False
    i = 1
    for e in lista:
        print(f"{i}. {e[0]}")
        i += 1
    return True

def listarRecuperacao(lista):
    
    lista_recuperacao = []
    for aluno in lista:
        situacao = aluno[5]
        nome = aluno[0]
        media = aluno[4]
        if situacao == "Recuperação":
          lista_recuperacao.append([nome, media])
    
    return lista_recuperacao

# Programa para calcular a nota necessária na recuperação

def calcular_nota_recuperacao(media_semestre, media_minima=7.0):
    if not (0 <= media_semestre <= 10):
        raise ValueError("A média do semestre deve estar entre 0 e 10.")
    
    nota_necessaria = (media_minima * 2) - media_semestre
    
    # Garante que a nota esteja no intervalo válido
    return max(0, min(10, nota_necessaria))



# --- LOOP PRINCIPAL ---

while True:
    print("\n--- MENU ---")
    print("1- Cadastrar aluno")
    print("2- Registrar notas")
    print("3- Listar alunos e médias")
    print("4- Sair.")
    print("5- Estatísticas da turma")
    print("6- Alunos em recuperacao")
    print("7- Simular nota de recuperacao")


    try:
        op = int(input("Digite a opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if op == 4:
        print("Desligando...")
        break

    if op == 1:
        nome = input("Digite o nome: ").strip()
        existe = any(a[0].lower() == nome.lower() for a in alunos)
        
        if existe:
            print("Erro: Este aluno já está cadastrado!")
        else:
            alunos.append([nome, 0.0, 0.0, 0.0, 0.0, "Pendente"])
            print(f"Aluno {nome} cadastrado!")

    elif op == 2:
        if listarNumerado(alunos):
            try:
                idx = int(input("Selecione o número: ")) - 1
                if 0 <= idx < len(alunos):
                    notas = []
                    for i in range(1, 4):
                        while True:
                            n = float(input(f"Nota {i} (0-10): "))
                            if 0 <= n <= 10:
                                notas.append(n)
                                break
                            print("Nota inválida!")
                    
                    media = sum(notas) / 3
                    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
                    
                    alunos[idx][1], alunos[idx][2], alunos[idx][3] = notas
                    alunos[idx][4], alunos[idx][5] = media, situacao
                    print(f"Média: {media:.2f} ({situacao})")
            except ValueError:
                print("Entrada inválida.")

    elif op == 3:
        if not alunos:
            print("\nLista vazia.")
        else:
            print(f"\n{'Nome':<15} | {'Média':<6} | {'Situação'}")
            print("-" * 40)
            for a in alunos:
                print(f"{a[0]:<15} | {a[4]:<6.2f} | {a[5]}")

    elif op == 5:
        if not alunos:
            print("\nNão há dados para gerar estatísticas.")
        else:
            print("\n--- ESTATÍSTICAS DA TURMA ---")
            print("Menor média: ", menor_valor(alunos))
            print("Maior média: ", maior_valor(alunos))
            print(f"Média geral:  {media_geral(alunos):.2f}")
            print(quantidade_por_situacao(alunos))
            print(f"taxa de aprovados {taxa_aprovados(alunos):.2f}%")

    elif op ==6:
        print("alunos em recuperacao: ")
        print(listarRecuperacao(alunos))

    elif op == 7:
        # 1. Obtemos a lista apenas de quem está em recuperação
        alunos_rec = listarRecuperacao(alunos)
        
        if not alunos_rec:
            print("\nNão há alunos em recuperação no momento.")
        else:
            print("\n--- SIMULAÇÃO DE RECUPERAÇÃO ---")
            # 2. Mostramos a lista numerada para seleção
            listarNumerado(alunos_rec)
            
            try:
                escolha = int(input("Selecione o número do aluno para simular: ")) - 1
                
                if 0 <= escolha < len(alunos_rec):
                    # alunos_rec[escolha] retorna [nome, media]
                    nome_aluno = alunos_rec[escolha][0]
                    media_atual = alunos_rec[escolha][1]
                    
                    # 3. Chamamos a função de cálculo
                    nota_precisa = calcular_nota_recuperacao(media_atual)
                    
                    print(f"\nO aluno {nome_aluno} tem média {media_atual:.2f}")
                    print(f"Para atingir a média final 7.0, ele precisa tirar {nota_precisa:.2f} na prova de recuperação.")
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número inteiro.")






    else:
        print("Opção inválida!")