from setuptools import setup, find_packages

setup(
    name='timcli',
    version='0.1.0',
    url='https://github.com/hornc/timcli',
    author='Charles Horn',
    description='PSX TIM image file format command line utility',
    packages=find_packages(),
    scripts=['timcli']
)
