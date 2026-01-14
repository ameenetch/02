class GardenError(Exception):

    """we can say that class is generale
    we can raise it for any kind of Errors in the
    garden, inheritign from the EXception class make him
    a child so he can also be an exception """

    pass


class PlantError(GardenError):

    """this class is a specialized for error that is in relation with plants"""

    pass


class WaterError(GardenError):

    """this class is a specialized for error that is in relation with plants"""

    pass


def raising_plant_error():

    """function to raise a plant kind of errors """

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print("Caught PlantError: ", e)


def raising_water_error():

    """function to raise a water kind of errors """

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print("Caught WaterError: ", e)


def raising_both():

    """this function raise water and plant errors due to GardenError
    class, the parent of other errors"""

    print("Testing catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)


def test_custom_errors(choise: int):
    if (choise == 1):
        raising_plant_error()

    elif (choise == 2):
        raising_water_error()

    elif (choise == 3):
        raising_both()

    else:
        print("invalide choise")


def main():
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors(1)
    test_custom_errors(2)
    test_custom_errors(3)
    # raising_both()
    print("\nAll custom error types work correctly!")


main()
