import unittest
import xml.etree.ElementTree as ET

from extinct_art.brush import jitter_path
from extinct_art.compose import build_svg
from extinct_art.palettes import PALETTES
from extinct_art.species import SPECIES

import random


class BuildTests(unittest.TestCase):
    def test_every_species_and_palette_is_valid_xml(self):
        for species in SPECIES:
            for palette in PALETTES:
                with self.subTest(species=species, palette=palette):
                    root = ET.fromstring(build_svg(species, palette))
                    self.assertTrue(root.tag.endswith("svg"))

    def test_same_seed_same_image(self):
        self.assertEqual(build_svg(seed=3), build_svg(seed=3))

    def test_different_seed_changes_image(self):
        self.assertNotEqual(build_svg(seed=3), build_svg(seed=4))

    def test_options_remove_layers(self):
        svg = build_svg(caption=False, grain=False, flower=False)
        self.assertNotIn("<text", svg)
        self.assertNotIn('id="grain"', svg)
        self.assertNotIn("<ellipse", svg)

    def test_unknown_names_raise(self):
        with self.assertRaises(KeyError):
            build_svg("dodo_inexistente")
        with self.assertRaises(KeyError):
            build_svg(palette="no_existe")

    def test_jitter_keeps_relative_commands(self):
        d = "M10 10 q4 5 8 0"
        out = jitter_path(d, 1.0, random.Random(1))
        self.assertTrue(out.endswith("q 4.00 5.00 8.00 0.00"))


if __name__ == "__main__":
    unittest.main()
