# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 08:58:34 2022

@author: AM
"""

# CRIPTOGRAFIA SIMÉTRICA - SUBSTITUIÇÃO SIMPLES NUMÉRICA e COM SHIFT - JÚLIO CESAR

chavecriptosimetrica2=[{"A":29,"B":49,"C":58,"D":72,"E":13,
                       "F":28,"G":48,"H":57,"I":71,"J":12,
                       "K":27,"L":47,"M":56,"N":70,"O":11,
                       "P":26,"Q":46,"R":55,"S":69,"T":10,
                       "U":25,"V":45,"X":54,"Y":68,"Z":9,
                       "W":24,".":44,",":53,"!":67,"?":8,
                       "$":23,"#":43,"%":52,"*":66,"+":7,
                       "-":22,"/":42,"0":51,"1":65,"2":6,
                       "3":21,"4":41,"5":50,"6":64,"7":5,
                       "8":20,"9":35,
                       "a":19,"b":34,"c":40,"d":63,"e":4,
                       "f":18,"g":33,"h":39,"i":62,"j":3,
                       "k":17,"l":32,"m":38,"n":61,"o":2,
                       "p":16,"q":31,"r":37,"s":60,"t":1,
                       "u":15,"v":30,"x":36,"y":59,"z":0,
                       "w":14," ":73
                       }]


chavedecriptosimetrica2=["z","t","o","j","e","7","2","+","?","Z",
                         "T","O","J","E","w","u","p","k","f","a",
                         "8","3","-","$","W","U","P","K","F","A",
                         "v","q","l","g","b","9","x","r","m","h",
                         "c","4","/","#",",","V","Q","L","G","B",
                         "5","0","%",",","X","R","M","H","C","y",
                         "s","n","i","d","6","1","*","!","Y","S",
                         "N","I","D"," ",]

#**************
# CRIPTOGRAFIA
#**************
def cripto(letra,fator):
  frase=letra[:1]
  cripto=""
  for s in frase:
    token=(chavecriptosimetrica2[0][s]+fator) % 74
    #print(token,"   ",(token+fator)% 74)
    cripto=cripto+format(token,"02d")
  return(cripto)
  

#****************
# DECRIPTOGRAFIA
#****************
def decripto(valor,fator):
  cripto=valor[:2]
  decriptos=""
  fatorDecoder=2
  for pos in range(0,len(cripto),fatorDecoder):
    ftoken=int(cripto[pos:pos+fatorDecoder])   
    decriptos=decriptos+chavedecriptosimetrica2[(ftoken-fator) % 74]   
  return(decriptos)
      
 