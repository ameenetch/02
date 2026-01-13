def water_plants(plant_list : list)->None:
    print("Opening watering system")
    try :
        for x in plant_list:
            x + ""
            print(f"Watering {x}")
    except :
        print(f"Error: Cannot water {x} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() :
    lst = ["tomato","lettuce","carrot"]
    lst2 = ["tomato", None]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(lst)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(lst2)

    print("\nCleanup always happens, even with errors!")


test_watering_system() 