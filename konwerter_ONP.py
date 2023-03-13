def zamien(input):
  elementy = input.split()
  stos = []
  operators = {'/':1,'*':1,'+':2,'-':2}
  output = []
  for e in elementy:
    #operator
    if e in operators:
        priority = operators[e]
        while len(stos)>0:
          top = stos[-1]
          if top in operators and operators[top]<=priority:
            output.append(top)
            stos.pop()
          else:
            break
        stos.append(e)
             
    elif e=='(':
        stos.append('(')
    elif e==')':
        while len(stos)>0 and stos[-1]!='(':
            output.append(stos[-1])
            stos.pop()
        if stos[-1]=='(':
            stos.pop()
    else:
        print('e:',e)
        output.append(e)
  while len(stos)>0:
    output.append(stos[-1])
    stos.pop()
  return output
    
      

print(zamien(' ( ( 10 + 5 ) / ( 7 - 2 ) ) * 2 + 12'))
