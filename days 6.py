class Hewan:
  def bersuara(self):
    raise NotImplementedError("Metode bersuara() belum diimplementasikan")

class Kucing(Hewan):
  def bersuara(self):
    print("Meow!")

class Anjing(Hewan):
    def bersuara(self):
        print("Woof!")

def pelihara_hewan(hewan):
    hewan.bersuara()


kucing = Kucing()
anjing = Anjing()

pelihara_hewan(kucing)  # Output: Meow!
pelihara_hewan(anjing)  # Output: Woof!
