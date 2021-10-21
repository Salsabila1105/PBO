#membuat class
class Ricecooker:
  #fungsi construktor
  def __init__(self,nama_merk,Tuas,panci,Mode):
    self.nama_merk = nama_merk
    self.Tuas = Tuas
    self.panci = panci
    self.Mode = Mode

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


#overriding phyton
class KosCooker(Ricecooker):
 def __init__(self,nama_merk,Tuas,panci,Mode):
    super(KosCooker, self).__init__(nama_merk,Tuas,panci,Mode)
 def pressTuas(self, version, step):
     self.step = step
     self.version = version
     print('Ricecooker Cook version',self.nama_merk, ' version ', self.version, self.step)

    


#atribut ke objek
Ricecooker_kamar_kost = Ricecooker('cosmos','memasak','terisi', 'mode bubur', )
Ricecooker_dapur = KosCooker('yong ma','menghangatkan','terisi', 'Ikan')

#memanggil fungsi dari objek
Ricecooker_dapur.turnonRicecooker()
Ricecooker_kamar_kost.turnonRicecooker()
Ricecooker_dapur.pressTuas('memasak', 2)


