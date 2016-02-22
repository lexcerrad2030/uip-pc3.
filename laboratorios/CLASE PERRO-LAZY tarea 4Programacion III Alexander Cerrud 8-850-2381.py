class Perro:
     def __init__(self, vida=0, alegria=0):
         self.vida = vida
         self.alegria = alegria

     def caminar(self):
         self.vida-=2
         self.alegria+=1

     def correr (self):
         self.vida-=4
         self.alegria+=3

     def dormir(self):
         self.vida+=1
         self.alegria+=3

     def jugar (self):
         self.vida-=3
         self.alegria+=4

     def comer(self):
         self.vida+=5
         self.alegria+=1

         cont=0
         lazy=Perro(5,5)
         while cont!=10:

             lazy.dormir()
             if lazy.vida==0:
                print("murio")
                break

             else:
                 cont+=1

             lazy.jugar()
             if lazy.vida==0:
                print("murio")
                break

             else:
                  cont+=1

             lazy.comer()
             if lazy.vida==0:
                print("murio")
                break

             else:
                 cont+=1
             lazy.jugar()
             if lazy.vida==0:
               print("murio")
               break
             else:
                cont=+1

             lazy.caminar()
             if lazy.vida==0:
                print("murio")
                break
             else:
                  cont=+1

             lazy.dormir()
             if lazy.vida==0:
                print("murio")
                break
             else:
                  cont=+1

             lazy.correr()
             if lazy.vida==0:
                 print("murio")
                 break
             else:
                   cont=+1

             lazy.dormir()
             if lazy.vida==0:
                print("murio")
                break
             else:
                 cont=+1

             lazy.dormir()
             if lazy.vida==0:
                print("murio")
                break
             else:
                 cont=+1

             lazy.comer()
             if lazy.vida==0:
                 print("murio")
                 break
             else:
                 cont=+1

                 if cont==10:
                   print("vive lazy")
                 else:
                   print("lamentablemente murio lazy")