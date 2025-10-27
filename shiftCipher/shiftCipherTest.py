import unittest

import random, sys, math

from shiftCipher.ShiftCipher import ShiftCipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class TestShiftCipher(unittest.TestCase):
    def test_shift_cipher(self):
        random.seed(543)

        shift = ShiftCipher()

        for i in range(50):
            randomText = SYMBOLS * random.randint(3, 15)
            randomTextList = list(randomText)
            random.shuffle(randomTextList)
            randomText = ''.join(randomTextList)

            print('Test no. {0} for text: {1}\n'.format(i+1, randomText[:40]))

            for key in range(2, len(randomText) // 2):
                encrypted = shift.encrypt(randomText, key)
                decrypted = shift.decrypt(encrypted, key)

                self.assertEqual(randomText, decrypted)


if __name__ == '__main__':
    unittest.main()
