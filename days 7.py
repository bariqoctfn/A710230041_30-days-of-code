def hitung_nilai(nilai):
  total = 0
  for hasil in nilai:
    if hasil >= 85:
      print(f"{hasil} nilai bagus sekali ")
    elif hasil >= 60:
      print(f"{hasil} nilai cukup")
    else:
      print(f"{hasil} nilai buruk")
    total += hasil
  rata_rata = total / len(nilai)
  return total, rata_rata

nilai_ujian = [85, 72, 90, 65, 58]
total, rata_rata = hitung_nilai(nilai_ujian)

print(f"Total nilai ujian: {total}")
print(f"Rata-rata nilai ujian: {rata_rata:.2f}")
