nome = input('Olá, qual é o seu nome?\n')
time = input('Certo, {}, agora me diga, para que time você torce?\n a)Corinthians\n b)São Paulo\n c)Palmeiras\n d)Santos\n'.format(nome)).lower()
print('Certo, agora vamos ver se você conhece mesmo o seu time.')
if (time == 'a'):
    resp1 = input('Quantos mundiais o Corinthians tem:\n a)0 mundiais\n b)1 mundial\n c)"2" mundiais\n d)3 mundiais\n').lower()
    if (resp1 == 'c'):
        print('Parabéns, você é um corinthiano roxo!')
    else:
        print('Você só é torcedor quando o "timão" ganha...')
elif (time == 'b'):
    resp2 = input('Quantos mundiais o Tricolor tem:\n a)0 mundiais\n b)1 mundial\n c)2 mundiais\n d)3 mundiais\n').lower()
    if (resp2 == 'd'):
        print('Parabéns, você realmente ama o Tricolor. Trimundial só tem um!')
    else:
        print('Você não é um são paulino de verdade...')
elif (time == 'c'):
    resp3 = input('Quantos mundiais o Palmeiras tem:\n a)0 mundiais\n b)1 mundial\n c)2 mundiais\n d)3 mundiais\n').lower()
    if (resp3 == 'a'):
        print('Parabéns, você acertou, meus pesâmes...')
    else:
        print('Parabéns, você é dodoi...')
else:
    resp4 = input('Quantos mundiais o Santos tem:\n a)0 mundiais\n b)1 mundial\n c)2 mundiais\n d)3 mundiais\n').lower()
    if (resp4 == 'c'):
        print('Parabéns, você é um santista apaixonado.')
    else:
        print('Você está pior que as lesões do Neymar...')