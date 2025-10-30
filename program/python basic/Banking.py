from mypackage.interest_calculation import simle_Interest, compund_Interest
prin=float(input("Principal: "))
ny=float(input("year: "))
roi=float(input("Rate of Interest: "))
si,amt=simle_Interest(prin=prin,ny=ny,roi=roi)
print(f"SI: {si} Amount: {amt} ")
amt=compund_Interest(prin=prin,ny=ny,roi=roi)
print(f"Amount: {amt}")