'''
The server api to contact our package and get the result from the AI emotion detection.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    '''
    The initial function of our page, to load the html up.
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    '''
    The route that will be used to pass the user input to our wrapper 
    package with the Emotion detection AI.
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyse)

    anger = result["anger"]
    disgust = result["disgust"]
    joy = result["joy"]
    fear = result["fear"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    answer = "For the given statement, the system response is "
    answer+=f"'anger': {anger}, "
    answer+=f"'disgust': {disgust}, "
    answer+=f"'fear': {fear}, "
    answer+=f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}"

    if dominant_emotion is None :
        return "Invalid text! Please try again!"
    return answer

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
