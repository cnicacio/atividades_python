'''
Crie uma classe que modele uma pessoa

a) Atributos nome, idade, peso e altura
b) Métodos envelhecer, engordar, emagrecer, crescer

Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0 5 cm
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if self.idade + anos < 21:
            self.altura += 0.5 * anos
        elif self.idade + anos >= 21 and self.idade <= 21:
            self.altura += 0.5 * (21 - self.idade)
        else:
            pass

    def dados(self):
        return f'''
        Nome: {self.nome}
        Idade: {self.idade}
        Peso: {self.peso}
        Altura: {self.altura}
        '''


p_nome = str(input('Digite o nome da pessoa: '))
p_idade = int(input('Digite a idade da pessoa: '))
p_peso = float(input('Digite o peso da pessoa em kg: '))
p_altura = int(input('Digite a altura da pessoa em cm: '))


p_pessoa = Pessoa(p_nome, p_idade, p_peso, p_altura)

p_anos = int(input(f'Quantos anos {p_nome} envelheceu? '))
p_pessoa.envelhecer(p_anos)

print(p_pessoa.dados())