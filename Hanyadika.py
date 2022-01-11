while True:
    print ('1. FELADAT')
    val = int(input( ' Hanyadik nap van a héten ' ))
    try:
    
        if val == 1:
            print('hétfö hétköznap')
            break
        elif val == 2:
            print('kedd hétköznap')
            break
        elif val == 3:
            print('szerda hétköznap')
            break
        elif val == 4:
            print('csütörtök hétköznap')
            break
        elif val == 5:
            print('péntek hétköznap')
            break
        elif val == 6:
            print('szombat hétvége')
            break
        elif val == 7:
            print('vasárnap hétvége')
        else:
            print('igy nem jó'  , end='')
    
    except Exception:
        print('error')




