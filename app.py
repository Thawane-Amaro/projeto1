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
        print("3- Ativar restaurante")
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
    print(texto)
    print()


def cadastra_novo_restaurante():
     os.system("cls")
     print("cadastro de novos restaurantes\n")
     nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar:")
     restaurantes.append(nome_do_restaurante)
     print(f"o restaurante{nome_do_restaurante} foi cadastrado com sucesso!")
     voltar_ao_menu_principal()
     main()

def listar_restaurantes():
    exibir_subtitulo("listando os restaurantes")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        print(f"  - {nome_restaurante}")


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