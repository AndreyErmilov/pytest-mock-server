# pytest-mock-server
Mock server plugin for pytest

## Installation
```bash
pip install pytest-mock-server
```

## Usage
```python
import pytest
import json
import requests

@pytest.mark.server(url='/v1/items', response=json.dumps({'key': 'value'}))
def test_handler_responses_200():
    response = requests.get('http://localhost:5000/v1/items')
    assert response.status_code == 200
```

## Contributing
Contributions are very welcome. Tests can be run with `tox`, please ensure
the coverage at least stays the same before you submit a pull request.

## License
Distributed under the terms of the `MIT` license, "pytest-mock-server" is free and open source software


## Issues
If you encounter any problems, please `file an issue` along with a detailed description.
