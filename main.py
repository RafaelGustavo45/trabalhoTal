print("Tarefa 7: Diário de Classe e Boletim Escolar (Versão Dicionários)")

alunos = []

#  FUNÇÕES DE ESTATÍSTICA 

def calcular_media_reutilizavel(notas):
    return sum(notas) / len(notas) if notas else 0.0

def menor_valor(lista):
    validos = [a for a in lista if a['situacao'] != "Pendente"]
    if not validos: return "Nenhum aluno com notas registradas."
    aluno_min = min(validos, key=lambda x: x['media'])
    return f"{aluno_min['media']:.1f} (Aluno: {aluno_min['nome']})"

def maior_valor(lista):
    validos = [a for a in lista if a['situacao'] != "Pendente"]
    if not validos: return "Nenhum aluno com notas registradas."
    aluno_max = max(validos, key=lambda x: x['media'])
    return f"{aluno_max['media']:.1f} (Aluno: {aluno_max['nome']})"

def media_geral(lista):
    validos = [a for a in lista if a['situacao'] != "Pendente"]
    if not validos: return 0.0
    soma_medias = sum(aluno['media'] for aluno in validos)
    return soma_medias / len(validos)

def taxa_aprovados(lista):
    validos = [a for a in lista if a['situacao'] != "Pendente"]
    if not validos: return 0.0
    aprovados = sum(1 for aluno in validos if aluno['situacao'] == "Aprovado")
    return (aprovados / len(validos)) * 100

def quantidade_por_situacao(lista):
    stats = {"Aprovado": 0, "Reprovado": 0, "Recuperação": 0, "Reprovado por Falta": 0, "Pendente": 0}
    for aluno in lista:
        stats[aluno['situacao']] += 1
    return f"Aprovados: {stats['Aprovado']}\nReprovados: {stats['Reprovado']}\nEm recuperação: {stats['Recuperação']}\nReprovados por Falta: {stats['Reprovado por Falta']}\nPendentes: {stats['Pendente']}"

#  FUNÇÕES DE UTILIDADE E ORDENAÇÃO 

def buscar_aluno_por_nome(lista, nome_busca):
    for aluno in lista:
        if aluno['nome'].lower() == nome_busca.lower():
            return aluno
    return None

def atualizar_situacao(aluno):
    # Bônus 1: Validação de Frequência (20 aulas no total, limite de 25% de faltas = 5 faltas)
    if aluno['faltas'] > 5:
        aluno['situacao'] = "Reprovado por Falta"
    else:
        media = aluno['media']
        if media >= 7.0:
            aluno['situacao'] = "Aprovado"
        elif 5.0 <= media < 7.0:
            aluno['situacao'] = "Recuperação"
        else:
            aluno['situacao'] = "Reprovado"

def bubble_sort_ranking(lista):
    
    lista_ordenada = list(lista)
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]['media'] < lista_ordenada[j + 1]['media']:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada

