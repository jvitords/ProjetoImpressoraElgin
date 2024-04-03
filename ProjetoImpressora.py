import os
import ctypes
import platform
'''
print("-=" * 20)
cadastro_usuario = input("Cadastre seu usuário: ")
print("-=" * 20)
cadastro_senha = input("Cadastre sua senha: ")
print("-=" * 20)
print("CADASTRADO COM SUCESSO")

os.system('cls')

print("LOGIN: \n")
usuario = input("Digite o usuário: ")
senha = input("Digite sua senha: ")

while cadastro_usuario != usuario or cadastro_senha != senha:
    print("Usuário ou senha incorreta.")
    usuario = input("Digite o usuário: ")
    senha = input("Digite sua senha: ")
if cadastro_usuario == usuario or cadastro_senha == senha:
    print("=-" * 30)
    print("SEJA BEM VINDO")
    print("-=" * 20)
'''


if platform.system() == "Windows":
    ffi = ctypes.WinDLL("./E1_Impressora01.dll")
else:
    ffi = ctypes.cdll.LoadLibrary("./libE1_Impressora.so")

def AbreConexaoImpressora(tipo, modelo, conexao, param):
    fn = ffi.AbreConexaoImpressora
    fn.restype = ctypes.c_int
    fn.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]

    modelo = ctypes.c_char_p(bytes(modelo, "utf-8"))
    conexao = ctypes.c_char_p(bytes(conexao, "utf-8"))

    return fn(tipo, modelo, conexao, param)

AbreConexaoImpressora()