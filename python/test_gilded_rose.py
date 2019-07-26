# -*- coding: utf-8 -*-
import copy
import unittest

from gilded_rose import GildedRose, Item
from legacyMasterData import legacy_output, legacy_test_set, legacy_test_duration


class GildedRoseTest(unittest.TestCase):
    def test_legacy_system(self):
        self.maxDiff = None
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

    def test_sulfuras_not_updated(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 65)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 65)
        self.assertEqual(items[0].sell_in, 0)

    def test_update_appreciating_item__should_increase_quality_by_one_if_not_expired(self):
        items = [Item("Aged Brie", 4, 0)]
        GildedRose(items).update_quality()
        print(items)
        self.assertEqual(1, items[0].quality)

    def test_update_appreciating_item__should_increase_quality_by_two_if_expired(self):
        items = [Item("Aged Brie", -1, 0)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 2)


if __name__ == '__main__':
    unittest.main()
