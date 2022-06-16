from setuptools import setup, find_packages

PACKAGE_NAME = "dropbox-content-hasher"

packages=find_packages()
print(packages)

setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    packages=packages,
    entry_points={
        'console_scripts': [
            'drophash=hash_file:main',
        ]
    },
)
