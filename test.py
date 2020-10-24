from unittest import TestCase

from plurk_dice import Dice


class Test(TestCase):
    def test_roll(self):
        dice = Dice(20).roll()
        self.assertTrue(20 >= dice["result"] >= 1)

    def test_base64(self):
        dice = Dice("bzz").roll(base64=True)
        self.assertIn("base64", dice)

    def test_parse(self):
        dices = Dice.parse("(dice20)  (dice8)")
        self.assertTrue(20 >= dices[0]["result"] >= 1)
        self.assertTrue(8 >= dices[1]["result"] >= 1)
