def hitung_pangkat_dua():
  while True:
    try:
      bilangan = int(input("Masukkan bilangan bulat: "))
      break
    except ValueError:
      print("Input yang dimasukkan tidak valid!")

  pangkat_dua = bilangan ** 2
  print(f"Pangkat dua dari {bilangan} adalah {pangkat_dua}")

hitung_pangkat_dua()