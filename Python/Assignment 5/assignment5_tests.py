"""Tests for CS109 Python Assignment 5.

This does not test for all the requirements of the assignment! So make
sure you test it yourself.

Run this script using:
  python3.5 assignment5_tests.py
It should work if you are in the same directory as your assignment5.py
file. If this does not work you may want to try:
  PYTHONPATH=[directory containing assignment2.py] python3.5 assignment5_tests.py

"""

# DO NOT CHANGE THIS FILE. Grading will be done with an official
# version, so make sure your code works with this exact version.

import unittest
import itertools
import functools
from contextlib import contextmanager
import sys


import assignment5

shuffled_list = [39, 83, 31, 8, 66, 19, 45, 61, 86, 65, 28, 89, 95,
                 82, 40, 50, 88, 25, 47, 24, 51, 87, 93, 2, 67, 73, 7,
                 79, 98, 9, 34, 5, 72, 91, 64, 48, 30, 20, 37, 22, 43,
                 54, 46, 17, 55, 74, 49, 76, 35, 97, 14, 26, 10, 52,
                 78, 75, 13, 6, 4, 36, 77, 84, 59, 68, 11, 60, 71, 63,
                 100,90, 57, 41, 70, 96, 15, 92, 21, 56, 38, 27, 53,
                 23, 18, 12, 16, 33, 85, 44, 69, 42, 1, 99, 32, 29,
                 81, 3, 80, 58, 94, 62]

    
