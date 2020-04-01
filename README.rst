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

.. image:: https://ci.appveyor.com/api/projects/status/github/AndreyErmilov/pytest-mock-server?branch=master
    :target: https://ci.appveyor.com/project/AndreyErmilov/pytest-mock-server/branch/master
    :alt: See Build Status on AppVeyor

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

  @pytest.mark.server(url='/v1/items', response=json.dumps({'key': 'value'}))
  def test_handler_responses_200():
      response = requests.get('http://localhost:5000/v1/items')
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

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/AndreyErmilov/pytest-mock-server/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
