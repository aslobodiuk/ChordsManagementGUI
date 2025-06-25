from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    "packages": ["requests", "python_dotenv"]
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)