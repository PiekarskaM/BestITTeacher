def oblicz(wyrazenie):
  symbole = wyrazenie.split()
  stos = []
  operators = ['/','*','+','-']
  for symbol in symbole:
    if symbol in operators:
      a = int (stos.pop())
      b = int (stos.pop())
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

print(oblicz("23 4 5 2 * 3 6 / + * +"))