def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    try:

        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!\n")

        elif water_level > 10 or water_level < 1:
            if water_level > 10:
                raise ValueError(f"Error: Water level {water_level} "
                                 f"is too high (max 10)\n")

            elif water_level < 1:
                raise ValueError(f"Error: Water level {water_level} "
                                 f"is too low (min 1)\n")

        elif sunlight_hours > 12 or sunlight_hours < 1:
            if sunlight_hours > 12:
                raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                                 f"is too high (max 12)\n")

            elif sunlight_hours < 2:
                raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                                 f"is too low (min 2)\n")

        return (f"Plant '{plant_name}' is healthy!\n")

    except ValueError as e:
        return (e)


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    print(check_plant_health("tomato", 5, 5))

    print("Testing empty plant name...")
    print(check_plant_health("", 5, 5))

    print("Testing bad water level...")
    print(check_plant_health("tomato", 15, 5))

    print("Testing bad sunlight hours...")
    print(check_plant_health("tomato", 5, 0))

    print("All error raising tests completed!")


test_plant_checks()
