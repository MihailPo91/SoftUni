from project.driver import Driver


class DriverCreator:

    @staticmethod
    def create_driver(driver_name: str):
        return Driver(driver_name)