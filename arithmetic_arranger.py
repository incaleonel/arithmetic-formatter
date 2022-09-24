def arithmetic_arranger(problems, result = False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  arrayNum1, arrayArit, arrayNum2, suma = [], [], [], []
  index = 0
  for problem in problems:
    opNum1 = problem.split()[0]
    opAr = problem.split()[1]
    opNum2 = problem.split()[2]
    
    if (opAr.find('+') == -1) and (opAr.find('-') == -1):
      return "Error: Operator must be '+' or '-'."
      
    if not(opNum1.isdigit() and opNum2.isdigit()):
      return 'Error: Numbers must only contain digits.'
      
    if (len(opNum1) > 4) or (len(opNum2) > 4):
      return "Error: Numbers cannot be more than four digits."

    suma.append(str(int(opNum1) + int(opAr + opNum2)))
    while (len(opNum1) - len(opNum2)):
      opNum1 = " " + opNum1 if len(opNum2) > len(opNum1) else "" + opNum1
      opNum2 = " " + opNum2 if len(opNum1) > len(opNum2) else "" + opNum2
    
    arrayNum1.append(opNum1)
    arrayArit.append(opAr)
    arrayNum2.append(opNum2)
    
    while (len(suma[index]) - len(opNum1 + '  ')):
      suma[index] = " " + suma[index]
    index += 1
    
  linea1 = "  " + arrayNum1[0]
  linea2 = "\n" + arrayArit[0] + " " + arrayNum2[0]
  linea3 = "\n--"

  for j in range(len(arrayNum1[0])):
    linea3 += '-'
  for i in range(1,len(arrayNum1)):
    linea1 += "      " + arrayNum1[i]
    linea2 += "    " + arrayArit[i] + " " + arrayNum2[i]
    linea3 += "    --"
    for j in range(len(arrayNum1[i])):
      linea3 += '-'
  arranged_problems = linea1 + linea2 + linea3 
  if result:
      arranged_problems += '\n'
      for element in suma:
        arranged_problems += element + '    '
      arranged_problems = arranged_problems[:len(arranged_problems)-4]  
  return arranged_problems
    