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


class GardenManager:

    """the class that manage the plant verification name and check health
    and watering th plants """

    water_times_left = 2
    plants_list = []

    def __init__(self, plant_name, water_level, sunlight_hours):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def add_plant(self):

        """check if the input name is valide then add it
        to the list plant to manage them all"""

        try:
            if self.plant_name == "" or self.plant_name is None:
                raise PlantError("Plant name cannot be empty!\n")
        except PlantError as e:
            print("Error adding plant: ", e)
            return
        else:
            GardenManager.plants_list.append(self)
            print(f"Added {self.plant_name} successfully")

    def check_plant_health(self):

        """chekc the health : make sure the water level and sunlight hours
        in the perfect range for plants"""

        try:
            if self.water_level > 10 or self.water_level < 1:
                if self.water_level > 10:
                    raise WaterError(
                        f"Error checking {self.plant_name}: Water"
                        f" level {self.water_level} is too high (max 10)\n"
                    )

                elif self.water_level < 1:
                    raise WaterError(
                        f"Error checking {self.plant_name}: "
                        f"Water level {self.water_level} is too low (min 1)\n"
                    )

            elif self.sunlight_hours > 12 or self.sunlight_hours < 1:
                if self.sunlight_hours > 12:
                    raise PlantError(
                        f"Error: Sunlight hours {self.sunlight_hours}"
                        f" is too high (max 12)\n"
                    )

                elif self.sunlight_hours < 2:
                    raise PlantError(
                        f"Error: Sunlight hours {self.sunlight_hours}"
                        f" is too low (min 2)\n"
                    )

            else:
                print(f"{self.plant_name}: healthy (water:"
                      f" {self.water_level}, sun: {self.sunlight_hours})")

        except WaterError as e:
            print(e)
        except PlantError as e:
            print(e)

    def water_plants(self, list_plant):

        """watering all plant in the list """

        print("Opening watering system")
        try:
            for x in list_plant:
                if GardenManager.water_times_left == 0:
                    raise WaterError(f"Error ther is no left water to water"
                                     f" the {x.plant_name}\n")
                print(f"Watering {x.plant_name} - success")
                GardenManager.water_times_left -= 1
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def recover_water_error(self):
        """recover water problelme and fix them here """
        try:
            if GardenManager.water_times_left == 0:
                raise WaterError("Not enough water in the tank!")
        except GardenError as e:
            GardenManager.water_times_left += 10
            print("Caught GardenError: ", e)
        finally:
            print("System recovered and continuing...\n")


def main():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    plant1 = GardenManager("tomato", 5, 8)
    plant2 = GardenManager("lettuce", 15, 8)
    plant3 = GardenManager(None, 15, 8)
    plant1.add_plant()
    plant2.add_plant()
    plant3.add_plant()
    print("Watering plants...")
    plant1.water_plants(GardenManager.plants_list)
    print("Checking plant health...")
    plant1.check_plant_health()
    plant2.check_plant_health()
    print("Testing error recovery...")
    plant1.recover_water_error()
    print("Garden management system test complete!")


main()