while True:
    print("\n MENU DIÁRIO DE CLASSE ")
    print("1 - Cadastrar aluno")
    print("2 - Registrar notas e faltas")
    print("3 - Listar alunos e médias")
    print("4 - Estatísticas da turma")
    print("5 - Alunos em recuperação")
    print("6 - Simular / Registrar nota de recuperação")
    print("7 - Ranking da turma (Bubble Sort)")
    print("8 - Aplicar curva de notas (+1 Ponto Bônus)")
    print("9 - Sair")

    try:
        op = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    if op == 9:
        print("Encerrando o programa...")
        break

    # Parte 1 -> Cadastrar Aluno
    if op == 1:
        nome = input("Digite o nome do aluno: ").strip()
        if not nome:
            print("Erro: O nome não pode ser vazio.")
        elif buscar_aluno_por_nome(alunos, nome):
            print("Erro: Este aluno já está cadastrado!")
        else:
            alunos.append({
                'nome': nome,
                'notas': [],
                'media': 0.0,
                'faltas': 0,
                'situacao': "Pendente"
            })
            print(f"Aluno '{nome}' cadastrado com sucesso!")

    # Parte 2 -< Registrar Notas e Faltas 
    elif op == 2:
        nome_busca = input("Digite o nome do aluno para registrar dados: ").strip()
        aluno = buscar_aluno_por_nome(alunos, nome_busca)
        
        if not aluno:
            print("Erro: Aluno não encontrado!")
        else:
            # Registro de notas
            novas_notas = []
            print(f"Registrando as 3 notas para {aluno['nome']}:")
            for i in range(1, 4):
                while True:
                    try:
                        n = float(input(f"Nota {i} (0.0 - 10.0): "))
                        if 0.0 <= n <= 10.0:
                            novas_notas.append(n)
                            break
                        else:
                            print("Nota inválida! Deve ser entre 0.0 e 10.0.")
                    except ValueError:
                        print("Entrada inválida! Digite um número decimal.")
            
            # Registro de faltas
            while True:
                try:
                    faltas = int(input("Digite o total de faltas (Total de 20 aulas): "))
                    if 0 <= faltas <= 20: 
                        aluno['faltas'] = faltas
                        break
                    else:
                        print("O número de faltas não é válido.")
                except ValueError:
                    print("Entrada inválida! Digite um número inteiro.")

            aluno['notas'] = novas_notas
            aluno['media'] = calcular_media_reutilizavel(novas_notas)
            atualizar_situacao(aluno)
            print(f"Dados atualizados! Média: {aluno['media']:.1f} | Situação: {aluno['situacao']}")

    # Parte 3 -> Listar Alunos e Médias
    elif op == 3:
        if not alunos:
            print("\n Nenhum aluno cadastrado ")
        else:
            print(f"\n{'Nome':<15} | {'Nota 1':<6} | {'Nota 2':<6} | {'Nota 3':<6} | {'Média':<6} | {'Faltas':<6} | {'Situação'}")
            print("-" * 75)
            for a in list(alunos):
                if a['situacao'] == "Pendente":
                    print(f"{a['nome']:<15} | {'-':<6} | {'-':<6} | {'-':<6} | {'-':<6} | {a['faltas']:<6} | {a['situacao']}")
                else:
                    print(f"{a['nome']:<15} | {a['notas'][0]:<6.1f} | {a['notas'][1]:<6.1f} | {a['notas'][2]:<6.1f} | {a['media']:<6.1f} | {a['faltas']:<6} | {a['situacao']}")

    # Parte 4 -> Estatísticas da Turma 
    elif op == 4:
        # Validação alunos que n possuem 3 notas
        pendentes = [a for a in alunos if a['situacao'] == "Pendente"]
        if pendentes:
            print("\n[AVISO]: Os seguintes alunos não possuem 3 notas e serão ignorados nas estatísticas:")
            for p in pendentes:
                print(f"- {p['nome']}")
        
        validos = [a for a in alunos if a['situacao'] != "Pendente"]
        if not validos:
            print("\n Nenhuma estatística disponível (nenhum aluno com notas completas) ")
        else:
            print("\n ESTATÍSTICAS DA TURMA ")
            print("Maior média: ", maior_valor(alunos))
            print("Menor média: ", menor_valor(alunos))
            print(f"Média geral da turma: {media_geral(alunos):.1f}")
            print(f"Taxa de aprovação: {taxa_aprovados(alunos):.1f}%")
            print("\nQuantidade por situação:")
            print(quantidade_por_situacao(alunos))

    # Parte 5 -< Listar apenas Alunos em Recuperação
    elif op == 5:
        em_recuperacao = [a for a in alunos if a['situacao'] == "Recuperação"]
        if not em_recuperacao:
            print("\n Não há alunos em situação de recuperação ")
        else:
            print(f"\n ALUNOS EM RECUPERAÇÃO (Média entre 5.0 e 6.9) ")
            print(f"{'Nome':<15} | {'Média Final':<11}")
            print("-" * 30)
            for a in em_recuperacao:
                print(f"{a['nome']:<15} | {a['media']:<11.1f}")

    # Parte 6 -> Simular/Registrar Nota de Recuperação
    elif op == 6:
        em_recuperacao = [a for a in alunos if a['situacao'] == "Recuperação"]
        if not em_recuperacao:
            print("\nErro: Não existem alunos em recuperação disponíveis para esta ação.")
        else:
            print("\nSelecione um dos alunos em recuperação listados abaixo:")
            for idx, a in enumerate(em_recuperacao, 1):
                print(f"{idx}. {a['nome']} (Média atual: {a['media']:.1f})")
            
            try:
                escolha = int(input("Digite o número do aluno: ")) - 1
                if 0 <= escolha < len(em_recuperacao):
                    aluno_selecionado = em_recuperacao[escolha]
                    
                    while True:
                        try:
                            nota_rec = float(input(f"Digite a nota da recuperação para {aluno_selecionado['nome']} (0-10): "))
                            if 0.0 <= nota_rec <= 10.0:
                                break
                            print("Nota inválida! Deve ser entre 0.0 e 10.0.")
                        except ValueError:
                            print("Entrada inválida!")

                    nova_media = (aluno_selecionado['media'] + nota_rec) / 2
                    aluno_selecionado['media'] = nova_media
                    
                    atualizar_situacao(aluno_selecionado)
                    print(f"\nDados atualizados para {aluno_selecionado['nome']}!")
                    print(f"Nova Média: {aluno_selecionado['media']:.1f} | Nova Situação: {aluno_selecionado['situacao']}")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Entrada inválida!")

    # Parte 7 -> Ranking da Turma  Bubble Sort
    elif op == 7:
        if not alunos:
            print("\n Nenhum aluno cadastrado para gerar o ranking ")
        else:
            # Executa a ordenação manual
            ranking = bubble_sort_ranking(alunos)
            print(f"\n RANKING DA TURMA ")
            print(f"{'Posição':<8} | {'Nome':<15} | {'Média Final':<11} | {'Situação'}")
            print("-" * 50)
            for pos, a in enumerate(ranking, 1):
                media_exibicao = f"{a['media']:.1f}" if a['situacao'] != "Pendente" else "-"
                print(f"{pos:<8} | {a['nome']:<15} | {media_exibicao:<11} | {a['situacao']}")

    # Parte 8-> Bônus 2: Curva de Notas (+1 Ponto Bônus)
    elif op == 8:
        if not alunos:
            print("\n Nenhum aluno cadastrado para aplicar o bônus ")
        else:
            print("\n APLICANDO CURVA DE NOTAS (+1.0 PONTO bônus) ")
            for a in alunos:
                if a['situacao'] != "Pendente" and a['situacao'] != "Reprovado por Falta":
                    media_anterior = a['media']
                    
                    a['media'] = min(10.0, a['media'] + 1.0)
                    atualizar_situacao(a)
                    print(f"Aluno: {a['nome']:<15} | Média Anterior: {media_anterior:.1f} -> Nova Média: {a['media']:.1f} ({a['situacao']})")
                elif a['situacao'] == "Reprovado por Falta":
                    print(f"Aluno: {a['nome']:<15} | Ignorado (Reprovado por Falta)")
                else:
                    print(f"Aluno: {a['nome']:<15} | Ignorado (Notas não registradas)")
            print("\nBônus aplicado com sucesso com respeito ao teto de 10.0!")
    else:
        print("Opção inválida! Escolha um número entre 1 e 9.")
