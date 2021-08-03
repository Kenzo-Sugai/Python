def contaPalavras(texto):
  dic = {}

  texto = texto.replace("!", "")
  texto = texto.replace("?", "")
  texto = texto.replace(",", "")

  texto = texto.lower()
  texto = texto.split()


  for i in texto:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
  
  return dic