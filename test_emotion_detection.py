''' Unittester for the wrapper module that we just created '''
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    ''' Unittester class for the wrapper module that we just created '''
    def test_emotion_detection(self):
        ''' Unittester function for the wrapper module that we just created '''

        result1=emotion_detector("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"],"joy")

        result2=emotion_detector("I am really mad about this")
        self.assertEqual(result2["dominant_emotion"],"anger")

        result3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3["dominant_emotion"],"disgust")

        result4=emotion_detector("I am so sad about this")
        self.assertEqual(result4["dominant_emotion"],"sadness")

        result5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5["dominant_emotion"],"fear")

        result6=emotion_detector("11111")
        self.assertEqual(result6["dominant_emotion"],"joy")

        result7=emotion_detector("")
        self.assertEqual(result7["dominant_emotion"],"None")

unittest.main()
