# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            self._update_item(item)

    def _update_item(self, item):
        item.sell_in = item.sell_in - 1
        if item.name == "Aged Brie":
            self._update_appreciating_item(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._update_time_sensitive_item(item)
        else:
            self.update_item_quality(item)

    def _increment_item_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def _decrement_item_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def update_item_quality(self, item):
        if item.sell_in < 0:
            self._decrement_item_quality(item, 2)
        else:
            self._decrement_item_quality(item, 1)

    def _update_appreciating_item(self, item):
        if item.sell_in < 0:
            self._increment_item_quality(item, 2)
        else:
            self._increment_item_quality(item, 1)

    def _update_time_sensitive_item(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self._increment_item_quality(item, 3)
        elif item.sell_in < 10:
            self._increment_item_quality(item, 2)
        else:
            self._increment_item_quality(item, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
