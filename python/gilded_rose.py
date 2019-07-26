# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                self.update_appreciating_item(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.sell_in = item.sell_in - 1
                self.update_time_sensitive_item(item)

            else:
                self.update_item_quality(item)
                self.update_item_sell_in(item)

    def increment_item_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def update_item_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def update_time_sensitive_item(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self.increment_item_quality(item, 3)
        elif item.sell_in < 10:
            self.increment_item_quality(item, 2)
        else:
            self.increment_item_quality(item, 1)

    def update_item_sell_in(self, item):
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.update_expired_item(item)

    def update_expired_item(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = item.quality - item.quality
        elif item.name == "Aged Brie":
            item.quality = min(50, item.quality + 1)
        else:
            item.quality = max(0, item.quality - 1)

    def update_appreciating_item(self, item):
        if item.sell_in < 0:
            self.increment_item_quality(item, 2)
        else:
            self.increment_item_quality(item, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
