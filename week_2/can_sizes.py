import math

def main():
    radius = float(input("What is the radius of the can? "))
    height = float(input("What is the height of the can? "))
    cost = float(input("What is the cost of the can? "))
    volume = compute_volume(radius,height)
    surface_area =compute_surface_area(radius,height)
    storage_efficiency = compute_storage_efficiency(volume,surface_area)
    cost_efficiency = compute_cost_efficiency(volume,cost)
    print (f"This containter has a storage effiency of {volume:.2f}")
    print(f"The surface area of this can is {surface_area:.2f}.")
    print(f"This container has a storage efficiency of {storage_efficiency:.2f}")
    print(f"The cost efficiency of this container is {cost_efficiency}")

def compute_volume(radius,height):
    volume = math.pi*radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, height):
    storage_efficiency = volume / height
    return storage_efficiency

def compute_cost_efficiency(volume,cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()

