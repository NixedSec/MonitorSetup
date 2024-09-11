#needs to be run as admin to read from graphics configuration
import winreg as wrg
errorFound = False
monitors = []

location = wrg.HKEY_LOCAL_MACHINE
baseLocation = r"SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Configuration"

regKey = wrg.OpenKeyEx(location, baseLocation)

monitorKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0))
# check monitor amount
monitorCount = 0
try:
    while (True):
        print(wrg.EnumKey(regKey, monitorCount))
        monitors.append(wrg.EnumKey(regKey, monitorCount))
        monitorCount += 1
        print(monitorCount)
        if (monitorCount >= 2):
            errorFound = True
except:
    print ("all keys")

# check/set values
if (errorFound != True):
    try:
        currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\00\\00", 0, wrg.KEY_ALL_ACCESS)
        if (wrg.QueryValueEx(currentKey, "Rotation")[0] != 1):
            print (wrg.QueryValueEx(currentKey, "Rotation"))
            wrg.SetValueEx(currentKey, "Rotation", 0, wrg.REG_DWORD, 1)

    except Exception as f:
        print (f)

    try:
        currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\01\\00", 0, wrg.KEY_ALL_ACCESS)
        if (wrg.QueryValueEx(currentKey, "Rotation")[0] != 2):
            print (wrg.QueryValueEx(currentKey, "Rotation"))
            wrg.SetValueEx(currentKey, "Rotation", 0, wrg.REG_DWORD, 2)
    except Exception as f:
        print (f)

    try:
        currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\01", 0, wrg.KEY_ALL_ACCESS)
        if (wrg.QueryValueEx(currentKey, "Position.cx")[0] != 4294966396):
            print (wrg.QueryValueEx(currentKey, "Position.cx"))
            wrg.SetValueEx(currentKey, "Position.cx", 0, wrg.REG_DWORD, 4294966396)
    except Exception as f:
        print (f)

    try:
        currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\01", 0, wrg.KEY_ALL_ACCESS)
        if (wrg.QueryValueEx(currentKey, "Position.cy")[0] != 4294967052):
            print (wrg.QueryValueEx(currentKey, "Position.cy"))
            wrg.SetValueEx(currentKey, "Position.cy", 0, wrg.REG_DWORD, 4294967052)
    except Exception as f:
        print (f)

if (errorFound):
    print ("Error")

    try:
        print (monitorCount)
        while (monitorCount > 0):
            monitorKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0), 0, wrg.KEY_ALL_ACCESS)

        try:
            print ("Subkeys deletion")
            try:
                currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\00\\00", 0, wrg.KEY_ALL_ACCESS)
                wrg.DeleteKey(currentKey, "")
            except Exception as f:
                print (f)

            try:
                currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\01\\00", 0, wrg.KEY_ALL_ACCESS)
                wrg.DeleteKey(currentKey, "")
            except Exception as f:
                print (f)

            try:
                currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\00", 0, wrg.KEY_ALL_ACCESS)
                wrg.DeleteKey(currentKey, "")
            except Exception as f:
                print (f)

            try:
                currentKey = wrg.OpenKeyEx(location, baseLocation + r"\\" + wrg.EnumKey(regKey, 0) + "\\01", 0, wrg.KEY_ALL_ACCESS)
                wrg.DeleteKey(currentKey, "")
            except Exception as f:
                print (f)
        except Exception as e:
            print (e)

        monitorCount -= 1
        wrg.DeleteKey(monitorKey, "")
    except Exception as e:
        print (e)
        print ("all keys deleted")

print ("no error detected")

regKey.Close()
monitorKey.Close()
