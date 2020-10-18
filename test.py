from unittest import TestCase

from plurk_dice import Dice


class Test(TestCase):
    def test_roll(self):
        dice = Dice(20).roll()
        self.assertTrue(20 >= dice["result"] >= 1)

    def test_base64(self):
        dice = Dice("bzz").roll(base64=True)
        self.assertIn("base64", dice)
