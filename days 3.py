class Kendaraan:
  def __init__(self,warna):
    self.warna = warna

  def klakson(self):
    print("2m 2m")

class Mobil(Kendaraan):
  def __init__(self,warna,jumlahpintu):
    super().__init__(warna) 
    self.jumlahpintu = jumlahpintu

  def __str__(self):
    return f"Mobil berwarna {self.warna} dengan {self.jumlahpintu} pintu."

class Motor(Kendaraan):
  def __init__(self,warna,topspeed):
    super().__init__(warna) 
    self.topspeed = topspeed

  def __str__(self):
    return f"Motor berwarna {self.warna} dengan kecepatan maksimal {self.topspeed} km/jam."

# Membuat objek Mobil
porsche = Mobil("hitam", 2)
print(porsche)  # Output: Mobil berwarna hitam dengan 2 pintu.
porsche.klakson()  # Output: 2m 2m (diwarisi dari class Kendaraan)

h4race = Motor("biru putih", 300)
print(h4race)  # Output: Motor berwarna biru putih dengan kecepatan maksimal 300 km/jam.
h4race.klakson()  # Output: 2m! 2m! (diwarisi dari Kendaraan)
