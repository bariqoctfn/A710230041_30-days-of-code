class Tiket:
  """Superclass untuk tiket bioskop."""

  def __init__(self, jenis, jumlah):
    self.jenis = jenis
    self.jumlah = jumlah

  def harga_tiket(self):
    """Mencetak harga tiket berdasarkan jenis tiket."""
    raise NotImplementedError

class TiketBiasa(Tiket):
  """Subclass untuk tiket biasa."""

  def harga_tiket(self):
    return self.jumlah * 25000

class TiketVIP(Tiket):
  """Subclass untuk tiket VIP."""

  def harga_tiket(self):
    return self.jumlah * 50000

class TiketGold(Tiket):
  """Subclass untuk tiket Gold."""

  def harga_tiket(self):
    return self.jumlah * 75000

def main():
  """Fungsi utama untuk menjalankan program."""
  jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ")
  jumlah_tiket = int(input("Masukkan jumlah tiket: "))

  # Membuat objek berdasarkan jenis tiket
  if jenis_tiket == "biasa":
    tiket = TiketBiasa(jenis_tiket, jumlah_tiket)
  elif jenis_tiket == "vip":
    tiket = TiketVIP(jenis_tiket, jumlah_tiket)
  elif jenis_tiket == "gold":
    tiket = TiketGold(jenis_tiket, jumlah_tiket)
  else:
    print("Jenis tiket tidak valid.")
    return

  # Menghitung total harga tiket
  total_harga = tiket.harga_tiket()

  # Menampilkan output
  print(f"Total Harga Tiket: Rp {total_harga}")

if __name__ == "__main__":
  main()