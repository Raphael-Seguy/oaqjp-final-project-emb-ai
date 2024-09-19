from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):

        ''' First unittest with a joyful statement, should return joy.'''
        result1=emotion_detector("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"],"joy")

        ''' Second unittest with an angry statement, should return anger.'''
        result2=emotion_detector("I am really mad about this")
        self.assertEqual(result2["dominant_emotion"],"anger")

        '''Third unittest with a disgusted statement, should return disgust'''
        result3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3["dominant_emotion"],"disgust")

        '''Fourth unittest with a sad statement, should return sadness'''
        result4=emotion_detector("I am so sad about this")
        self.assertEqual(result4["dominant_emotion"],"sadness")

        '''Fifth unittest with a fearful statement, should return fear'''
        result5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5["dominant_emotion"],"fear")

        '''Sixth unittest with only numbers, should return joy '''
        result6=emotion_detector("11111")
        self.assertEqual(result6["dominant_emotion"],"joy")

        '''Seventh unittest with an empty string, should return None '''
        result7=emotion_detector("")
        self.assertEqual(result7["dominant_emotion"],"None")

unittest.main()
