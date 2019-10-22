#!/usr/bin/env python

import comtypes
import comtypes.client

CLSID_DesktopWallpaper = comtypes.GUID("{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}")
CLSID_IDesktopWallpaper = comtypes.GUID("{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}")

mod = comtypes.client.GetModule('shobjidl.tlb')

dw = comtypes.client.CreateObject(CLSID_DesktopWallpaper, interface=mod.IDesktopWallpaper)

monitorid = dw.GetMonitorDevicePathAt(0)
# print(monitorid)
wppath = dw.GetWallpaper(monitorid)
print(wppath)

dw.Release()


# import pythoncom

# # for i in dir(pythoncom):
#   # print("%s:%s:%s"%(i, pythoncom.get(i), type(pythoncom.get(i))))
#   #print("%s"%(i))
# CLSID_DesktopWallpaper = "{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}"
# CLSID_IDesktopWallpaper = "{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}"

# PYIID_DesktopWallpaper = pythoncom.MakeIID(CLSID_DesktopWallpaper)
# PYIID_IDesktopWallpaper = pythoncom.MakeIID(CLSID_IDesktopWallpaper)

# import _shobjidl
# import win32com.client
# pythoncom.CoInitialize()



# dw = pythoncom.CoCreateInstance(CLSID_DesktopWallpaper, None, pythoncom.CLSCTX_ALL, PYIID_IDesktopWallpaper)
# # dw = pythoncom.CoCreateInstance(CLSID_DesktopWallpaper, None, pythoncom.CLSCTX_ALL, pythoncom.IID_IUnknown)
# # dw = win32com.client.CastTo(dw, PYIID_IDesktopWallpaper)

# for i in dir(dw):
#   print(i)
# print(dw)
# # monitorid = dw.GetMonitorDevicePathAt(0)
# # print(monitorid)
# # dw = pythoncom.CoCreateInstance(CLSID_DesktopWallpaper, iunk, pythoncom.CLSCTX_ALL, PYIID_IDesktopWallpaper)
# # dw = pythoncom.CoCreateInstance(PYIID_DesktopWallpaper, None, pythoncom.CLSCTX_ALL, PYIID_IDesktopWallpaper)
# dw.Release()
# pythoncom.CoUninitialize()