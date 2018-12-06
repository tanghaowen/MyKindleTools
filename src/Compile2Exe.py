import PyInstaller.__main__

PyInstaller.__main__.run([
    'epub2mobi.py',
    '--distpath=..//',
    '--clean',
    '--onefile',
    ])
PyInstaller.__main__.run([
    'sendToKindle.py',
    '--distpath=..//',
    '--clean',
    '--onefile',
    ])