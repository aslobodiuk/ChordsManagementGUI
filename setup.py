from setuptools import setup
import jaraco.text

APP = ['main.py']
OPTIONS = {
    'iconfile': 'icon.icns',
    'packages': ['requests', 'dotenv', 'chardet'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)