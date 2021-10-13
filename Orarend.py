print('Választható napok: (h, k, sz, cs, p)')

dayOfWeek = input("Melyik nap órarendjét szeretnéd megtudni?")

validDays = ["h", "k", "sz", "cs", "p"]

timeTable = {
  "h": "Történelem,Ikt,Ikt,Magyar,Angol,Matematika",
  "k": "Fizika,Osztályfőnöki,Angol,Történelem,Magyar,Magyar",
  "sz": "Magyar,Táv,Táv,Angol,Matematika,Testnevelés,Programozás,Programozás",
  "cs": "Matematika,Pénzügyi,Angol,Digi kult,Történelem,Fizika,Testnevelés,Testnevelés",
  "p": "Matematika,Testnevelés,Magyar,Táv,Táv,Digi kult"
} 
if dayOfWeek.lower() not in validDays:
  print('Nem megfelelő a nap formátuma')
else:
  print(timeTable[dayOfWeek.lower()])