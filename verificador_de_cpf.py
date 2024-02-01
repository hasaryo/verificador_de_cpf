import random

while True:

    pergunta = input('Você deseja gerar um CPF ou validar um existente?: [g]erar [v]alidar: ')

    if pergunta.startswith('v'):

        cpf = input('Digite o CPF (somente números): ')

        # Verifica se o campo digitado contém somente números e se tem a quantidade de números correta.
        if cpf.isdigit():
            if len(cpf) < 11 or len(cpf) > 11:
                print('Digite um CPF válido.')
                continue
        else: 
            print('Digite somente números.')
            continue

        # Verifica se todos os dígitos são iguais.
        if len(set(cpf)) == 1:
            print('CPF inválido. Todos os dígitos são iguais.')
            continue

        # Verifica o primeiro dígito.

        cpf_9primeiros = cpf[:9]
        multi = 10
        soma = 0

        for i, digito in enumerate(cpf_9primeiros):
            soma += int(digito) * multi
            multi -= 1
            if multi == 1:
                break
            
        
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto == int(cpf[9]):
            print('Primeiro digito é valido.')
        else:
            print('CPF inválido.')
            continue
        

        # Verifica o segundo dígito. 

        multi = 11
        soma = 0

        cpf_10primeiros = cpf[:10]
        for i, digito in enumerate(cpf_10primeiros):
            soma += int(digito) * multi
            multi -= 1
            if multi == 1:
                break
        resto = (soma * 10) % 11
        if resto > 9:
            resto = 0
        if resto == int(cpf[10]):
            print('O segundo digito é válido. CPF aprovado.')
        else:
            print('O segundo digito não é válido. CPF inválido.')
    
    elif pergunta.startswith('g'):
        nove_digitos = []

        for _ in range(9):
            gerado = random.randint(0,9)
            nove_digitos.append(str(gerado))
        
        resultado = ''.join(nove_digitos)


        # Gera o penúltimo digito.

        multi = 10
        soma = 0

        for i, digito in enumerate(resultado):
            soma += int(digito) * multi
            multi -= 1
            if multi == 1:
                break
            
        
        resto = (soma * 10) % 11
        if resto > 9:
            resto = 0
        

        # Gera o último digito. 

        multi = 11
        soma = 0

        cpf_10primeiros = resultado + str(resto)
        for i, digito in enumerate(cpf_10primeiros):
            soma += int(digito) * multi
            multi -= 1
            if multi == 1:
                break
        resto = (soma * 10) % 11
        if resto > 9:
            resto = 0
        final = cpf_10primeiros + str(resto)
        print(f'Seu CPF gerado é: {final}')

    else:
        print('Inválido.')
