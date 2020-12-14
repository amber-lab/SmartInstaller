# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:02:59 2018

@author: HP_Server
"""
import os
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {}

os.environ['TCL_LIBRARY'] = "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_86\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_86\\tcl\\tk8.6"

# GUI applications require a different base on Windows (the default is for a
# console application).

base = "Win32GUI"

#if sys.platform == "win32":
#    base = "Win32GUI"

setup(name = "LAB-SmartInstaller",
      version = "2.0",
      description = "LAB-SmartInstaller",
#      options = {"build_exe": build_exe_options},
      executables = [Executable("iLG_SmartInstall_v2.0.py", base=base, icon = "1icon.ico")])

