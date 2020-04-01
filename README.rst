==================
pytest-mock-server
==================

.. image:: https://img.shields.io/pypi/v/pytest-mock-server.svg
    :target: https://pypi.org/project/pytest-mock-server
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-mock-server.svg
    :target: https://pypi.org/project/pytest-mock-server
    :alt: Python versions

.. image:: https://travis-ci.org/AndreyErmilov/pytest-mock-server.svg?branch=master
    :target: https://travis-ci.org/AndreyErmilov/pytest-mock-server
    :alt: See Build Status on Travis CI


Mock server plugin for pytest

----

Installation
------------

You can install "pytest-mock-server" via `pip`_ from `PyPI`_::

    $ pip install pytest-mock-server


Usage
-----
.. code-block:: python

  import pytest
  import json
  import requests

  @pytest.mark.server(url='/v1/items/', response=json.dumps({'key': 'value'}))
  def test_handler_responses_200():
      response = requests.get('http://localhost:5000/v1/items/')
      assert response.status_code == 200
      

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-mock-server" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/AndreyErmilov/pytest-mock-server/issues
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
