from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_instance_by_name(hardware_name, System._hardware)
        if hardware is None:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_instance_by_name(hardware_name, System._hardware)
        if hardware is None:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.get_instance_by_name(hardware_name, System._hardware)
        software = System.get_instance_by_name(software_name, System._software)

        if hardware is not None and software is not None:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        memory_taken = sum([x.memory_consumption for x in System._software])
        total_memory = sum([x.memory for x in System._hardware])
        capacity_taken = sum([x.capacity_consumption for x in System._software])
        total_capacity = sum([x.capacity for x in System._hardware])

        result = f"System Analysis\n"\
                 f'Hardware Components: {len(System._hardware)}\n'\
                 f'Software Components: {len(System._software)}\n'\
                 f'Total Operational Memory: {memory_taken} / {total_memory}\n' \
                 f''f'Total Capacity Taken: {capacity_taken} / {total_capacity}'

        return result

    @staticmethod
    def system_split():
        result = []

        for h in System._hardware:

            software_components = ', '.join([s.name for s in h.software_components]) if h.software_components else None
            output = f"""Hardware Component - {h.name}
Express Software Components: {len([s for s in h.software_components if s.software_type == 'Express'])}
Light Software Components: {len([s for s in h.software_components if s.software_type == 'Light'])}
Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}
Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}
Type: {h.hardware_type}
Software Components: {software_components}
""".strip()
            result.append(output)
        return '\n'.join(result)

    @staticmethod
    def get_instance_by_name(name, iterable):
        for obj in iterable:
            if obj.name == name:
                return obj
        return None



