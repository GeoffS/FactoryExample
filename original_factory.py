 
# Here are some factories that might appear in a test:
def test1_foo_factory(foo_param):
    class MockFoo:
        def param(self): return "Testing"
    return MockFoo()


#-------- Production Code for Foo  -----------
class Foo:
    def __init__(self, param):
        self._param = param

    def param(self): return self._param


def production_foo_factory(foo_param):
    return Foo(foo_param)

#-------  Foo consumer:  ---------
def main(foo_factory):
    foo = foo_factory("main")
    print(f'foo.param = {foo.param()}')


#-----  Runner that simulates both a "production" call to main()  -----
#-----  and two unit-tests.                                       -----
if __name__ == "__main__":
    # This is what would appear in production:
    print('Production main():')
    main(production_foo_factory)

    # This is one of number of ways we could supply main() a Foo
    # in a appear in a test:
    print('\nTest #1 main():')
    main(test1_foo_factory)

    # This is another way we could supply main() a Foo
    # in a appear in a test:
    print('\nTest #2 main():')
    class T2Foo:
        def __init__(self):
            self.param_called_count = 0
            
        def param(self): 
            self.param_called_count += 1
            return "Testing for the 2nd time..."

        def verify(self):
            if self.param_called_count != 1: raise Exception()

    test2_foo = T2Foo()

    def my_test_foo_factory(param):
        if param != "main": raise Exception()
        return test2_foo

    main(my_test_foo_factory)

    test2_foo.verify()


