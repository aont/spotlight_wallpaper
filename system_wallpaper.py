#!/usr/bin/env python

import comtypes
import comtypes.client

CLSID_DesktopWallpaper = comtypes.GUID("{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}")
CLSID_IDesktopWallpaper = comtypes.GUID("{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}")

mod = comtypes.client.GetModule('shobjidl.tlb')

dw = comtypes.client.CreateObject(CLSID_DesktopWallpaper, interface=mod.IDesktopWallpaper)

monitorid = dw.GetMonitorDevicePathAt(0)

wppath = dw.GetWallpaper(monitorid)
print(wppath)

dw.Release()
