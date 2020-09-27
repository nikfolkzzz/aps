from setuptools import setup
setup(
    name='aps',
    version='0.1.0',
    packages=['aps'],
    entry_points={
        'console_scripts': [
            'aps = aps.__main__:main'
        ]
    })
