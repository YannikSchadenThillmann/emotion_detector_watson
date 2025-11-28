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
    response_list = list(response.items())
    response_list_formatted = [item[0]*": "*item[1] for item in response_list[0:5]]
    dom_emo = response_list[5][1]
    return "For the given statement, the system response is {}. The dominant emotion is {}.".format(response_list_formatted,dom_emo)

if __name__ == "__main__":
    app.run(debug = True)
