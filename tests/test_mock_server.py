

def test_server_works(testdir):
    testdir.makepyfile("""
        import pytest
        import json
        import urllib.request
        @pytest.mark.server(url='/test/', response='')
        def test_handler_responses_200():
            response = urllib.request.urlopen('http://localhost:5000/test/')
            assert response.status == 200
    """)
    result = testdir.runpytest('-v')
    assert result.ret == 0
