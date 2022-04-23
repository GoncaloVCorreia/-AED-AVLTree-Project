from sys import stdin,stdout

class Node:
    def __init__(self, numUtente):
        self.left = None
        self.right = None
        self.profundidade=1
        self.key= numUtente
        self.vacinasDatas={}
        
class Avl():
    def infoPaciente(self,root,dicOrdenado):

        linha=str(root.key)+" "
        for i in range(len(dicOrdenado)):
            if(i<(len(dicOrdenado)-1)):
                linha+=str(dicOrdenado[i][0])+" "+str(dicOrdenado[i][1])+" "
            else:
                linha+=str(dicOrdenado[i][0])+" "+str(dicOrdenado[i][1])
        outln(linha)

    def percorreOrdemCrescente(self,root):
        if root: 

            self.percorreOrdemCrescente(root.left) 
            
            self.infoPaciente(root,sorted(root.vacinasDatas.items()))
            
            self.percorreOrdemCrescente(root.right) 
        
    def recebePaciente(self,root,numUtente,vacina,data,lista,comando):

        if(root.key==numUtente):
           
            lista.append(0)
            
            self.Atualiza(root,numUtente,vacina,data,comando)

        elif root!=None and len(lista)==0: 
            
            if(root.left!=None):
                self.recebePaciente(root.left,numUtente,vacina,data,lista,comando) 
           
            if(root.right!=None):
               
                self.recebePaciente(root.right,numUtente,vacina,data,lista,comando) 
                
        return lista
    def Atualiza(self,root,numUtente,vacina,data,comando):

        if(comando=="ACRESCENTA"):
            if(vacina in root.vacinasDatas.keys()):
                root.vacinasDatas[vacina]=data
                outln("VACINA ATUALIZADA")
            else:
                outln("NOVA VACINA INSERIDA")
                root.vacinasDatas.update({vacina:data})

        if(comando =="CONSULTA"):
           
            self.infoPaciente(root,sorted(root.vacinasDatas.items()))
            
            outln("FIM")

    def Apaga(self,root):
        if root: 
           
            self.Apaga(root.left) 

            self.Apaga(root.right) 
            
            root.left=None
            root.right=None
  
    def CriaRegisto(self,numUtente,vacina,data):
        registo = Node(numUtente)

        registo.vacinasDatas.update({vacina:data})
        outln("NOVO UTENTE CRIADO")
        return registo

    def insereRegisto(self,root,key,vacina,data):
        
        if root == None:
         
            return self.CriaRegisto(key,vacina,data)
        
        
        if key < root.key:
            
            root.left = self.insereRegisto(root.left, key,vacina,data)

        if key > root.key:  
                     
            root.right = self.insereRegisto(root.right, key, vacina, data)
       

        #Profundidade sub árvore esquerda
        subEsquerda=self.getProfundidade(root.left)
        #Profundidade sub árvore direita
        subDireita= self.getProfundidade(root.right)
        #Atualiza Profundidade
        root.profundidade = 1 + max(subEsquerda, subDireita)
     
        fatorEquilibrio = self.getfatorEquilibro(root)
       
        if fatorEquilibrio > 1:

            if self.getfatorEquilibro(root.left) >= 0:

                return self.rightRotate(root)

            else:

                root.left = self.leftRotate(root.left)

                return self.rightRotate(root)

        if fatorEquilibrio < -1:

            if self.getfatorEquilibro(root.right) <= 0:

                return self.leftRotate(root)

            else:

                root.right = self.rightRotate(root.right)

                return self.leftRotate(root)

        return root

    def leftRotate(self, root):

        centro= root.right
        subAEsquerda = centro.left
        centro.left = root
        root.right = subAEsquerda

        #Atualiza profundidade
        root.profundidade = 1+max(self.getProfundidade(root.left), self.getProfundidade(root.right))
        centro.profundidade = 1+max(self.getProfundidade(centro.left), self.getProfundidade(centro.right))
        return centro
    
    
    def rightRotate(self, root):
       
        centro = root.left
        subADireita = centro.right
        centro.right = root
        root.left = subADireita

         #Atualiza profundidade
        root.Profundidade = 1+max(self.getProfundidade(root.left), self.getProfundidade(root.right))
        centro.Profundidade = 1+max(self.getProfundidade(centro.left),self.getProfundidade(centro.right))

        return centro

    def getProfundidade(self, root):
        if root==None:
            return 0
        return root.profundidade

    def getfatorEquilibro(self, root):
        if root==None:
            return 0

        subAEsquerda=self.getProfundidade(root.left)
        subADireita=self.getProfundidade(root.right)

        return subAEsquerda-subADireita
        
def readlines():
    
    
    instrucoes = []
    read=True
    while read:
        line = stdin.readline().rstrip('\n')
        if line == 'FIM':
            read= False
        else:
            instrucoes.append(line)

    return instrucoes

def outln(value):
    stdout.write(str(value))
    stdout.write("\n")

if __name__ == "__main__":
   lista=readlines()
   listaFinal=[]
   for i in range (len(lista)):
       listaFinal.append(lista[i].split())
   
   for j in range(len(listaFinal)):
        
        if(listaFinal[j][0]=="ACRESCENTA" or listaFinal[j][0]=="CONSULTA"):
            listaFinal[j][1]=int(listaFinal[j][1])
 
   ArvoreAvl=Avl()
   root=None
  
   for x in range (len(listaFinal)):
        
        aux=[]
        atualiza=[]
        #Recebe instrucao, se paciente ja estiver inserido atualiza informacao ou faz a consulta das vacinas dependendo da instrucao
        if(root!=None):
            if(listaFinal[x][0]=="ACRESCENTA"):
                atualiza=ArvoreAvl.recebePaciente(root,listaFinal[x][1],listaFinal[x][2],listaFinal[x][3],aux,listaFinal[x][0])
            if(listaFinal[x][0]=="CONSULTA"):
                atualiza=ArvoreAvl.recebePaciente(root,listaFinal[x][1],None,None,aux,listaFinal[x][0])

        #Se paciente nao estiver registado regista
        if(len(atualiza) == 0 and listaFinal[x][0]=="ACRESCENTA"):
           
            root=ArvoreAvl.insereRegisto(root,listaFinal[x][1],listaFinal[x][2],listaFinal[x][3])
        #Se quando executar o comando de consulta não encontrar nenhum registo
        if(len(atualiza)== 0 and listaFinal[x][0]=="CONSULTA"):
            outln("NAO ENCONTRADO")

        if(listaFinal[x][0]=="APAGA"):
            ArvoreAvl.Apaga(root)
            root=None
            outln("LISTAGEM DE NOMES APAGADA")

        if(listaFinal[x][0]=="LISTAGEM"):
            ArvoreAvl.percorreOrdemCrescente(root)
            outln("FIM")
  
   
   