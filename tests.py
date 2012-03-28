import datetime
import decimal

try:
    import unittest2 as unittest
except ImportError:
    import unittest
    if not hasattr(unittest, 'expectedFailure'):
        import functools

        def _expectedFailure(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    func(*args, **kwargs)
                except AssertionError:
                    pass
                else:
                    raise AssertionError("UnexpectedSuccess")
            return wrapper
        unittest.expectedFailure = _expectedFailure


class JS_OBJ_ATTR(object):

    @property
    def __json__(self):
        return {'a': 'b',
                'c': [1, 2, 3]}


class JS_OBJ(object):

    def __json__(self):
        return {'a': 'b',
                'c': [1, 2, 3]}

ndt = datetime.datetime.now()
nd = ndt.date()
t = ndt.time()
dec = decimal.Decimal('1.231230018234413213141241421')
dec2 = decimal.Decimal('2.2')
test_cases = [
  # test, orgvalue, json value
  ('testint', 1, '1'),
  ('testlist', [1, 2, 3], '[1, 2, 3]'),
  ('mixedlist', ['a', {'a':'b'}, 3], '["a", {"a": "b"}, 3]'),
  ('datetime', ndt, '"%s"' % ndt.isoformat()[:-3]),
  ('datetime.date', nd, '"%s"' % nd.isoformat()),
  ('datetime.time', t, '"%s"' % t.isoformat()[:-3]),
  ('set', set([1, 3, 2]), '[1, 2, 3]'),
  ('decimal', dec, '"%s"' % dec),
  ('decimal', dec2, '"%s"' % dec2),
  ('float', 1.234, '%s' % 1.234),
  ('__json__', JS_OBJ(), '{"a": "b", "c": [1, 2, 3]}'),
  ('__json__attr', JS_OBJ_ATTR(), '{"a": "b", "c": [1, 2, 3]}'),
]


def _make_dump_test(name, orgval, jsonval):
    def test_serialize(self):
        retjsonval = self.json.dumps(orgval)
        self.assertEqual(jsonval, retjsonval)
    return test_serialize


#def _make_load_test():
#    def test_serialize(self):
#        retjsonval = self.json.dumps(orgval)
#        loadedjsonval = self.json.loads(retjsonval)
#        self.assertEqual(orgval, loadedjsonval)
#    return test_serialize    


class TestJSONEncoder(unittest.TestCase):

    def setUp(self):
        from ext_json import stdjson
        self.json = stdjson


class TestSIMPLEJSONEncoder(unittest.TestCase):

    def setUp(self):
        from ext_json import simplejson
        self.json = simplejson

for name, orgval, jsonval in test_cases:
    setattr(TestJSONEncoder, "test_JSON_%s" % name,
            _make_dump_test(name, orgval, jsonval))
    setattr(TestSIMPLEJSONEncoder, "test_SIMPLEJSON_%s" % name,
            _make_dump_test(name, orgval, jsonval))

if __name__ == '__main__':
    unittest.main()
