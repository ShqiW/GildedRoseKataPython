# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)])

    def test_aged_brie_should_increase_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(brie, 1, 1), Item(brie, -1, 12)])

    def test_backstage_passes_increase_quality(self):
        passes = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(passes, 15, 20), Item(passes, 10, 30), Item(passes, 5, 40)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(passes, 14, 21), Item(passes, 9, 32), Item(passes, 4, 43)])

    def test_sulfuras_should_never_decrease_in_quality(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)  ])



if __name__ == '__main__':
    unittest.main()
