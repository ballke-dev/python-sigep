============
python-sigep
============

python-sigep is a lib for making queries over the brazilian shipping webservice Sigepweb from ECT - Correios

Installation
^^^^^^^^^^^^^
Use "PIP" or "easy_install": ::

    pip install -e git+git://github.com/ribeiroti/python-sigep.git#egg=python-sigep

Usage
^^^^^

For send a simple query: ::

    from sigep import consultaCEP

    params = {'cep': '89802100'}
    query = consultaCEP(**params)
    data = query.do() # dict with the returned data

To see more operations see the file: "tests.py"

Tests
^^^^^
For tests: ::

    python tests.py


Documentation
^^^^^^^^^^^^^
There is no documentation yet.
