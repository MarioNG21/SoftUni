from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    HARDWARE_MAPPER = {
        'HeavyHardware': HeavyHardware,
        'PowerHardware': PowerHardware
    }

    SOFTWARE_MAPPER = {
        'LightSoftware': LightSoftware,
        'ExpressSoftware': ExpressSoftware
    }

    _hardware = []
    _software = []

    @staticmethod
    def _registration_of_software(name_of_software, capacity, memory, type_of_software, hardware_to_install) -> None:
        software = System.SOFTWARE_MAPPER[type_of_software](name_of_software, capacity, memory)
        try:
            hardware_to_install.install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def _get_hardware_by_name(name):
        for software in System._hardware:
            if software.name == name:
                return software

        return None

    @staticmethod
    def _get_software_by_name(name, list_of_software):
        for software in list_of_software:
            if software.name == name:
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
        hardware_to_install = System._get_hardware_by_name(hardware_name)
        if hardware_to_install is None:
            return 'Hardware does not exist'
        return System._registration_of_software(name, capacity_consumption, memory_consumption,
                                                'ExpressSoftware', hardware_to_install)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_to_install = System._get_hardware_by_name(hardware_name)
        if hardware_to_install is None:
            return 'Hardware does not exist'
        return System._registration_of_software(name, capacity_consumption, memory_consumption,
                                                'LightSoftware', hardware_to_install)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware_to_install = System._get_hardware_by_name(hardware_name)
        if hardware_to_install is not None:
            software_to_install = System._get_software_by_name(software_name)
            if software_to_install is not None:
                hardware_to_install.uninstall(software_to_install)

            else:
                return 'Some of the components do not exist'
        else:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        hardware_memory_sum = sum([h.memory for h in System._hardware])
        software_memory_sum = sum([h.used_memory for h in System._hardware])

        hardware_capacity_sum = sum([h.capacity for h in System._hardware])
        software_capacity_sum = sum([h.used_capacity for h in System._hardware])

        return f"System Analysis" + '\n' + \
               f"Hardware Components: {len(System._hardware)}" + '\n' + \
               f"Software Components: {len(System._software)}" + '\n' + \
               f"Total Operational Memory: {software_memory_sum} / {hardware_memory_sum}" + '\n' + \
               f"Total Capacity Taken: {software_capacity_sum} / {hardware_capacity_sum}"

    @staticmethod
    def system_split():
        result = ''

        for h in System._hardware:
            express_software = [es for es in h.software_components if es.__class__.__name__ == 'ExpressSoftware']
            light_software = [ls for ls in h.software_components if ls.__class__.__name__ == "LightSoftware"]
            total_memory = sum(soft.memory_consumption for soft in h.software_components)
            total_capacity = sum([soft.capacity_consumption for soft in h.software_components])
            names = ', '.join([soft.name for soft in h.software_components])

            result += f"Hardware Component - {h.name}" + '\n' + \
                      f"Express Software Components: {len(express_software)}" + '\n' + \
                      f"Light Software Components: {len(light_software)}" + '\n' + \
                      f"Memory Usage: {total_memory} / {h.memory}" + '\n' + \
                      f"Capacity Usage: {total_capacity} / {h.capacity}" + '\n' + \
                      f"Type: {h.TYPE}" + '\n' + \
                      f"Software Components: {names if names else None}" + '\n'

        return result.rstrip()

