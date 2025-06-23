import unittest
from morse import Decoder, Encoder

class MyTestCase(unittest.TestCase):

    def testDecoder(self):
        self.decoder = Decoder()
        self.assertEqual(self.decoder.action('.... . .-.. .-.. ---'), 'HELLO')
        self.assertEqual(self.decoder.action('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'), 'HELLO WORLD')
        self.assertEqual(self.decoder.action('.... . .-.. .-.. --- / .-- --- .-. .-.. -.. / ..'), 'HELLO WORLD I')

    def testEncoder(self):
        self.encoder = Encoder()
        self.assertEqual(self.encoder.action('HELLO'), '.... . .-.. .-.. ---')
        self.assertEqual(self.encoder.action('HELLO WORLD'), '.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
        self.assertEqual(self.encoder.action('HELLO WORLD I'), '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. / ..')


if __name__ == '__main__':
    unittest.main()
