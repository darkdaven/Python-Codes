import hashlib
import bz2

class EncryptInterface():
     def Encrypt(self):
          pass
     def addPhrase(self,Phrase):
          pass

class Sha512(EncryptInterface):
     
     def __init__(self):
          self.encryptClass = hashlib.sha512()

     def addPhrase(self,Phrase):
           self.encryptClass.update(Phrase)
          
     def Encrypt(self):
          return self.encryptClass.hexdigest()

class Bz2(EncryptInterface):
     
     def __init__(self):
          self.phrase = ''

     def addPhrase(self,Phrase):
           self.phrase += Phrase
          
     def Encrypt(self):
          return bz2.compress(self.phrase)
         
          

class EncryptorContainer():
     
     def __init__(self):
          self.Container = {}
          self.Container['sha512'] = Sha512
          self.Container['bz2'] = Bz2

     def getAlgorithm(self,Algorithm):
          _algorithm = self.Container[Algorithm]
          return _algorithm()
          
          

encryptCont = EncryptorContainer().getAlgorithm('sha512')

encryptCont.addPhrase('hola mundo')
encryptCont.addPhrase('como estan')

print encryptCont.Encrypt()