strings_list = ['\u00ACUlV=ic',
     'q\u00B4wBox\u00B4{\u00A5!^Yu',
     '\u00AAC\u00B0\u00A7\u00AA/\u00ACW',
     'q}QYX',
     ')B',
     '\u0776\U000244AA\u2E92\u9DB4',
     '\U00029F94\uAE3D\u7DE0\U0002050D\U0002B033\u6776\U0002976A\U0002B0F2\U0002077C\uB5B4\u5483\u16C2',
     '\uB247',
     '\u00B6\u00B0GGm',
     '\uCB9B\U000263D6\u9C57\U000200B1\U00028902\U0002A5BA',
     'Un',
     '\U00027E1C',
     '\uAF54\u420B\u7781\u5681\u4C44\u5A33\U000299BC\u541D\u7D58\u7395\u5878\U00011024\U00027424',
     '\U00027594\u4F8F\u2F4A\u1FAC\U000296E7\u58DD\U00024E40\u70F6\u25E0\U00011090\u9B7E\u14EA\U00024559\U0002AD71',
     '\U0002541A',
     '\U00022E50\U000241D4\U0001D6B2\U000168C5\u8BC5\U000130E6\U0002647B\uD507\u8E35\u3069\u9329\U0002A2BA\u3CB0',
     '\U000255FB',
     'bd:hrTWo\u00B7By\u00AEc',
     '\u537C\U000256BF\U0002364A\U00029C04\U00023949\u6CF0\U00021239\u6810\u2366\u9608\U0001F342',
     '\U000234B3\U00028030\u85B7\u4439\u5A3B\U000234D8',
     'V)Hz%Q\u00B0\u00A5}jp',
     'u}n;\u00A7G',
     '\uB8B2\U0002159F\uA230\U000299CE\U0001D06A\U00025BA3',
     'W+\u00BB?\u00AC',
     ';TGeG\u00AB>hE',
     '[\u00BA\u00A9S',
     '[%L\u00AB',
     '\U00028FE3\uA753\u1E4A\uC453\u9E5B\u6088\u7274\U00025A05\u631F\U0002807C',
     '\u91BE\u3D50\U00021075\u868A\u10C2\U000285DF\U00020FC8\U00028C23\u51FA\U0002939C\U0001F611\U00026D06\u6722',
     '\u52C2\u6A6D\u5981\U00024761\u02FB\uBABB',
     '\u00A3U:[F\u00A9i\u00BBnB_',
     '\u2108\U000243D6\U00020601\uD6FE\U0001D62B\U0002837F\uD1E8\U00029620\u4EBB\uB620\u79C8',
     'X{-J\u00B6Ni\u00A5\u00B1AeSQ\u00B0',
     '\U000276AA\U000201B8\U00020332\u52F2',
     'GWPj\u00BB\u00AB}',
     '\U0002917E',
     'gzAbF|jF)[\u00A6',
     '\u5629\u583D\U00026BA0\U0001D5F8\u251C\u8888\U00027283\U00024246',
     '\u56A5\uC1DA\uFCA3\U000228AD\u3050',
     'M',
     '\u00A5',
     'Y@\u00A2$\u00B0JaTsr\u00B0\u00B1->',
     '\u8293\U000248C6\uA6B0\uBD25\U00021ABC\U0002770A\U00027504\uB722\u6163\U00024A1B\U00021B77',
     'b',
     'pweo',
     '\U00022F66\u79F7\U00028E81\U00022C8D\u8B03\u4D27\u559F\uCAB3',
     '\U000277CD\U0002862E\U00025A2E\U00022C4D\u6AC1\U00029C80',
     '\u7156\u593F\u6741\u0993\U0002900E\U00029B22\uCD26\U000232C1\U0001205A\u31D3',
     'slk',
     '\u00AEAv\u00A7p\u00A5\u00A6P*?J~\u00A1',
     '\u10A5\U0002A0DD\U0002AA17\u0A98\uCA38\U00023B12\u733A',
     '\u9086\U0002A5B7\uA76A\U00021F07\U00024CA0\u5C99\U00027AA6\u221C\uFE58\U0002B14B\U00025D1C\u6F9D',
     '\U0002491B\U00028A5D\u6B15\u907C\U000295A6\U00024454\U00020C07\u5CBF\U00024421\u4E39',
     'N?HW.qzL\u00B8cQ',
     'RXIoMU|q\u00B6\u00ABJ',
     '_eXDiMs&\u00B4%\u00B5\u00A6',
     '\U0002A33C\u7923\u8595\u56B2',
     '(~\u00BA}jH\u00A4\u00A4',
     '\uFEC4\u8C95\U00013199\U0001F161',
     '\U00026DCA\u33A1\uB98F\U00024D25\U00023D74\uADDB\u37CE',
     '\u15BA\uACD8\U00023845\u97DC\uB0BC',
     '\u2993\uFD5C\u35AE\u22AB\uABCE\u6AEC\U0002AA41\u8BDE\U00025740\u6342\u40A6\u69FB',
     '\u375A\U000206E0\U000215A0\U000224AB\U0002A466\U0002A233\U000244F1\u4AA2\uA643\u3891\uBC26',
     't',
     '\u00AE.a.\u00B0x~x`}k@w\u00A3',
     '\U0002B721\U00024597\uBC6F\U00025CB3\U0002330B\U0002549C\U00025DC3\uC578\u72F4\u02D0\u4BC2\u9801\U000122B1',
     'B',
     'l\u00A8\u00A6',
     '\u00AE',
     '^@\u00AFnyB\u00BB',
     '\U00029699',
     '\U00029436\u954B\u3BFC\U00026997\U00025B10\U00028ECB\u293D\u16C2\U00023D1F\uD660',
     '\uC3B9\u7B19\U00023411\u6633\U0002AC95',
     'MRu-=mU#JZ',
     'iR-}\u00A5uU/N\u00B4\u00AC(b}',
     '\U00010850\uD792\U0002A860\u73CA\u7BE9\u6360\u615C\U00022FCB\U0002AB45\u868A\U00023E61',
     '\uC999\U00029ED3\u69CE\u3C05\U00024B04',
     '/\u00A4qG&#\u00A1o]',
     '$}\u00B0yC\u00A8/',
     '\u00A7OP',
     '\u34E3\U00028E26\U0001F0C3\u7652\U00025B54\uCA58',
     '\u289B\uCF34\U00025562\U000132D2\U00022459\u59FA\U000204C2',
     '>',
     '\u812A\U0002A71D\uBAE8\u1F63\U0002A378\u661D\U00020FC7\U0002B178\U0002062D',
     '\u00A4iDtU\u00A4(t\u00A2Fn',
     '\U00028BA4\U0001D784\U00029B4D\uC031\U000287BB\u716B\uBB36',
     '\u00A1ScM};(\u00AF',
     '+IGn.JRB',
     '#g',
     'woqt*%lxY@']

@functools.total_ordering
class OrderedThing(object):
    allow_hashing = False

    def __init__(self, data):
        self.data = data

    @property
    def _sum(self):
        return sum(ord(c) for c in self.data)

    def __eq__(self, other):
        if not isinstance(other, OrderedThing):
            return NotImplemented
        return self._sum == other._sum

    def __lt__(self, other):
        if not isinstance(other, OrderedThing):
            return NotImplemented
        return self._sum < other._sum

    def __hash__(self):
        if self.allow_hashing:
            return hash(self._sum)
        else:
            raise TypeError("OrderedThing is not hashable")

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self._sum)
    def __str__(self):
        return "{}([{}])".format(self.__class__.__name__, self._sum)

@contextmanager
def hashable_OrderedThing():
    OrderedThing.allow_hashing = True 
    try:
        yield None
    finally:
        OrderedThing.allow_hashing = False 

def get_attrs(obj, attrs):
    return tuple(getattr(obj, a) for a in attrs if hasattr(obj, a))


