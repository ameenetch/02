def garden_operations(choise_your_error : int)->None:
    
    """testing the ValueError cases : when expecting the user 
    to give u and int and give you a non-integer input or division by zero ,
    open non-existed file , or a non valie key-value in dictionnary """
    if(choise_your_error == 1):
        """bad data conversion"""
        int("crashing")
    elif(choise_your_error == 2):
        """division by zero"""
        x = 2/0
    elif(choise_your_error == 3):
        """missing file"""
        open("missing.txt")
    elif(choise_your_error == 4):        
        """invalide key in dictionnary"""
        dictionnary = {}
        dictionnary["A"]
    else:
        print("invalide choise")



def test_error_types():
    """the first function run we going to """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try :
        int("string")
    except ValueError: 
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try :
        x = 2/0
    except ZeroDivisionError: 
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try :
        open("missing.txt")
    except FileNotFoundError: 
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try :
        dictionnary = {}
        dictionnary["A"]
    except KeyError: 
        print("Caught KeyError: 'missing\\_plant'\n")
    
    print("Testing multiple errors together...")
    try : 
        garden_operations(3)
    except :
        print("Caught an error, but program continues!\n")
        
    print("All error types tested successfully!")

# try:
test_error_types() 
# except TypeError:
#     print("Error: check args nbr ypu passed")