def  check_temperature(temp_str)-> int | None:
    
    """the function where w handle first if the 
    input is correct using try execpt blocks, then handle every case 
    if its correct"""
    # 
    # if temp_str is None: 
    #     return None
    # 
    print(f"Testing temperature: {temp_str}")
    try : 
        temp = int(temp_str)
        
    except :
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if 0 < temp < 41 :
        print(f"Temperature {temp}°C is perfect for plants!\n")
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    return temp

def  test_temperature_input() :

    """the function where everething start we test 
        our check_temperature function, by some tests"""
    
    print("=== Garden Temperature Checker ===\n")
    try : 
        check_temperature("25")
        check_temperature("abc")
        check_temperature("100")
        check_temperature("-50")
    except :
        print("Wrong usage: check_temperature takes one argm")
    else:
        print("All tests completed - program didn't crash!")

test_temperature_input()

