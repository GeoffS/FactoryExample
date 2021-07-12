from foo_client import foo_client


# Factory method for test_foo_client1()
def foo_factory1(foo_param):
    assert foo_param == 'foo_client Parameter Value'

    class SimpleStandInFoo:
        def param(self): return "Testing for App1"

    return SimpleStandInFoo()


# Pretty simple test that just checks some values.
def test_foo_client1():
    res = foo_client(foo_factory1)
    assert res == "foo.param() = Testing for App1"


# This is  bit more comprehensive test that validates
# the values within the system, but also that the
# factory and Foo.param() methods were call once each.
def test_foo_client2():
    # A "real" mock (i.e. has a verify() method)
    class Test2MockFoo:
        def __init__(self):
            self.param_called_count = 0

        def param(self):
            self.param_called_count += 1
            return "Testing for the 2nd time..."

        def verify(self):
            assert self.param_called_count == 1

    # We need to instantate our mock here so we can call its verify() later:
    test2_foo = Test2MockFoo()

    # A variable to close over in the factory so we can check calls:
    my_test_foo_factory_call_count = 0

    # Here's our factory that closes over my_test_foo_factory_call_count and test2_foo
    def my_test_foo_factory(param):
        nonlocal my_test_foo_factory_call_count
        nonlocal test2_foo

        # Check the param value we're passed:
        assert param == 'foo_client Parameter Value'

        # Count how many times we're called:
        my_test_foo_factory_call_count += 1

        # Return the instance defined above:
        return test2_foo

    # Finally we test foo_client:
    res = foo_client(my_test_foo_factory)

    # Check the return value:
    assert res == "foo.param() = Testing for the 2nd time..."

    # Check the factory and mock-foo:
    assert my_test_foo_factory_call_count == 1
    test2_foo.verify()
