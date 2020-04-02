

def test_server_works(testdir):
    testdir.makepyfile("""
        import pytest
        import json
        import urllib.request
        TEST_DATA = {'key': 'value'}
        @pytest.mark.server(url='/test/', response=TEST_DATA)
        def test_handler_responses_200():
            response = urllib.request.urlopen('http://localhost:5000/test/')
            assert response.status == 200
            assert json.loads(response.read()) == TEST_DATA
    """)
    result = testdir.runpytest('-v')
    assert result.ret == 0


# def test_status_code_works(testdir):
#     testdir.makepyfile("""
#         import pytest
#         import json
#         import urllib.request
#
#         @pytest.mark.server(url='/test/', response='', status_code=201)
#         def test_handler_status_codes():
#             response = urllib.request.urlopen('http://localhost:5000/test/')
#             assert response.status == 201
#     """)
#     result = testdir.runpytest('-v')
#     assert result.ret == 0
