#!/usr/bin/env python
import ctypes

_dll = ctypes.WinDLL('system_wallpaper.dll')
_dll.system_wallpaper.restype = ctypes.c_wchar_p
_dll.system_wallpaper.argtypes = []

print(_dll.system_wallpaper())

# ).value.decode("UTF-16LE"))


#
# import comtypes
# import comtypes.client
# import ctypes

# # import win32com
# # import win32com.client

# # win32com.client.

# CLSID_DesktopWallpaper = comtypes.GUID("{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}")
# CLSID_IDesktopWallpaper = comtypes.GUID("{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}")
# # desktop_wallpaper = comtypes.client.CreateObject(CLSID_DesktopWallpaper, interface=CLSID_IDesktopWallpaper)

# hr = comtypes.CoInitialize()
# #(
# # idesktop_wallpaper = 
# comtypes.
# desktop_wallpaper = comtypes.CoCreateInstance(CLSID_DesktopWallpaper, clsctx=comtypes.CLSCTX_ALL)
# # CoCreateInstance

# monitorid = comtypes.c_wchar_p()
# desktop_wallpaper.GetMonitorDevicePathAt(0, monitorid)
# print(monitorid.value)
# desktop_wallpaper.Release()
# # idesktop_wallpaper.Release()

# comtypes.CoUninitialize()
#####################

# import ctypes
# user32_dll = ctypes.WinDLL('user32.dll')
# user32_dll.SystemParametersInfo.restype = ctypes.c_bool
# user32_dll.SystemParametersInfo.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]

# SPI_GETDESKWALLPAPER=0x0073

# user32_dll.SystemParametersInfo(SPI_GETDESKWALLPAPER, 

#import ctypes
# import win32com.client

# "IDesktopWallpaper"
# "{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}"
# "{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}"
#desktop_wallpaper = win32com.client

# win32com.client.
#wallpaper = ctypes.c_char_p()
#desktop_wallpaper.GetWallpaper(None, wallpaper)
#print(wallpaper.value.decote('utf-8'))
# win32com.client.
