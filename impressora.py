from time import sleep
import impressora

print("Cadastro de login e senha")
cadastrar_login = str(input("Cadatrar login: "))
cadastrar_senha = str(input("Cadatrar senha: "))
print("-+" * 20)
login = str(input("Login: "))
senha = str(input("Senha: "))

if cadastrar_login == login and cadastrar_senha == senha:
    print("Acesso liberado")
while cadastrar_senha != senha or cadastrar_login != login:
    print("Cadastro ou senha errada")
    login = str(input("Login: "))
    senha = str(input("Senha: "))
    print ('___'*12)
    sleep(3)

impressora.AbreConexaoImpressora (1 ,'i8' , 'USB', 0)
if impressora.AbreConexaoImpressora != 0:
    print("Deu erro na conexão.")

def exibir_menu():
    print("1 - Imprimir um texto")
    print("2 - Imprimir um QR Code")
    print("3 - Imprimir um XML SAT")
    print("4 - Fechar o sistema")

def main():
    while True:
        impressora.AbreConexaoImpressora(1 ,'i8' , 'USB', 0)
        while True:
            exibir_menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                texto = input("Digite o texto a ser impresso: ")                    
                print(impressora.ImpressaoTexto(texto,1,0,17))
                impressora.AvancaPapel(2)
                impressora.Corte(5)
            elif opcao == "2":
                qr_code = input("Digite o QR Code a ser impresso: ")
                print(impressora.ImpressaoQRCode(qr_code,5, 3))                    
                impressora.Corte(5)
            elif opcao == "3":
                print(impressora.ImprimeXMLSAT('path=XMLSAT.xml',0))    
                impressora.AvancaPapel(2)
                impressora.Corte(5)            
            elif opcao == "4":
                confirmacao = input("Tem certeza que deseja fechar o sistema? (S/N): ")
                if confirmacao.upper() == "S":
                    impressora.FechaConexaoImpressora()
                    break
                elif confirmacao.upper() == "N":
                    continue
            else:
                print("Opção inválida")
        break

main()