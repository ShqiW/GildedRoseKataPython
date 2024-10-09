class ItemStrategy:
    def update_item(self, item):
        pass

class RegularItemStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1
        item.quality -= 1 if item.quality > 0 else 0

        if item.sell_in < 0:
            item.quality -= 1 if item.quality > 0 else 0

class AgedBrieStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1

        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

class BackstagePassStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

class SulfurasStrategy(ItemStrategy):
    def update_item(self, item):
        pass  

class ConjuredItemStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1
        item.quality -= 2 if item.quality > 0 else 0

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        item.quality = max(0, item.quality)

class Item:
    """DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    # def __eq__(self, other):
    #     if not isinstance(other, Item):
    #         return False
    #     return self.name == other.name and self.sell_in == other.sell_in and self.quality == other.quality

class GildedRose:
    def __init__(self, items):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items


        self.strategy_map = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Conjured": ConjuredItemStrategy()
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategy_map.get(item.name, RegularItemStrategy())
            strategy.update_item(item)