def check_temperature(temp_str: str) -> int | None:

    """the function where w handle first if the
    input is correct using try execpt blocks, then handle every case
    if its correct"""

    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return

    try:
        if temp > 40:
            raise ValueError(f"Error: {temp}°C is too hot "
                             f"for plants (max 40°C)\n")
        elif temp < 0:
            raise ValueError(f"Error: {temp}°C is too cold"
                             f" for plants (min 0°C)\n")
    except ValueError as e:
        print(e)
        return

    print(f"Temperature {temp}°C is perfect for plants!\n")
    return temp


def test_temperature_input():

    """the function where everething start we test
        our check_temperature function, by some tests"""

    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


test_temperature_input()
