#pragma comment( lib, "Ole32.lib" )
#include <windows.h>
#include <shobjidl.h>
#include <cstdio>

// ref: https://matthewvaneerde.wordpress.com/2012/10/10/changing-the-desktop-wallpaper-using-idesktopwallpaper/

class CoUninitializeOnExit {
public:
    CoUninitializeOnExit() {}
    ~CoUninitializeOnExit() { CoUninitialize(); }
};

class ReleaseOnExit {
public:
    ReleaseOnExit(IUnknown *p) : m_p(p) {}
    ~ReleaseOnExit() { if (NULL != m_p) { m_p->Release(); } }
private:
    IUnknown *m_p;
};

int _cdecl wmain(int argc, LPCWSTR argv[]) {
    
    HRESULT hr = CoInitialize(NULL);
    if (FAILED(hr)) {
        fwprintf(stderr, L"[error] CoInitialize returned 0x%08x", hr);
        return -__LINE__;
    }
    CoUninitializeOnExit cuoe;

    IDesktopWallpaper *pDesktopWallpaper = NULL;
    hr = CoCreateInstance(__uuidof(DesktopWallpaper), NULL, CLSCTX_ALL, IID_PPV_ARGS(&pDesktopWallpaper));
    if (FAILED(hr)) {
        fwprintf(stderr, L"[error] CoCreateInstance(__uuidof(DesktopWallpaper)) returned 0x%08x", hr);
        return -__LINE__;
    }
    ReleaseOnExit releaseDesktopWallpaper((IUnknown*)pDesktopWallpaper);
    

    LPWSTR monitorID;
    hr = pDesktopWallpaper->GetMonitorDevicePathAt(0, &monitorID);
    if(hr!=S_OK) {
        fwprintf(stderr, L"[error] IDesktopWallpaper::GetMonitorDevicePathAt returned 0x%08x", hr);
        return -__LINE__;
    }

    LPWSTR wallpaper;
    hr = pDesktopWallpaper->GetWallpaper(monitorID, &wallpaper);
    if (hr!=S_OK) {
        fwprintf(stderr, L"[error] IDesktopWallpaper::GetWallpaper returned 0x%08x", hr);
        return -__LINE__;
    }

    fwrite(wallpaper, wcslen(wallpaper)*sizeof(WCHAR), 1, stdout);
    printf("\n");

    return 0;
}