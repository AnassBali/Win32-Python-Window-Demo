from win32api import *
from win32gui import *
import win32con

def OnPaint(hWnd, message, wParam, lParam):
   hDC, paintStruct = BeginPaint(hWnd)
   rect = GetClientRect(hWnd)
   DrawText(
            hDC,
            'Hello send by Python via Win32!',
            -1,
            rect,
            win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER)
   EndPaint(hWnd, paintStruct)
   return 0

def OnDestroy(Hwnd, Msg1, wParm3 , lParam4):
   print('Destroy is triggered') 
   PostQuitMessage(0) # Beëindig de toepassing.
   return 0

def OnDefault(Hwnd, Msg1, wParm3 , lParam4):
   return DefWindowProc(Hwnd, Msg1, wParm3, lParam4)

# Berichtafhandelingsmap
msgMap = {
    win32con.WM_DESTROY: OnDestroy,
    win32con.WM_PAINT: OnPaint,
    win32con.WM_APP: OnDefault,
    win32con.WM_ASKCBFORMATNAME: OnDefault,
    win32con.WM_ACTIVATEAPP: OnDefault,
    win32con.WM_CANCELMODE: OnDefault,
    win32con.WM_HELP: OnDefault,
    win32con.WM_ACTIVATEAPP: OnDefault,
    win32con.WM_ACTIVATE: OnDefault
}

wc = WNDCLASS()
wc.lpszClassName = 'YPTF Example 1'
wc.lpfnWndProc = msgMap
hinst = wc.hInstance = GetModuleHandle(None)


try:
   wndClassAtom = RegisterClass(wc)
except Exception as e:
   print(e)
   raise(e)

if __name__ == '__main__':
   style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
   hwnd = CreateWindow(wndClassAtom, "Taskbar", style, 50, 50, 500, 500, 0, 0, hinst, None)
   ShowWindow(hwnd,win32con.SW_SHOWNORMAL)
   UpdateWindow(hwnd)
   PumpMessages()
   print('done.')
