'''
Fatiamento
'''

Frase = 'Curso em vídeo python'

print(Frase[0])

print(Frase[0:14])

# ':' fatia uma string de () a () '[:]'

print(Frase[0:14:2])

# ':' fatia uma string de () a () '[:]'
# quando usamos ['':'':'']; o terceiro valor é o intevarlo entre cada caractere

print(Frase[:5])

# vai do início até o numero pedido

print(Frase[15:])

# printa do numero pedido até o final da Frase

print(Frase[9::13])

# print de do início a 9 e de 13 até o final

'''
Análise
'''

print(len(Frase))

# da o tamanho da string


print(Frase.count('o'))

# .count() da o numero pedido da caractere

print(Frase.count('o',0,14))

print(Frase.find('deo'))

# procura quando começa a str no .find()

Frase.find('Android')
print(Frase)

# printa -1, ou seja, não existe ou não foi encontrado

print('Curso' in Frase)

'''
Transformação
'''

print(Frase.replace('python','Android'))


print(Frase.upper())

print(Frase.lower())

print(Frase.capitalize())

print(Frase.title())

print(Frase.strip())

'''
Divisão
'''

print(Frase.split())

'''
Junção
'''

print('-'.join(Frase))

motivacional = '''Desejo que você
Não tenha medo da vida, tenha medo de não vivê-la.
Não há céu sem tempestades, nem caminhos sem acidentes.
Só é digno do pódio quem usa as derrotas para alcançá-lo.
Só é digno da sabedoria quem usa as lágrimas para irrigá-la.
Os frágeis usam a força; os fortes, a inteligência.
Seja um sonhador, mas una seus sonhos com disciplina,
Pois sonhos sem disciplina produzem pessoas frustradas.
Seja um debatedor de ideias. Lute pelo que você ama.'''

print(len(motivacional))
print(motivacional.strip())
print('-'.join(motivacional))


