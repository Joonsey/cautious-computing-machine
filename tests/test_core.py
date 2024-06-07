from tests.testutils import client

class TestCore:
    """
    Test core should test all 'standard' test cases that does not confide within their own reasonable category
        i.e each route should have their own respective test suite and reasonably be reasonably self-confained.

    Any case that is considered expected uniform behaviour could and should be asserted by this test suite.
    """

    @staticmethod
    def test_is_healthy():
        response = client.get("healthy")

        assert response.status_code == 200

