from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('g:\\tooldev\\sscomplus_src\\sscomplus.py', base=base, targetName = 'sscomplus')
]

setup(name='sscomplus_src',
      version = '1.01',
      description = 'hello',
      options = dict(build_exe = buildOptions),
      executables = executables)
