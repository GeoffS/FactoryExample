
# A stupid-simple client that just instantiates a Foo and returns
# a formatted version of the foo.param() call.
def foo_client(foo_factory):
    foo = foo_factory("foo_client Parameter Value")
    return f'foo.param() = {foo.param()}'