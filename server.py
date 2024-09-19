from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    textToAnalyze = request.args.get('textToAnalyze')
    result = emotion_detector(textToAnalyze)

    anger = result["anger"]
    disgust = result["disgust"]
    joy = result["joy"]
    fear = result["fear"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)