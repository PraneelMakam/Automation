import run_tests

def test_simulate_test():
    result = run_tests.simulate_test("dummy_test")
    assert "test" in result
    assert result["result"] in ["pass", "fail"]
    assert 0 <= result["duration"] <= 10
    assert 0 <= result["resource_usage"] <= 100
