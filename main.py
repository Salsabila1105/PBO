#membuat class
class Ricecooker:
  #fungsi construktor
  def __init__(self,nama_merk,Tuas,panci):
    self.nama_merk = nama_merk
    self.Tuas = Tuas
    self.panci = panci

#objek
# Ricecooker_kamar_kost = Ricecooker()
# Ricecooker_dapur = Ricecooker()

#methode
  def turnonRicecooker(self):
    print('Ricecooker ON ',self.nama_merk)

  def turnoffRicecooker(self):
    print('Ricecooker off ',self.nama_merk)
    
  def pressTuas(self):
    print('Tuas Ricecooker On ',self.nama_merk)

#atribut ke objek
Ricecooker_kamar_kost = Ricecooker('cosmos','memasak','terisi')
Ricecooker_dapur = Ricecooker('yong ma','menghangatkan','terisi')

#memanggil fungsi dari objek
Ricecooker_dapur.turnonRicecooker()
Ricecooker_dapur.pressTuas()

print(Ricecooker_dapur.nama_merk)
print(Ricecooker_dapur.Tuas)
print(Ricecooker_dapur.panci)
print(Ricecooker_kamar_kost.nama_merk)
print(Ricecooker_kamar_kost.Tuas)
print(Ricecooker_kamar_kost.panci)