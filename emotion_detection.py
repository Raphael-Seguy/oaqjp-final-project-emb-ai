import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myheaders = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = { "raw_document": { "text": text_to_analyse } }

    emotion_response = requests.post(url, json=myjson, headers=myheaders)
    formated_emotion_response = json.loads(emotion_response.text)

    emotions_list = formated_emotion_response['emotionPredictions'][0]['emotion']

    anger=emotions_list['anger']
    disgust=emotions_list['disgust']
    fear=emotions_list['fear']
    joy=emotions_list['joy']
    sadness=emotions_list['sadness']

    dominant_emotion = determine_dominant_emotion(emotions_list)
    

    return {"anger" : anger, "disgust" : disgust, "fear" : fear, "joy" : joy, "sadness" : sadness, "dominant_emotion" : dominant_emotion}

def determine_dominant_emotion(emotionDict):
    return max(emotionDict, key=emotionDict.get)
