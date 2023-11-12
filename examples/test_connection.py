from pyossila.solar_simulator import OssilaSolarSimulator

# Reset the solar simulator
test = OssilaSolarSimulator('COM3')
test.modify_irradiance(100)
test.save_settings()
# Read the settings
print(f"Firmware Number: {test.get_firmware_number()}")
print(f"Error State: {test.get_error_state()}")
print(f"Serial Number: {test.get_serial_number()}")
print(f"Temperature: {test.get_temperature()}")
print(f"LED Time: {test.get_led_time()}")
print(f"Irradiance: {test.get_irradiance()}")
print(f"Shutter State: {test.get_shutter()}")
print(f"Device Name: {test.get_device_name()}")