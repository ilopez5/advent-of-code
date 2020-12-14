import pdb

# DAY 1
def find_fuel():
    with open("day1input.txt", 'r') as fd:
        masses = fd.read().split()
    
    total_fuel = 0
    for mass in masses:
        total_fuel += (int(mass) // 3) - 2
    
    return total_fuel

def find_fuel_alt():
    with open("day1input.txt", 'r') as fd:
        masses = fd.read().split()
    
    total_fuel = 0
    for mass in masses:
        fuel = (int(mass) // 3) - 2     # calculate fuel needed for module
        while fuel > 0:                 # while fuel > 0
            total_fuel += fuel
            fuel = ((fuel // 3) - 2)    # update fuel needed for subsequent fuel
    return total_fuel

if __name__ == "__main__":
    pdb.run()
    print(find_fuel_alt())
