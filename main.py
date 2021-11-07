#membuat class
class Ricecooker:
  #fungsi construktor
  def __init__(self,nama_merk,Tuas,panci,Mode):
    self.nama_merk = nama_merk
    self.Tuas = Tuas
    self.panci = panci
    self.Mode = Mode
    self._activatedtemperature = None

#objek
# Ricecooker_kamar_kost = Ricecooker()
# Ricecooker_dapur = Ricecooker()

#methode
  def turnonRicecooker(self):
    print('Ricecooker ON ',self.nama_merk)

  def turnoffRicecooker(self):
    print('Ricecooker off ',self.nama_merk)
  
  def pressTuas(self,version):
    self.version=version
    print('Ricecooker Cook version',self.nama_merk, ' version ', self.version)

  def __typetemperature(self):
    print('choose type of temperature')
    self.__temperatur = [50, 65, 75]

  def _temperature(self):
    print('choose temperature')
    self._activatedtemperature = self._temperatur
 
  def activatedtemperature(self, num):
    self._activatedtemperature = num
    print('Temperatur aktif', self.nama_merk,'Ricecooker',self._activatedtemperature)
    
  def __add__(self, other) :
   return self.Mode + other.Mode

kost = Ricecooker('Young Ma', 'memasak', 'terisi', 5)
dapur = Ricecooker('Cosmos', 'menghagatkan', 'terisi', 6)
print(kost + dapur)
print(kost)
print(kost.__dict__)

#overriding phyton
#class KosCooker(Ricecooker):
# def __init__(self,nama_merk,Tuas,panci,Mode):
 #   super(KosCooker, self).__init__(nama_merk,Tuas,panci,Mode)
# def pressTuas(self, version, step):
   #  self.step = step
    # self.version = version
    # print('Ricecooker Cook version',self.nama_merk, ' version ', self.version, self.step)
 #def temperature(self):
    #return self._activatedtemperature



#atribut ke objek
#Ricecooker_kamar_kost = Ricecooker('cosmos','memasak','terisi', 5 )
#Ricecooker_dapur = KosCooker('yong ma','menghangatkan','terisi', 7)
#Ricecooker_dapur.activatedtemperature(200)
#print(Ricecooker_dapur.temperature())

#memanggil fungsi dari objek
#Ricecooker_dapur.turnonRicecooker()
#Ricecooker_kamar_kost.turnonRicecooker()
#Ricecooker_dapur.pressTuas('memasak', 2)
#print()

