import math

height = int(input("What is the height of the wall?"))
width = int(input("What is the width of the wall?"))
coverage = int(input("What area can a can cover?"))

def number_of_paint_can(height = height, width = width, coverage = coverage):
    cans_needed = math.ceil((height * width) / coverage)
    print(f"A total of {cans_needed} cans are needed for the paintings")

number_of_paint_can()