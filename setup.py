from setuptools import setup, find_packages

setup(
    name='email_verification_client',
    version='0.3.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)