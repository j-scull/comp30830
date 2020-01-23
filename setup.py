


from setuptools import setup

setup(name="system_info",
      version="0.1",
      description="Basic system information for COMP30830",
      url="",
      author="Joe Scullion",
      author_email="joe-scullion@hotmail.com",
      license="GPL3",
      install_requires = ['os', 'psutils']
      packages=['system_info'],
      entry_points={
        'console_scripts':['comp30830_systeminfo=system_info.main:main']
        }

      )
