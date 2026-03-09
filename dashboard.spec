# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# CustomTkinter path identified: 
# C:\Users\admin\Documents\porject\berry-vitals-monitor-1\.venv\Lib\site-packages\customtkinter
ctk_path = os.path.join(os.getcwd(), '.venv', 'Lib', 'site-packages', 'customtkinter')

added_files = [
    (ctk_path, 'customtkinter/'),
    ('models/', 'models/'),
    ('water/config.py', 'water/'),
    ('water/berry_protocol.py', 'water/'),
    ('water/ble_connector.py', 'water/'),
    ('water/signal_processing.py', 'water/'),
    ('water/feature_extraction.py', 'water/'),
    ('water/hydration_engine.py', 'water/'),
    ('water/inference_engine.py', 'water/'),
    ('water/ppg_simulator.py', 'water/'),
]

# Collect any additional data files if needed (e.g. for matplotlib)
# added_files += collect_data_files('matplotlib')

a = Analysis(
    ['water/dashboard.py'],
    pathex=['water'],
    binaries=[],
    datas=added_files,
    hiddenimports=['bleak', 'customtkinter', 'pandas', 'matplotlib.backends.backend_tkagg', 'scipy.signal', 'joblib'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PPG_Hydration_Monitor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PPG_Hydration_Monitor',
)
