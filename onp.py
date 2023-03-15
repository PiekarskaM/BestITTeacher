def oblicz(wyrazenie):
  symbole = wyrazenie.split()
  stos = []
  operators = ['/','*','+','-']
  for symbol in symbole:
    if symbol in operators:
      b = int (stos.pop()) #b jest na szczycie stosu
      a = int (stos.pop()) #a jest na stosie tuż pod b
      if symbol == '+':
        res = a + b
      elif symbol == '-':
        res = a - b
      elif symbol == '*':
        res = a * b
      elif symbol == '/':
        res = a / b
      stos.append(res)
    else:
      stos.append(int(symbol))
  return stos.pop()

print(oblicz("23 4 5 2 * 6 3 / + * +"))
