#Dimitra Machairidou AM 4108
print('CODECRACKER GAME')
print('The objective is to guess the secret code in as few attempts as posible.')
print()
attempts=0
b=int(input('input 1 for 1-player game or 2 for 2-player game:'))
if b==1:
    import random
    y=str(random.randint(1,6))
    k=str(random.randint(1,6))
    l=str(random.randint(1,6))
    p=str(random.randint(1,6))
    c=(y,k,l,p)
elif b==2:
    print("player 2 enter the secret code.you can use any combination of 4 symbols in ['1','2','3','4','5','6'] as colors.:")
    d=0
    y=""
    while len(y)!=4 or d!=4:
        y=input("")
        d=0
        for m in  range(len(y)):
            if y[m] in ['1','2','3','4','5','6']:
                d+=1
        if len(y)!=4:
            print("More numbers than 4. Enter just 4 numbers")
        if d!=4 and len(y)==4:
            print("You can only use numbers between 1 and 6")
    c=list(y)
print("player 1 please, enter your color code.you can use any combination of 4 symbols in ['1','2','3','4','5','6'] as colors.")
while attempts!=8:
    e=[]
    q=[]
    d=0
    r=[]
    w=""
    print('attempt',attempts+1)
    while len(w)!=4 or d!=4:
        w=input("")
        v=list(w)
        d=0
        for m in range(len(w)):
            if w[m] in ['1','2','3','4','5','6']:
                d+=1
        if len(w)!=4:
            print("More numbers than 4. Enter just 4 numbers")
        if d!=4:
            print("You can only use numbers between 1 and 6")
    if c==v:
        print('Congratulations! You found it in',attempts+1,'attempts!')
        break
    for n in range(len(v)):
        if v[n]==c[n]:
            r.append('o')
            e.append(n)
    for n in range(len(v)):
        for z in range(len(c)):
            if v[n]==c[z] and z not in e and n not in q:
                r.append('x')
                q.append(n)
                e.append(z)
    s=r.sort()
    print(''.join(r))
    attempts+=1
    if b==1 and attempts==8:
        print('You failed to guess within 8 attempts.')
        print('The secret code was',int(''.join(c)))
        print('CPU wins.')
    elif b==2 and attempts==8:
        print('You failed to guess within 8 attempts.')
        print('The secret code was',int(''.join(c)))
        print('Player 2 wins.')
