import pythoncom
import PyHook3 as pyHook

def onKeyboardEvent(event):
    print("Key:", str(event.Key))
    return True

#创建hook句柄
hm = pyHook.HookManager()
#监控键盘
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
#循环获取消息
pythoncom.PumpMessages()




