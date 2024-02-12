from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('pleora.pyw', base=base, target_name = 'Pleora',icon="pleora.ico")
]

setup(name='Pleora',
      version = '1.0',
      description = 'Pleora',
      options = {'build_exe': build_options},
      executables = executables)
