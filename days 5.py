def bagi(x, y):
  try:
    hasil = x / y
  except ZeroDivisionError:
    print("Tidak dapat membagi dengan nol!")
    return None
  else:
    return hasil

# Contoh penggunaan fungsi

bilangan1 = 10
bilangan2 = 5

hasil_bagi = bagi(bilangan1, bilangan2)
print(f"{bilangan1} dibagi {bilangan2} = {hasil_bagi}")

bilangan1 = 10
bilangan2 = 0

hasil_bagi = bagi(bilangan1, bilangan2)
print(f"{bilangan1} dibagi {bilangan2} = {hasil_bagi}")
