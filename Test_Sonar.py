import unittest
from mock import Mock, patch
from Sonar import distanceMeasurement

class TestStringMethods(unittest.TestCase):

    @mock.patch('Adafruit_BBIO.input')
    def test_distanceMeasurement(self):
        ECHO_PIN = "P8_11"
        TRIGGER_PIN = "P8_12"
        timeDuration = .01
        SPEED_OF_SOUND_CM = 17150
        expected = timeDuration * SPEED_OF_SOUND_CM
        actualDistance = distanceMeasurement(TRIGGER_PIN,ECHO_PIN)

        self.assertEqual(expected, actualDistance)

if __name__ == '__main__':
    unittest.main()