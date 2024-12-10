from distutils.core import setup
from setuptools import find_packages

setup(name='UKIT',
      description='A cross-platform cross-radio programming tool',
      packages=find_packages(include=["chirp*"]),
      include_package_data=True,
      version=0,
      url='UniversalKIT.com',
      python_requires=">=3.10,<4",
      install_requires=[
          'pyserial',
          'requests',
          'yattag',
          'suds',
      ],
      extras_require={
          'wx': ['wxPython'],
      },
      entry_points={
          'console_scripts': [
              "ukit=ukit.wxui:chirpmain",
              "ukitc=ukit.cli.main:main",
              "experttune=ukit.cli.experttune:main",
          ],
      },
      )
