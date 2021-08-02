from setuptools import setup
setup(
    name='note',
    version='0.1.0',
    packages=['note'],
    install_requires=[
        "pyperclip"
    ],
    entry_points={
        'console_scripts': [
            'note = note.__main__:main'
        ]
    })
