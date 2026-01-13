class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass


class GardenManager:
    water_times_left = 2
    plants_list=[]
    def __init__(self , plant_name:str, water_level:int, sunlight_hours:int ):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
    
    def add_plant(self):
        try :
            if self.plant_name == "" or self.plant_name == None:
                raise PlantError("Plant name cannot be empty!\n")
        except PlantError as e:
            print("Error adding plant: ",e)
            return
        else:
            GardenManager.plants_list.append(self)
            print(f"Added {self.plant_name} successfully")



    def  check_plant_health(self):
        try :
            if self.water_level > 10 or self.water_level < 1:
                if self.water_level > 10:
                    raise WaterError(f"Error checking {self.plant_name}: Water level {self.water_level} is too high (max 10)\n")
                elif self.water_level < 1:
                    raise WaterError(f"Error checking {self.plant_name}: Water level {self.water_level} is too low (min 1)\n")

            elif self.sunlight_hours > 12 or self.sunlight_hours < 1:
                if self.sunlight_hours > 12:
                    raise PlantError(f"Error: Sunlight hours {self.sunlight_hours} is too high (max 12)\n")
                elif self.sunlight_hours < 2:
                    raise PlantError(f"Error: Sunlight hours {self.sunlight_hours} is too low (min 2)\n")
            
            else:
                print(f"{self.plant_name}: healthy (water: {self.water_level}, sun: {self.sunlight_hours})")

        except WaterError as e:
            print(e)
        except PlantError as e:
            print(e)
        

    def water_plants(self ,list_plant):
        print("Opening watering system")
        try :
            for x in list_plant:
                if GardenManager.water_times_left == 0:
                    raise WaterError(f"Error ther is no left water to water the {self.x}\n")
                print(f"Watering {x.plant_name} - success")
                GardenManager.water_times_left-=1
        except WaterError as e:
            print(e)
        except :
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)\n")
    
    def recover_water_error(self):
        try :
            if GardenManager.water_times_left == 0:
                raise WaterError("Not enough water in the tank!")
        except GardenError as e:
            print("Caught GardenError: ",e)
        finally:
            print("System recovered and continuing...\n")


def main():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    plant1 = GardenManager("tomato" , 5 , 8)
    plant2 = GardenManager("lettuce" , 15 , 8)
    plant3 = GardenManager("" , 15 , 8)
    plant1.add_plant()
    plant2.add_plant()
    plant3.add_plant()
    print("Watering plants...")
    plant1.water_plants(GardenManager.plants_list)
    print("Checking plant health...")
    plant1.check_plant_health()
    plant2.check_plant_health()
    print("plant1ing error recovery...")
    plant1.recover_water_error()
    print("Garden management system plant1 complete!")


main()