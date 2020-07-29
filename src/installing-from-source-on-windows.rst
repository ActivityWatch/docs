Installing from source (on Windows)
===================================

This was a guide hastily written by :gh-user:`ErikBjare` when he had to build on Windows once, it is not complete.

 - Install Git for Windows (including Git Bash)

 - Install MinGW

 - Rename C:/MinGW/mingw-make.exe to C:/MinGW/make.exe

    - :code:`cp C:\\MinGW\\mingw32-make.exe C:\\MinGW\\make.exe`

 - Set PATH to use MinGW

    - :code:`SET PATH=C:\\MinGW\\bin;%PATH%`

 - Install Python 3.5.4

 - Install Poetry

 - Install PyInstaller

   - :code:`pip install pyinstaller`
   - Add PyInstaller script to PATH: :code:`SET PATH=C:\\Users\User\\AppData\\Roaming\\Python\\Python35\\Scripts`
