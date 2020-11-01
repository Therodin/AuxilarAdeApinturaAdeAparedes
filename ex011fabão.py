b = float(input('insira a Base: '))
a = float(input('insira a altura: '))

dim = b * a

print(f'sua parede tem a dimensão {b} x {a} e sua parede tem {dim}m²')

ml = dim/2

print(f'sua parede precisará de {ml:.2f} litros de tinta ')

t = ml/18

if t <= 1:
    print(f'você só precisa comprar uma lata')
else:
    t = t
    print(f'você vai precisar de {t:.0f} latas de tinta para terminar sua parede')

    CT = 160.00

    lm = str(input('você precisa comprar mais tinta?: '))

    if lm == 'sim':
        print("uma lata custa {:.2f}".format(CT))

    else: lm == 'não'
    print('volte sempre!')
