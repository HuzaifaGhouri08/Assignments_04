C: int=  299792458
def energy():
  mass_in_kg = float(input("Enter kilo of mass:"))
  energy_in_joules: float = mass_in_kg * (C ** 2)

  print("e = m * C^2...")
  print("Mass = "+str(mass_in_kg) + "kg")
  print("C = " + str(C) + "m/s")
  print("e = " + str(energy_in_joules) +  "Joules of Energy")

if __name__ == "__main__":
  energy()
