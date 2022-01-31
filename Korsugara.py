def kerulet (r):
    pi=3.14
    return(2*r*pi)

def terulet (r):
    pi=3.14
    return(r**2)*(pi)
sugar=float(input("A kör sugara "))
K=kerulet(sugar)
T=terulet(sugar)
print(" A körterülete: [0] egység".format(K))
print(' A Kerület: [0] négzetegység.'.format(T))