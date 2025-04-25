import os
restaurantes=[{"nome": "doce da vovo", "categoria": "doce", "ativo": False},
{"nome": "mundo do doce", "categoria": "doce", "ativo": True},
{"nome": "macarrone", "categoria": "massa" , "ativo": False}
] 
def exibir_nome_do_progama():
    print ("restaurante")
def exibir_opçoes():
        print("1- Cadastrar restaurante")
        print("2- Listar restaurante")
        print("3- alterar estado de restaurante") 
        print("4- Sair\n")

def Encerrando_programa():
    os.system("cls")
    print("Encerrando o programa")
    
def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


def opçao_invalida():
   print("Opiçao invalida!\n")
   voltar_ao_menu_principal()
   main()
 
def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto))
    print (linha)
    print(texto)
    print(linha)
    print()

def alterar_restaurante():
    exibir_subtitulo("alterando estado do restaurante")
    nome_restaurante_=input("digite o nome do restaurante que deseja alterar o estado:")
    restaurante_encontrado= False

    for restaurante in restaurantes: 
       if nome_restaurante_ == restaurante ["nome"] :
           restaurante_encontrado = True
           restaurante["ativo"] = not restaurante["ativo"]
           mensagem = f" o restaurante {nome_restaurante_} foi ativado com sucesso" if restaurante ['ativo'] else f" o restaurante {nome_restaurante_}foi desativado com sucesso"
           print (mensagem)

     
       if   not restaurante_encontrado:
         print ("o restaurante nao foi encontrado")

         voltar_ao_menu_principal()
       





def cadastra_novo_restaurante():
     os.system("cls")
     print("cadastro de novos restaurantes\n")
     nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar:")
     categoria = input('digite o nome da categoria do restaurante {nome_do_restaurante}:')
     dados_do_restaurante = {nome_do_restaurante,"categoria", categoria,"ativo" ,False}
     restaurantes.append(nome_do_restaurante)
     print(f"o restaurante{nome_do_restaurante} foi cadastrado com sucesso!")
     voltar_ao_menu_principal()
     main()

def listar_restaurantes():
    exibir_subtitulo("listando os restaurantes")
  Print (f'{"Nome do restaurante".ljust(22)} | {'categoria}'.ljust(20)} | status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante['categoria']
        ativo = "ativo" if restaurante ["ativo"] else "desativado"
        print(f'  - {nome_restaurante.ijust(20)} | {categoria.ijust(20)} | {ativo}')

    voltar_ao_menu_principal()
    main()


def escolher_opçoes():
    try:
        item_selecionado = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção: {item_selecionado}\n")

        if item_selecionado == 1:
          cadastra_novo_restaurante ()
        elif item_selecionado == 2:
           listar_restaurantes()
        elif item_selecionado == 3: 
            print("Ativar restaurantes")
        elif item_selecionado == 4:
            Encerrando_programa()
        else:
            opçao_invalida()
    except:
         opçao_invalida()
            

def main():
        os.system("cls")
        exibir_nome_do_progama()
        exibir_opçoes()
        escolher_opçoes()

if __name__ == "__main__":
    main() 