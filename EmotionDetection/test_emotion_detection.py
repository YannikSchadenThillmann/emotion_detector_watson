import unittest
from emotion_detection import emotion_detector

class TestMyModule(unittest.TestCase):
    def test_emotion_detector(self):
        text = "I am glad this happened"
        test = emotion_detector(text)["dominant_emotion"]
        check = "joy"
        self.assertEqual(test, check)

        text = "I am really mad about this"
        test = emotion_detector(text)["dominant_emotion"]
        check = "anger"
        self.assertEqual(test, check)

        text = "I feel disgusted just hearing about this"
        test = emotion_detector(text)["dominant_emotion"]
        check = "disgust"
        self.assertEqual(test, check)

        text = "I am so sad about this"
        test = emotion_detector(text)["dominant_emotion"]
        check = "sadness"
        self.assertEqual(test, check)

        text = "I am really afraid that this will happen"
        test = emotion_detector(text)["dominant_emotion"]
        check = "fear"
        self.assertEqual(test, check)

if __name__ == "__main__":
    unittest.main()
