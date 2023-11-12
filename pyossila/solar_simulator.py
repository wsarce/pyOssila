from enum import Enum
import serial
from serial.tools import list_ports


class LEDChannels:
    NM390 = 1
    NM450 = 2
    NM515 = 3
    COOL_WHITE = 4
    WARM_WHITE = 5
    NM600 = 6
    NM630 = 7
    NM660 = 8
    NM730 = 9
    NM850 = 10
    NM950 = 11


class SettingCommands:
    IRRADIANCE = '<power:'
    LED_POWER = '<ch'
    SAVE_SETTINGS = '<save:1>'
    SHUTTER = '<shutter:'

    @staticmethod
    def get_command(command, parameters=None):
        if command == SettingCommands.SAVE_SETTINGS:
            return SettingCommands.SAVE_SETTINGS
        elif command == SettingCommands.SHUTTER:
            assert len(parameters) == 1, "One parameter needed for SHUTTER command!"
            return f"{SettingCommands.SHUTTER}{parameters[0]}>"
        elif command == SettingCommands.LED_POWER:
            assert len(parameters) == 2, "Two parameters needed for LED_POWER command!"
            return f"{SettingCommands.LED_POWER}{parameters[0]}:{parameters[1]}>"
        elif command == SettingCommands.IRRADIANCE:
            assert len(parameters) == 1, "One parameter needed for IRRADIANCE command!"
            return f"{SettingCommands.IRRADIANCE}{parameters[0]}>"
        else:
            raise ValueError(f"Invalid command: {command}")


class QueryCommands:
    IRRADIANCE = '<power?>'
    LED_POWER = '<ch'
    DEVICE_NAME = '<device?>'
    FIRMWARE_NUMBER = '<firmware?>'
    SERIAL_NUMBER = '<serial?>'
    TEMPERATURE = '<temp?>'
    SHUTTER = '<shutter?>'
    LED_TIME = '<ledtime?>'
    ERROR = '<error?>'

    @staticmethod
    def get_command(command, parameters=None):
        if command == QueryCommands.IRRADIANCE:
            return QueryCommands.IRRADIANCE
        elif command == QueryCommands.LED_POWER:
            assert len(parameters) == 1, "Two parameters needed for LED_POWER query!"
            return f"{QueryCommands.LED_POWER}{parameters[0]}?>"
        elif command == QueryCommands.DEVICE_NAME:
            return QueryCommands.DEVICE_NAME
        elif command == QueryCommands.FIRMWARE_NUMBER:
            return QueryCommands.FIRMWARE_NUMBER
        elif command == QueryCommands.SERIAL_NUMBER:
            return QueryCommands.SERIAL_NUMBER
        elif command == QueryCommands.TEMPERATURE:
            return QueryCommands.TEMPERATURE
        elif command == QueryCommands.SHUTTER:
            return QueryCommands.SHUTTER
        elif command == QueryCommands.LED_TIME:
            return QueryCommands.LED_TIME
        elif command == QueryCommands.ERROR:
            return QueryCommands.ERROR


class ErrorList(Enum):
    NO_ERROR = 0
    LOW_VOLTAGE_DETECTED = 1
    HIGH_TEMPERATURE = 2
    LED_FAULT = 3


class OssilaSolarSimulator:
    def __init__(self, comport, timeout=None):
        self.ossila_port = serial.Serial(comport, timeout=timeout)

    def modify_irradiance(self, new_level):
        assert type(new_level) is int
        command = SettingCommands.get_command(SettingCommands.IRRADIANCE, [new_level])
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip().split(':')[1]
        if response[0] == command.split(':')[0] and response[1] == command.split(':')[1]:
            return True
        return False

    def modify_led_power(self, channel, new_level):
        assert type(channel) is int
        assert type(new_level) is int
        command = SettingCommands.get_command(SettingCommands.LED_POWER, [channel, new_level])
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip().split(':')
        if response[0] == command.split(':')[0] and response[1] == command.split(':')[1]:
            return True
        return False

    def save_settings(self):
        command = SettingCommands.get_command(SettingCommands.SAVE_SETTINGS)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip().split(':')
        if response[0] == command.split(':')[0] and response[1] == command.split(':')[1]:
            return True
        return False

    def modify_shutter(self, new_shutter):
        assert type(new_shutter) is int
        command = SettingCommands.get_command(SettingCommands.SHUTTER, [new_shutter])
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip().split(':')
        if response[0] == command.split(':')[0] and response[1] == command.split(':')[1]:
            return True
        return False

    def get_irradiance(self):
        command = QueryCommands.get_command(QueryCommands.IRRADIANCE)
        self.ossila_port.write(command.encode())
        return int(self.ossila_port.readline().decode().strip().split('>')[0].split(':')[1])

    def get_led_power(self, channel):
        assert type(channel) is int
        command = QueryCommands.get_command(QueryCommands.LED_POWER, [channel])
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return int(response.split('>')[0].split(':')[1])
        return -1

    def get_device_name(self):
        command = QueryCommands.get_command(QueryCommands.DEVICE_NAME)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return response.split('>')[0].split(':')[1]
        return -1

    def get_firmware_number(self):
        command = QueryCommands.get_command(QueryCommands.FIRMWARE_NUMBER)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return response.split('>')[0].split(':')[1]
        return -1

    def get_serial_number(self):
        command = QueryCommands.get_command(QueryCommands.SERIAL_NUMBER)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return response.split('>')[0].split(':')[1]
        return -1

    def get_temperature(self):
        command = QueryCommands.get_command(QueryCommands.TEMPERATURE)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return response.split('>')[0].split(':')[1]
        return -1

    def get_shutter(self):
        command = QueryCommands.get_command(QueryCommands.SHUTTER)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return response.split('>')[0].split(':')[1]
        return -1

    def get_led_time(self):
        command = QueryCommands.get_command(QueryCommands.LED_TIME)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return response.split('>')[0].split(':')[1]
        return -1

    def get_error_state(self):
        command = QueryCommands.get_command(QueryCommands.ERROR)
        self.ossila_port.write(command.encode())
        response = self.ossila_port.readline().decode().strip()
        if command.split('?')[0] == response.split(':')[0]:
            return ErrorList(int(response.split('>')[0].split(':')[1]))
        return -1

