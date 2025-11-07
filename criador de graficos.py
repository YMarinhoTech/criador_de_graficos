import matplotlib.pyplot as plt; import string

pessoas_notas = {}

while True:
    print("============== CRIAR GRAFICO ==============\n")
    
    try:
        choices = int(input("1) Adicionar dados comparativos\n2) Remover dados comparativos\n3) Comparar estatisticas\n4) Configurar Grafico e Finalizar\n"))
    except ValueError:
        print("Digite um número válido!")
        continue
    print()

    if choices == 1:
        while True: 
            nome_pessoa = input("ESCREVA o NOME da PESSOA ou\n0) para voltar no menu anterior\n").strip().lower()
            if nome_pessoa == "0":
                break
            elif nome_pessoa.isdigit() or all(c in string.punctuation for c in nome_pessoa):
                print("Nome inválido! Use apenas letras.\n")
                continue
            
            if nome_pessoa in pessoas_notas:
                print(f"A pessoa '{nome_pessoa}' já está cadastrada com nota {pessoas_notas[nome_pessoa]}.")
                atualizar = input("Deseja atualizar a nota? (s/n): ").strip().lower()
                if atualizar != 's':
                    continue

            try:
                nota = float(input(f"ADICIONE a NOTA de {nome_pessoa}:\n"))
            except ValueError:
                print("Digite um número válido!")
                continue
            print()
            
            
            pessoas_notas[nome_pessoa] = nota
            print(f"✓ Adicionado: {nome_pessoa} -> {nota}")
            print(f"\nPESSOAS E NOTAS:\n")
            for pessoa, nota_valor in pessoas_notas.items():
                print(f"  {pessoa}: {nota_valor}")
            print()

    
    elif choices == 2:
        while True:
            if not pessoas_notas:
                print("Nenhum dado cadastrado!\n")
                break
            
            print("\nPESSOAS CADASTRADAS:")
            for pessoa, nota in pessoas_notas.items():
                print(f"  {pessoa}: {nota}")
            print()
            
            remover_pessoa = input("DIGITE o NOME da pessoa para remover ou\n0) para voltar no menu anterior\n").strip().lower()
            
            if remover_pessoa == "0":
                break
            elif remover_pessoa in pessoas_notas:
                nota_removida = pessoas_notas.pop(remover_pessoa)
                print(f"✓ Removido: {remover_pessoa} (nota: {nota_removida})\n")
            else:
                print("PESSOA não encontrada na lista!\n")

    
    elif choices == 3:
        if not pessoas_notas:
            print("Informação incompleta! Nenhum dado cadastrado.\n")
        else:
            print("\n========== ESTATÍSTICAS ==========")
            print(f"Total de itens: {len(pessoas_notas)}")
            
            for pessoa, nota in pessoas_notas.items():
                print(f"  {pessoa}: {nota}")
            
            notas = list(pessoas_notas.values())
            print(f"\nMédia dos valores: {sum(notas) / len(notas):.2f}")
            print(f"Maior valor: {max(notas):.2f}")
            print(f"Menor valor: {min(notas):.2f}")
            print("==================================\n")

    elif choices == 4:
        if not pessoas_notas:
            print("Não há dados para criar o gráfico!\n")
            continue
        
        title = input("Escreva o TÍTULO do GRÁFICO:\n").strip()
        yname = input("Adicione a DESCRIÇÃO dos NÚMEROS (ex: Notas):\n").strip()
        xname = input("Adicione a DESCRIÇÃO dos DADOS (ex: Pessoas):\n").strip()
        
        pessoas = list(pessoas_notas.keys())
        notas = list(pessoas_notas.values())
        
        plt.figure(figsize=(8, 4.5))
        plt.bar(pessoas, notas, color='green')
        plt.xlabel(xname)
        plt.ylabel(yname)
        plt.title(title)
        plt.xticks(rotation=0, ha='right')
        plt.tight_layout()
        plt.show()
        break
    
    else:
        print("Opção inválida! Escolha entre 1 e 4.\n")

print("CODIGO FINALIZADO...")
