#!/usr/bin/env python

import comtypes
import comtypes.client
import ctypes
import ctypes.wintypes

class IDesktopWallpaper(comtypes.IUnknown):
    _iid_ = comtypes.GUID('{B92B56A9-8b55-4e14-9a89-0199bbb6f93b}')
    _methods_ = (
        comtypes.COMMETHOD([], comtypes.HRESULT, 'SetWallpaper',
            (['in', 'unique'], ctypes.wintypes.LPCWSTR, "monitorID"),
            (['in'], ctypes.wintypes.LPWSTR, "wallpaper"),
        ),
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetWallpaper',
            (['in', 'unique'], ctypes.wintypes.LPCWSTR, "monitorID"),
            (['out', 'string'], ctypes.POINTER(ctypes.wintypes.LPWSTR), "wallpaper"),
        ),
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetMonitorDevicePathAt',
            (['in'], ctypes.wintypes.UINT, "monitorIndex"),
            (['out', 'string'], ctypes.POINTER(ctypes.wintypes.LPWSTR), "monitorID"),
        ),
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetMonitorDevicePathCount', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetMonitorRECT', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'SetBackgroundColor', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetBackgroundColor', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'SetPosition', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetPosition', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'SetSlideshow', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetSlideshow', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'SetSlideshowOptions', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetSlideshowOptions', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'AdvanceSlideshow', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetStatus', ), # todo
        comtypes.COMMETHOD([], comtypes.HRESULT, 'Enable', ), # todo
    )

CLSID_DesktopWallpaper = comtypes.GUID("{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}")

dw = comtypes.client.CreateObject(CLSID_DesktopWallpaper, interface=IDesktopWallpaper)

monitorid = dw.GetMonitorDevicePathAt(0)

wppath = dw.GetWallpaper(monitorid)
print(wppath)

dw.Release()