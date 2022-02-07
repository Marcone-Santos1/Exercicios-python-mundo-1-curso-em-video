a = int(input('Qual o tamanho da reta 1? '))
b = int(input('Qual o tamanho da reta 2? '))
c = int(input('Qual o tamanho da reta 3? '))

if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
    print('Os lados {}, {} e {} podem formar triângulo.'.format(a,b,c))
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(a,b,c))