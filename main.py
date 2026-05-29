print("Tarefa 7: Sala de aula")

alunos = []

def estatisticas(lista):
    print("\n--- ESTATÍSTICAS DA TURMA ---")

    if not lista:
            print("Nenhum aluno cadastrado.")
            return

    medias = []

    for aluno in lista:
        medias.append(aluno[4])

        print(f"Menor média : {menor_valor(medias):.2f}")
        print(f"Maior média : {maior_valor(medias):.2f}")
        print(f"Média geral : {media_geral(medias):.2f}")

        aprovados, recuperacao, reprovados = quantidade_por_situacao(lista)

        print(f"Aprovados   : {aprovados}")
        print(f"Recuperação : {recuperacao}")
        print(f"Reprovados  : {reprovados}")


def menor_valor(lista):
    menor_nota = lista[0]
    
    for nota in lista:
        if nota < menor_nota:
            menor_nota = nota
    return menor_nota

def maior_valor(lista):
    maior_nota = lista[0]

    for nota in lista:
        if nota > maior_nota:
            maior_nota = nota

    return maior_nota

def media_geral(lista):
    soma = 0
    
    for n in lista:
        soma += n

    return soma / len(lista)

def quantidade_por_situacao(lista):
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for aluno in lista:
        if aluno[5] == "Aprovado":
            aprovados += 1

        elif aluno[5] == "Recuperação":
            recuperacao += 1
        
        elif aluno[5] == "Reprovado":
            reprovados += 1

    return aprovados, recuperacao, reprovados


def listarNumerado(lista):
    if not lista:
        print("\n--- Nenhun aluno cadastrado ---")
        return False
    i = 1
    for e in lista:
        print(f"{i}. {e[0]}")
        i += 1
    return True
#Ranking da turma (ordenar 
# alunos por média final, do maior para o menor; ordenação manual; mostrar posição, nome e média).
def raking_da_turma(lista):
    

while True:
    print("\n--- MENU ---")
    print("1- Cadastrar aluno")
    print("2- Registrar notas de um aluno")
    print("3- Listar alunos e médias")
    print("4- Estatísticas da turma ")
    print("9- Sair.")
    

    try:
        op = int(input("Digite a opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if op == 9:
        print("Desligando...")
        break

    if op == 1:
        nome = input("Digite o nome: ").strip()
        
        # Verificação de duplicata (case-insensitive)
        existe = False
        for a in alunos:
            if a[0].lower() == nome.lower():
                existe = True
                break
        
        if existe:
            print("Erro: Este aluno já está cadastrado!")
        else:
            # Inicializa com notas e média zero
            alunos.append([nome, 0.0, 0.0, 0.0, 0.0, "Pendente"])
            print(f"Aluno {nome} cadastrado com sucesso!")

    elif op == 2:
        if listarNumerado(alunos):
            try:
                idx = int(input("Selecione o número do aluno: ")) - 1
                if 0 <= idx < len(alunos):
                    notas = []
                    for i in range(1, 4):
                        while True:
                            n = float(input(f"Digite a nota {i} (0 a 10): "))
                            if 0 <= n <= 10:
                                notas.append(n)
                                break
                            else:
                                print("Nota inválida! Digite um valor entre 0 e 10.")
                    
                    # Processamento dos dados
                    media = sum(notas) / 3
                    
                    if media >= 7:
                        situacao = "Aprovado"
                    elif 5 <= media < 7:
                        situacao = "Recuperação"
                    else:
                        situacao = "Reprovado"
                    
                    # Atualiza a sub-lista do aluno
                    alunos[idx][1] = notas[0]
                    alunos[idx][2] = notas[1]
                    alunos[idx][3] = notas[2]
                    alunos[idx][4] = media
                    alunos[idx][5] = situacao
                    
                    print(f"Notas registradas! Média: {media:.2f} ({situacao})")
                else:
                    print("Índice inválido!")
            except ValueError:
                print("Entrada inválida. Operação cancelada.")

    elif op == 3:
        if not alunos:
            print("\nLista vazia.")
        else:
            print("\n--- RELATÓRIO ALUNOS ---")
            print(f"{'Nome':<15} | {'N1':<5} | {'N2':<5} | {'N3':<5} | {'Média':<6} | {'Situação'}")
            print("-" * 60)
            for a in alunos:
                print(f"{a[0]:<15} | {a[1]:<5.1f} | {a[2]:<5.1f} | {a[3]:<5.1f} | {a[4]:<6.2f} | {a[5]}")

    elif op == 4:
        if not alunos:
            print("\nLista vazia.")
        else:
            #estatisticas da turma
            estatisticas(aluno)
            print("")
    
    else:
        print("Opção inválida!")
        
        


   



    








