
import flask
import os
import tkinter


variavel = "É uma string"


def funcaoSoma(a, b):
    c = a+b
    return c


def executaAlgoSemParametro():
    print("Mensagem Qualquer")
    return


if __name__ == '__main__':
    print("Python")
    print(variavel)
    print(funcaoSoma(5, 8))
    executaAlgoSemParametro()
