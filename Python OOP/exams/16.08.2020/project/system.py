from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    HARDWARE_MAPPER = {
        "PowerHardware": PowerHardware,
        'HeavyHardware': HeavyHardware
    }

    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def find_hardware(list_of_hardware, name_of_hardware):
        for hardware in list_of_hardware:
            if hardware.name == name_of_hardware:
                return hardware

    @staticmethod
    def find_software(list_of_software, name_of_software):
        for software in list_of_software:
            if software.name == name_of_software:
                return software

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.find_hardware(System._hardware, hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as e:
            return str(e)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.find_hardware(System._hardware, hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception as e:
            return str(e)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = System.find_hardware(System._hardware, hardware_name)
        software = System.find_software(System._software, software_name)
        if hardware is not None and software is not None:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis" + '\n'
        result += f"Hardware Components: {len(System._hardware)}" + '\n'
        result += f"Software Components: {len(System._software)}" + '\n'
        result += f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / " \
                  f"{sum([h.memory for h in System._hardware])}\n"
        result += f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / " \
                  f"{sum([h.capacity for h in System._hardware])}\n"

        return result.rstrip()

    @staticmethod
    def system_split():
        result = ''

        for hardware in System._hardware:
            num_of_exspress = len(
                [es for es in hardware.software_components if es.__class__.__name__ == 'ExpressSoftware'])
            num_light = len([es for es in hardware.software_components if es.__class__.__name__ == 'LightSoftware'])
            memory_consumption = sum([s.memory_consumption for s in hardware.software_components])
            capacity_consumption = sum([s.capacity_consumption for s in hardware.software_components])
            names = ', '.join([s.name for s in hardware.software_components])
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: {num_of_exspress}\n"
            result += f"Light Software Components: {num_light}\n"
            result += f"Memory Usage: {memory_consumption} / {hardware.memory}\n"
            result += f"Capacity Usage: {capacity_consumption} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            result += f"Software Components: {names if names else None}"

        return result
