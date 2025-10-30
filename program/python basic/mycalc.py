#from idlelib.debugobj_r import remote_object_tree_item
from mypackage.interest_calculation import simle_Interest
from mypackage.shape import area_of_circle,area_of_rectangle
prin=float(input("Prin: "))
ny=float(input("Ny: "))
roi=float(input("Roi: "))
#remote_object_tree_item()
print(f'Simple Interest: {simle_Interest(prin=prin,ny=ny,roi=roi)[0]} '
      f'Amount:{simle_Interest(prin=prin,ny=ny,roi=roi)[1]}')
print(f'Area of circle: {area_of_circle(10)}\n'
    f'Perimeter of circle: {area_of_circle(10)}'
)
