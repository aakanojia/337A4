import unittest
import impl

class TestPhysicalInfo(unittest.TestCase):

    def test_set_temperature_valid(self):
        pi = impl.PhysicalInfo()
        valid_temperatures = [95, 99.5, 104]
        for temp in valid_temperatures:
            with self.subTest(temp=temp):
                pi.set_temperature(temp)
                self.assertEqual(pi.temperature, temp)

    def test_set_temperature_invalid(self):
        pi = impl.PhysicalInfo()
        invalid_temperatures = [94.9, 104.1, "a string", None, 200]
        for temp in invalid_temperatures:
            with self.subTest(temp=temp):
                with self.assertRaises(ValueError):
                    pi.set_temperature(temp)

if __name__ == '__main__':
    unittest.main()
