
"""
Revising Oriented Object Coding(POO)
"""
from abc import *

class Person(ABC, object):

    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
        self.speaking = 0

    @abstractmethod
    def get_nome(self):
        print(self.__nome)

    @abstractmethod
    def set_nome(self, n):
        self.__nome = n

    @abstractmethod
    def get_idade(self):
        return self.__idade

    @abstractmethod
    def set_idade(self, ida):
        self.__idade = ida

    def speak(self):
            if self.speaking == 0:
                print("speaking...")
                print("Hello Emmanuel, Do not give up!")
                self.speaking = 1
            else:
                print("I am already speaking")

    def stopspeaking(self):
            if self.speaking == 1:
                print("silence")
                self.speaking = 0
            else:
                print(" Already quite ")


class Aluno(Person, object):
    def __init__(self, nome, idade, codigo: str, curso: str, turma: str):
        Person.__init__(self, nome, idade)
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso
        self.__turma = turma

    def get_nome(self):
        return self.__nome

    def set_nome(self, n):
        self.__nome = n

    def get_idade(self):
        return self.__idade

    def set_idade(self, ida):
        self.__idade = ida

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, c):
        self.__codigo = c

    def get_turma(self):
        return self.__turma

    def set_turma(self, t):
        self.__turma = t

    def getcurso(self):
        return self.__curso

    def set_curso(self, cur):
        self.__curso = cur

Emanuel = Aluno("Emanuel",19,"055/0174","Maquinas Maritimas","MM2")
Emanuel.speak()
print(Emanuel.get_nome(), Emanuel.get_idade(),"anos ", Emanuel.getcurso())
