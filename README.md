# pyOssila

### Parties Involved
Group: UNL Aerospace Club - Advanced eXperimental Payloads<br>
Developer: Walker Arce<br>

### Motivation
This Python library was written to facilitate closed-loop experimental testing of perovskite solar cells for extended periods of time, in collaboration with the National Renewable Energy Laboratory.

### Installation
Clone this repository, cd into the directory using either your virtual environment or your local environment, and run:
`python setup.py install`

### Usage
```
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
```

### Citation
```
@misc{Arce_pyOssila_2023,
      author = {Arce, Walker},
      month = {8},
      title = {{pyOssila}},
      url = {https://github.com/wsarce/pyOssila},
      year = {2023}
}
```
