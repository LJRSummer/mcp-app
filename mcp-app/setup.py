from setuptools import setup, find_packages

setup(
    name='app',
    version='0.0.1',
    description='A Flask application for image upload and similarity scoring.',
    author='Laurelliang',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Pillow',
        'imagehash',
        'Werkzeug'
    ],
    entry_points={
        'console_scripts': [
            'app-server=app.main:main'
        ]
    },
    include_package_data=True,
)
