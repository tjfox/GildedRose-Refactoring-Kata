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

    def test_update__should_not_increase_quality_over_50(self):
        items = [Item("Aged Brie", 4, 50), Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        GildedRose(items).update_quality()

        self.assertEqual(50, items[0].quality)
        self.assertEqual(50, items[1].quality)

    def test_update_should_not_decrease_quality_below_0(self):
        items = [Item("Generic", 0, 0)]
        GildedRose(items).update_quality()
        print(items)
        self.assertEqual(0, items[0].quality)

    def test_generic_item__should_decreate_quality_by_1_if_not_expired(self):
        items = [Item("Generic", 4, 1)]
        GildedRose(items).update_quality()
        print(items)
        self.assertEqual(0, items[0].quality)

    def test_generic_item__should_decrease_quality_by_2_if_expired(self):
        items = [Item("Generic", 0, 2)]
        GildedRose(items).update_quality()
        print(items)
        self.assertEqual(0, items[0].quality)

    def test_appreciating_item__should_increase_quality_by_one_if_not_expired(self):
        items = [Item("Aged Brie", 4, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(1, items[0].quality)

    def test_appreciating_item__should_increase_quality_by_two_if_expired(self):
        items = [Item("Aged Brie", -1, 0)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 2)

    def test_time_sensitive_item__should_increase_quality_by_1_if_sell_in_greater_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 1)

    def test_time_sensitive_item__should_increase_quality_by_2_if_sell_in_less_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 2)

    def test_time_sensitive_item__should_increase_quality_by_3_if_sell_in_less_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 3)

    def test_time_sensitive_item__should_set_quality_to_0_if_sell_in_passed(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 4)]
        GildedRose(items).update_quality()

        self.assertEqual(items[0].quality, 0)

if __name__ == '__main__':
    unittest.main()
