import os
from setuptools import setup, find_packages

VERSION = (0, 1)

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='python-sigep',
    version='.'.join(map(str, VERSION)),
    description='python-sigep is a lib for making queries over the brazilian shipping webservice Sigepweb from ECT - Correios',
    long_description=readme,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='correios sigep sigepweb e-commerce',
    author='Bruno Ribeiro',
    author_email='brunoribeiroinf@gmail.com',
    url='http://github.com/ribeiroti/python-sigep',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['urllib3'],
)
