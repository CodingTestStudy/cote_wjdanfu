k= input()
while True:
  if k.count('U')!=0:
    k=(k[k.index('U'):])
  else:
    print("I hate UCPC")
    break;

  if k.count('C')!=0:
    k=(k[k.index('C'):])
  else:
    print("I hate UCPC")
    break

  if k.count('P')!=0:
    k=(k[k.index('P'):])
  else:
    print("I hate UCPC")
    break

  if k.count('C')!=0:
    print("I love UCPC")
    break
  else:
    print("I hate UCPC")
    break
