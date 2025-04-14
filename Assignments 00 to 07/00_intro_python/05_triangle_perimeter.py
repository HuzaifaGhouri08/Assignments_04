def triangle_perimeter():
  
  print("This program calculates the perimeter of a triangle.")
  side_a: float = float(input("Enter the length of side A. "))
  side_b: float = float(input("Enter the length of side B. "))
  side_c: float = float(input("Enter the length of side C. "))

  total : float = float (side_a + side_b + side_c)
  print(f'The total perimeter of the triangle is {total}')

if __name__ == "__main__":
  triangle_perimeter()