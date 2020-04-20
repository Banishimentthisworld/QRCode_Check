from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = [r'QRCode_Check_Main.py', '-i', 'logo.ico', '-F','-w']
    run(opts)
