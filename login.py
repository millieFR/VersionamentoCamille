import re
logins = []

def verificar_login():
    while True:
        regex = (r'^[a-zA-Z0-9._%+-] +@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}$')
        
        login =  input("Digite o seu login: ")
        regex = re.match(login, regex)
        if login == regex:
          if  login in logins:
            print(f'Login ja existe {login}')
        elif login !=  regex:
           print('Login invalido')
        else:
           print('Login criado com sucesso')
           login.append(logins)
           print(login)
verificar_login()
       
'''senha = input('Digite sua senha: ')
        if len(senha) >= 8 and any(char.isdigit() for char in senha) and any(char.islower() for char in senha) and any(char.isupper() for char in senha):
            con = input('Confirme a senha:')
            if senha in senha:
                print('Senha e login valídos')
            elif senha != senha:
             print('Senha Invalída')
break
    else:
          print('Senha inválida. Crie uma que senha deve conter pelo menos 8 caracteres, um dígito ou mais, uma letra minúscula e uma letra maiúscula.')
        verificar_login()'''