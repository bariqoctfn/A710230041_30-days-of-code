class Employee:
  def __init__(self, name, age, salary):
    self.__name = name
    self.__age = age
    self.__salary = salary

  def set_name(self, name):
    self.__name = name

  def set_age(self, age):
    self.__age = age

  def set_salary(self, salary):
    self.__salary = salary

  def get_name(self):
    return self.__name

  def get_age(self):
    return self.__age

  def get_salary(self):
    return self.__salary

# Membuat objek baru dari class Employee
karyawan = Employee("Budi", 30, 5000000)

# Mengubah nilai atribut
karyawan.set_name("Andi")
karyawan.set_age(32)
karyawan.set_salary(6000000)

# Mendapatkan nilai atribut
nama = karyawan.get_name()
usia = karyawan.get_age()
gaji = karyawan.get_salary()

# Mencetak informasi karyawan
print(f"Nama: {nama}")
print(f"Usia: {usia}")
print(f"Gaji: {gaji}")
