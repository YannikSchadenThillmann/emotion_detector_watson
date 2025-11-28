from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a formatted string with the sentiment label and score
    response_copy = dict(response)
    del response_copy["dominant_emotion"]
    response_str = str(response_copy).strip("}{")
    dom_emo = response["dominant_emotion"]
    return "For the given statement, the system response is {}. The dominant emotion is <b>{}</b>.".format(response_str, dom_emo)

if __name__ == "__main__":
    app.run(debug = True)
