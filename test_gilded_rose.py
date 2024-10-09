# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2)]
        gr = GildedRose(items)
        gr.update_quality()

        assert gr.items[0].name == "+5 Dexterity Vest"
        assert gr.items[0].sell_in == 0
        assert gr.items[0].quality == 1

    
 
        
    def test_aged_brie_should_increase_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0)]
        gr = GildedRose(items)
        gr.update_quality()
  
        assert gr.items[0].name == "Aged Brie"
        assert gr.items[0].sell_in == 1
        assert gr.items[0].quality == 1

    def test_backstage_passes_increase_quality(self):
        passes = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(passes, 15, 20)]
        gr = GildedRose(items)
        gr.update_quality()
   
        assert gr.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
        assert gr.items[0].sell_in == 14
        assert gr.items[0].quality == 21

    def test_sulfuras_should_never_decrease_in_quality(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()

        assert gr.items[0].name == "Sulfuras, Hand of Ragnaros"
        assert gr.items[0].sell_in == 0
        assert gr.items[0].quality == 80



if __name__ == '__main__':
    unittest.main()
