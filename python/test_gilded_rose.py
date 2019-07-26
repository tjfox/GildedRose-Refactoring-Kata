# -*- coding: utf-8 -*-
import copy
import unittest

from gilded_rose import GildedRose
from legacyMasterData import legacy_output, legacy_test_set, legacy_test_duration


class GildedRoseTest(unittest.TestCase):
    def test_legacy_system(self):
        items = copy.deepcopy(legacy_test_set)
        output = ''
        for day in range(legacy_test_duration):
            output += "\n-------- day %s --------\n" % day
            output += "name, sellIn, quality\n"

            for item in items:
                output += str(item)
                output += "\n"
            GildedRose(items).update_quality()

        self.assertEqual(legacy_output, output)


if __name__ == '__main__':
    unittest.main()
