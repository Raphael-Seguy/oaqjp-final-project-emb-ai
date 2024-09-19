'''Wrapper to interact with the AI API'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    The function that will make the call to the API
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myheaders = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = { "raw_document": { "text": text_to_analyse } }

    emotion_response = requests.post(url, json=myjson, headers=myheaders, timeout=10)

    if emotion_response.status_code != 400:
        formated_emotion_response = json.loads(emotion_response.text)

        emotions_list = formated_emotion_response['emotionPredictions'][0]['emotion']

        anger=emotions_list['anger']
        disgust=emotions_list['disgust']
        fear=emotions_list['fear']
        joy=emotions_list['joy']
        sadness=emotions_list['sadness']

        dominant_emotion = determine_dominant_emotion(emotions_list)
    else:
        anger=None
        disgust=None
        fear=None
        joy=None
        sadness=None

        dominant_emotion = None

    return {"anger" : anger, "disgust" : disgust, "fear" : fear, "joy" : joy, "sadness" : sadness, "dominant_emotion" : dominant_emotion}

def determine_dominant_emotion(emotion_dict):
    '''
    The function that determine which emotion is dominating 
    by comparing values and keeping the key with the highest value in the dictionary.
    '''
    return max(emotion_dict, key=emotion_dict.get)
