# Pattern1
n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()

# Pattern2
n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()

# Pattern3
n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print('*',end=' ')
    print()

# Pattern4
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(str(p),end=' ')
    p+=1
    print()

# Pattern5
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()

# Pattern11
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()

# Pattern6
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

# Pattern7
n = 5
q = (2 * n) - 2

for i in range(n):
    p = 1
    for j in range(q):
        print(' ',end="")
    q-= 1
    for j in range(i + 1):
        print(p, end=' ')
        p+= 1
    print(" ")


#Pattern9:
n = 5
q = (2 * n) - 2
for i in range(n):
    p = 65
    for j in range(q):
        print(' ',end="")
    q-= 1
    for j in range(i + 1):
        print(chr(p), end=' ')
        p+= 1
    print(" ")


# Pattern14
n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(p,end='')
        p+=1
    print()


# Pattern18
n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print(chr(p),end='')
        p+=1
    print()


# Pattern15
n=5
for i in range(n):
    p=5
    for j in range(i,n):
        print(p,end=' ')
        p-=1
    print()


# Pattern16
n=5
for i in range(n):
    p=5
    for j in range(i+1):
        print(p,end=' ')
        p-=1
    print()


#pattern17
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()


#Pattern12
n = 5
q = (2 * n) - 2
p = 1
for i in range(n):
    for j in range(q):
        print(' ',end="")
    q-= 1
    for j in range(i + 1):
        print(p, end=' ')
    p+= 1
    print(" ")

#Pattern13
n = 5
q = (2 * n) - 2
p = 65
for i in range(n):
    for j in range(q):
        print(' ',end="")
    q-= 1
    for j in range(i + 1):
        print(chr(p), end=' ')
    p+= 1
    print(" ")


#Pattern18
n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print(chr(p),end=' ')
        p+=1
    print()


#Pattern12
n = 5
q = (2 * n) - 2
p = 65
for i in range(n):
    for j in range(q):
        print(' ',end="")
    q-= 1
    for j in range(i + 1,0,-1):
        print(n-j+1, end=' ')
    p+= 1
    print(" ")


#Pattern10
