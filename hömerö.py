def homerseglet(c):
    if c == 0 :
        return("fagypont")
    elif c < 0 :
        return("fagy")
    elif c > 99 :
        return("forras")
    else  : 
        return("normal")

for x in reversed (range (-20,121,20)):
    print(x,"c",homerseglet(x))