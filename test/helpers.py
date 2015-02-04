import nose.tools as nt

def assert_type(object, klass):
    nt.assert_equals(type(object), klass)
