import unittest
from unittest import TestCase
from main import geo_logs_list, ids_new_list, max_element


class TestCity(TestCase):

    def test_type_not_list(self):
        result = type(geo_logs_list)
        self.assertNotEqual(result, list)

    @unittest.expectedFailure
    def test_list_not_empty(self):
        result = geo_logs_list
        self.assertEqual(len(result), 0)


class TestUniqueValues(TestCase):
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    def test_unique(self):
        result = ids_new_list(self.ids)
        expected = [98, 35, 15, 213, 54, 119]
        self.assertEqual(result, expected)

    def test_len_list(self):
        result = len(ids_new_list(self.ids))
        expected = 6
        self.assertEqual(result, expected)


class TestMaxElement(TestCase):
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    def test_max_element(self):
        result = max_element(self.stats)
        expected = 'yandex'
        self.assertEqual(result, expected)

    def test_not_None(self):
        result = max_element(self.stats)
        self.assertIsNotNone(result)

    def test_max_not_element(self):
        result = max_element(self.stats)
        expected = 'google'
        self.assertNotEqual(result, expected)