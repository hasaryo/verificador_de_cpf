while True:

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
        
    print(soma)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto == int(cpf[9]):
        print('Primeiro digito é valido.')
    else:
        print('CPF inválido.')
        continue
    print(resto)

    # Verifica o segundo dígito. 

    multi = 11
    soma = 0

    cpf_10primeiros = cpf[:10]
    print(cpf_10primeiros)
    for i, digito in enumerate(cpf_10primeiros):
        soma += int(digito) * multi
        multi -= 1
        if multi == 1:
            break
    print(soma)
    resto = (soma * 10) % 11
    if resto > 9:
        resto = 0
    print(resto)
    print(int(cpf[10]))
    if resto == int(cpf[10]):
        print('O segundo digito é válido. CPF aprovado.')
    else:
        print('O segundo digito não é válido. CPF inválido.')



