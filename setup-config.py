from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('gui.pyw', base=base, target_name = 'PleoraConfig',icon="pleora.ico")
]

setup(name='Pleora Config',
      version = '1.0',
      description = 'Config for Pleora',
      options = {'build_exe': build_options},
      executables = executables)
