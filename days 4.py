class Mobil:
  def __init__(self, merk, warna, jumlahkursi):
    self._merk = merk
    self._warna = warna
    self._jumlahkursi = jumlahkursi

  # Getter 
  def get_merk(self):
    return self._merk

  # Setter 
  def set_merk(self, merkbaru):
    self._merk = merkbaru

  # Getter
  def get_warna(self):
    return self._warna

  # Setter
  def set_warna(self, warnabaru):
    self._warna = warnabaru

  # Getter 
  def get_jumlahkursi(self):
    return self._jumlahkursi

  # Setter 
  def set_jumlahkursi(self, jumlah_kursibaru):
    self._jumlahkursi = jumlah_kursibaru

# object
mobil1 = Mobil("Toyota", "Merah", 5)
print(mobil1.get_merk())  # Output: Toyota
mobil1.set_merk("Honda")
print(mobil1.get_merk())  # Output: Honda
print(mobil1.get_warna())  # Output: Merah
mobil1.set_warna("Biru")
print(mobil1.get_warna())  # Output: Biru
print(mobil1.get_jumlahkursi())  # Output: 5
mobil1.set_jumlahkursi(4)
print(mobil1.get_jumlahkursi())  # Output: 4