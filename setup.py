from setuptools import setup, find_packages

setup(
    name='eos_app',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'eos-app = eos_app.cli:save_list'
        ]
    },
    install_requires=[
        'click>=8.1.3'
    ],
    author='A.Chupakhina',
    author_email='liskin.sun@gmail.com',
    description='A command line interface for saving two-dimensional lists to JSON or CSV files',
)
