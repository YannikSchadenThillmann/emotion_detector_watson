''' server.py module '''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' renders index page '''
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    ''' use app on server '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dom_emo = response["dominant_emotion"]
    if dom_emo is None:
        return "Invalid text! Please try again!"
    # Return a formatted string with the sentiment label and score
    response_copy = dict(response)
    del response_copy["dominant_emotion"]
    response_str = str(response_copy).strip("}{")
    message1 = f"For the given statement, the system response is {response_str}."
    message2 = f"The dominant emotion is <b>{dom_emo}</b>."
    return message1 + message2

if __name__ == "__main__":
    app.run(debug = True)
