import cp

print("\n")

letra = "A"
fator = 3
cd= cp.cripto(letra,fator)
codigo = cd
saida = cp.decripto(codigo,fator)

print(f"O Código {codigo} corresponde á letra : {saida}")
