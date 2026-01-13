class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def raising_plant_error():
    print("Testing PlantError...")
    try :
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e :
        print("Caught PlantError: ",e)

def raising_water_error():
    print("Testing WaterError...")
    try :
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print("Caught WaterError: ",e)

def raising_both():
    
    print("Testing catching all garden errors...")

    try :
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try :
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)

def test_custom_errors(choise:int):
    if(choise == 1):
        raising_plant_error()
    elif(choise == 2):
        raising_water_error()
    elif(choise == 3):
        raising_both()
    else:
        print("invalide choise")

def main():
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors(1)
    # raising_plant_error()
    test_custom_errors(2)
    # raising_water_error()
    test_custom_errors(3)
    # raising_both()
    print("\nAll custom error types work correctly!")

main()
 