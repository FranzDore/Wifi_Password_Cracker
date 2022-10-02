import subprocess

def main():
   output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode() #comando wifi
   lista = output.split("Tutti i profili utente")  
   lista.remove(lista[0])                          #tolgo il primo, che non mi serve
   lista = pulisci_lista(lista)                    #contiene i nomi delle wifi
   lis_pw = []
   cerca_pw(lista, lis_pw)                         #lis_pw contiene le password
   with open("lista_wifi", "w") as f:
      str = ""
      for i in range(len(lis_pw)):
         str += lista[i]
         str += " : "
         str += lis_pw[i]
         str += "\n"
      f.write(str)

def cerca_pw(lis, pw):
   for x in lis:
      info = subprocess.run(["netsh", "wlan", "show", "profile", x, "key=clear"], capture_output=True).stdout.decode(errors='replace')
      #print(info)
      temp = info.split("Contenuto chiave")
      if len(temp) == 1:                      #non esiste il campo "Contenuto chiave"
         pw.append("Non trovata")
      else:                         #se esiste, la cerchiamo con ".split()" e ".strip()"
         sporco = temp[1].strip().strip(": ")
         temp = sporco.split("\r")
         pw.append(temp[0])

def pulisci_lista(lis):
   lista_new = [] #conterrà ANCHE i nomi delle wifi, senza spazi bianchi
   for x in lis:
      temp = x.strip()
      str = temp.strip(": ")
      lista_new.append(str)
   return lista_new


main()