from cx_Freeze import setup, Executable

# python setup.py bdist_mac --iconfile='logo.ico'
# python setup.py bdist_dmg
# python setup.py bdist_msi
# python setup.py bdist_rpm
# python setup.py bdist_wininst
# python setup.py bdist_exe



# Dependencies are automatically detected, but it might need
# fine tuning.

build_options = {'packages': [], 'excludes': []}


import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('app.py', base=base, target_name = 'tiktokdownloader')
]

setup(name='TiktokDownloader',
      version = '1.0',
      description = 'Download Tiktok Videos',
      iconfile = 'static/logo.ico',
      options = {'build_exe': build_options},
      executables = executables)
