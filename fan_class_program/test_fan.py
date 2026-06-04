from fan_class_file import FanFile, Fan

fan_1= FanFile(Fan.fast, 10, "yellow", True)
fan_2= FanFile(Fan.medium, 5, "blue", False)

print(f"Fan 1: {fan_1}")
print(f"Fan 2: {fan_2}")