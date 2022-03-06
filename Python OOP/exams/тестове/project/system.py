from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.finding_hardware(hardware_name)
        if hardware is not None:
            es = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(es)
            System._software.append(es)

        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.finding_hardware(hardware_name)
        if hardware is not None:
            ls = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(ls)
            System._software.append(ls)

        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = System.finding_hardware(hardware_name)
        software = System.finding_software(software_name)
        if hardware is not None and software is not None:
            hardware.uninstall(software)
            System._software.remove(software)

        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        pass

    @staticmethod
    def system_split():
        pass

    @classmethod
    def finding_hardware(cls, hardware_name):
        for hardware in cls._hardware:
            if hardware.name == hardware_name:
                return hardware

        return None

    @classmethod
    def finding_software(cls, software_name):
        for software in cls._software:
            if software.name == software_name:
                return software

        return None
