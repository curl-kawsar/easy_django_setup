# setup.py
from setuptools import setup, find_packages

setup(
    name='easy_django_setup',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        easy-django-setup=cli:cli
    ''',
    author='Kawsar',
    author_email='knownaskawsar@example.com',
    description='Easy Django Setup Tool',
    long_description=open('README.txt').read(),
    long_description_content_type='text/plain',
    url='https://github.com/curl-kawsar/easy_django_setup',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