class Assignment5Tests(unittest.TestCase):
    def setUp(self):
        super().setUp()
        sys.stdout.flush()
        sys.stderr.flush()

    def float_key_td(self):
        return self.make_treedict((float(i/19), chr(i)) for i in shuffled_list)
    def large_str_key_td(self):
        return self.make_treedict((s, s and ord(s[0])) for s in strings_list)
    def custom_key_td(self):
        with hashable_OrderedThing():
            d = dict((OrderedThing(s), s and ord(s[0])) for s in strings_list)
        return self.make_treedict(d.items())

    def make_treedict(self, iterable):
        # Test two different ways of making the TreeDict each time.
        iterable = list(iterable)
        assignment5.TreeDict(iter(iterable))
        return assignment5.TreeDict(iterable)

    def treedict_get(self, td, key):
        return td.get(key)

    def int_key_td(self):
        return self.make_treedict((i, str(i)) for i in shuffled_list)
    def str_key_td(self):
        return self.make_treedict(({"zero": 0, "one": 1, "two": 2}).items())

    def call_methods(self, td, key, value=None):
        try:
            td[key]
        except Exception:
            self.fail("The key '{}' should exist in TreeDict".format(key))
        if value is not None:
            self.assertEqual(td[key], value)
        td[key] = 1
        td[key]
        td.get(key)
    
    def test_construct_empty(self):
        td = assignment5.TreeDict()
        td["1"] = 1
        td["1"]
        td.get("1")        
        
    def test_construct_unordered_pairs(self):
        self.call_methods(assignment5.TreeDict((i, str(i)) for i in shuffled_list), 1, "1")
        
    def test_construct_ordered_pairs(self):
        self.call_methods(assignment5.TreeDict((i, str(i)) for i in range(1, 101)), 2, "2")
        
    def test_construct_dict(self):
        self.call_methods(assignment5.TreeDict({1: "1", 2: "2"}), 2, "2")
        self.call_methods(assignment5.TreeDict({"1": "1", "2": "2"}), "1", "1")

    def test_construct_td(self):
        self.call_methods(assignment5.TreeDict(self.int_key_td()), 2, "2")
        self.call_methods(assignment5.TreeDict(self.str_key_td()), "one", 1)

    def test_construct_order_unimportant(self):
        td1 = assignment5.TreeDict((i, str(i)) for i in shuffled_list)
        td2 = assignment5.TreeDict((i, str(i)) for i in range(1, 101))
        self.assertEqual(self.treedict_get(td1, 2), "2")
        self.assertEqual(self.treedict_get(td2, 2), "2")
        self.assertTrue(all(self.treedict_get(td1, i) == self.treedict_get(td2, i)
                            for i in range(110)))

    def test_index1(self):
        self.assertEqual(self.int_key_td()[50], "50")
    def test_index2(self):
        self.assertEqual(self.str_key_td()["zero"], 0)

    def test_set_add(self):
        td = self.int_key_td()
        td[1000] = 5
        self.assertEqual(self.treedict_get(td, 1000), 5)
    def test_set_overwrite(self):
        td = self.int_key_td()
        td[30] = 3
        self.assertEqual(self.treedict_get(td, 30), 3)

    def test_in1(self):
        self.assertIn(10, self.int_key_td())
        
    def test_in2(self):
        self.assertIn("two", self.str_key_td())
        self.assertTrue(hasattr(self.str_key_td(), "__contains__"))

    def test_get_exists(self):
        self.assertEqual(self.int_key_td().get(50), "50")
    def test_get_nonexists(self):
        self.assertEqual(self.int_key_td().get(500), None)
    def test_get_default(self):
        td = self.int_key_td()
        self.assertEqual(td.get(500, 400), 400)
        self.assertEqual(td.get(500), None)
    def test_get_str_key(self):
        self.assertEqual(self.str_key_td().get("one"), 1)
        self.assertEqual(self.str_key_td().get("zero"), 0)

    def test_update1(self):
        td = self.int_key_td()
        td.update([(10, "ten"), (11, "eleven")])
        self.assertEqual(self.treedict_get(td, 10), "ten")
        self.assertEqual(self.treedict_get(td, 11), "eleven")
        self.assertEqual(self.treedict_get(td, 12), "12")

    def test_len1(self):
        self.assertEqual(len(self.int_key_td()), 100)
        td = self.int_key_td()
        td.update({6: 7, 10000: 100})
        self.assertEqual(len(td), 101)
        self.assertEqual(len(td), 101)
        
    def test_len2(self):
        self.assertEqual(len(self.str_key_td()), 3)
        td = self.str_key_td()
        td["one"] = 3
        self.assertEqual(len(td), 3)
        self.assertEqual(len(td), 3)
        
    def test_len3(self):
        td = assignment5.TreeDict()
        self.assertEqual(len(td), 0)
        td["2"] = 2
        self.assertEqual(len(td), 1)
        self.assertEqual(len(td), 1)

    def test_iterate(self):
        self.assertEqual(list(self.int_key_td()), list(range(1, 101)))
        self.assertEqual(list(self.make_treedict([])), list())
        self.assertTrue(all(x == y
                            for x, y in itertools.zip_longest(self.int_key_td(), range(1, 101))))

    def test_parallel_iterate(self):
        td = self.int_key_td()
        
        for x, y in zip(td, td):
            self.assertEqual(x, y)

        td = self.str_key_td()
        
        i1 = iter(td.items())
        i2 = iter(td.items())
        prev = next(i1)
        for x, y in zip(i1, i2):
            self.assertEqual(prev, y)
            prev = x
            

    def test_items(self):
        self.assertEqual(list(self.int_key_td().items()), [(y, str(y)) for y in range(1, 101)])
        self.assertEqual(list(self.make_treedict([]).items()), list())
        self.assertTrue(all(x == (y, str(y)) 
                            for x, y in itertools.zip_longest(self.int_key_td().items(), range(1, 101))))

    def test_iterate2(self):
        self.assertEqual(list(self.str_key_td()), ["one", "two", "zero"])
        self.assertEqual(list(self.str_key_td().items()), [("one", 1), ("two", 2), ("zero", 0)])

    def test_raises_KeyError(self):
        td = self.str_key_td()
        with self.assertRaisesRegex(KeyError, ".*aaaa.*"):
            td["aaaa"]

    def test_raises_on_None(self):
        td = self.str_key_td()
        with self.assertRaises((ValueError, TypeError, KeyError)):
            td[None] = 1

    def test_raises_on_None_in_update_init(self):
        td = self.str_key_td()
        with self.assertRaises((ValueError, TypeError, KeyError)):
            td.update([("sss", 3), (None, 4)])
        with self.assertRaises((ValueError, TypeError, KeyError)):
            assignment5.TreeDict([("sss", 3), (None, 4)])

    def test_update_dict(self):
        td = self.float_key_td()
        td.update({10.0: "ten", 11.2: "eleven"})
        self.assertEqual(self.treedict_get(td, 10.0), "ten")
        self.assertEqual(self.treedict_get(td, 11.2), "eleven")

    def test_update_td(self):
        td = self.int_key_td()
        td.update(self.make_treedict({10: "ten", 0: "eleven"}.items()))
        self.assertEqual(self.treedict_get(td, 9), "9")
        self.assertEqual(self.treedict_get(td, 10), "ten")
        self.assertEqual(self.treedict_get(td, 0), "eleven")

    def test_update_bad_argument(self):
        td = self.int_key_td()
        with self.assertRaises(Exception, msg="Update should not accept random values and ignore them. Values that will not work should cause some error."):
            td.update(5)
        with self.assertRaises(Exception, msg="Update should not accept random values and ignore them. You shouldn't just pass a default None value to update. Use () or similar instead."):
            td.update(None)

    def test_str_keys_iterate(self):
        td = self.large_str_key_td()
        pairs = [(s, s and ord(s[0])) for s in strings_list]
        self.assertEqual(list(td.items()), sorted(pairs))
        
    def test_str_keys_get(self):
        td = self.large_str_key_td()
        pairs = [(s, s and ord(s[0])) for s in strings_list]
        self.assertTrue(all(self.treedict_get(td, k) == v 
                            for k, v in pairs))
        
    def test_custom_keys_iterate(self):
        td = self.custom_key_td()
        with hashable_OrderedThing():
            d = dict((OrderedThing(s), s and ord(s[0])) for s in strings_list)
        self.assertEqual(list(td.items()), sorted(d.items()))

    def test_custom_keys_get(self):
        td = self.custom_key_td()
        with hashable_OrderedThing():
            d = dict((OrderedThing(s), s and ord(s[0])) for s in strings_list)
        self.assertTrue(all(self.treedict_get(td, k) == v 
                            for k, v in d.items()))
        
    def test_in3(self):
        self.assertIn('\uC999\U00029ED3\u69CE\u3C05\U00024B04', self.large_str_key_td())

    def test_in4(self):
        self.assertIn(78/19, self.float_key_td())

    def test_0_key(self):
        td = self.int_key_td()
        td[0] = 102
        self.assertEqual(self.treedict_get(td, 0), 102)

    def test_0_value(self):
        td = self.int_key_td()
        td[102] = 0
        self.assertEqual(self.treedict_get(td, 102), 0)
        self.assertIn(102, td)

        td = self.int_key_td()
        td[102] = None
        self.assertEqual(self.treedict_get(td, 102), None)
        self.assertIn(102, td)

    def test_none_value(self):
        td = self.int_key_td()
        td[0] = None
        self.assertEqual(self.treedict_get(td, 0), None)
        self.assertEqual(td[0], None)

if __name__ == "__main__":
    unittest.main()
