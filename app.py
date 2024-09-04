import requests
from flask import Flask, render_template, url_for
from flask import request as req

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    """
    Renders the index.html template.

    This function is triggered upon accessing the root URL ("/") and handles both GET and POST requests.
    For GET requests, it renders the initial HTML template for the data summarization interface.
    For POST requests, it processes the form data submitted by the user.

    Returns:
        HTML: Renders the index.html template.
    """
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    """
    Summarizes the input text using the Hugging Face API.

    This function handles the summarization process by obtaining data from the submitted form.
    It utilizes the Hugging Face BART model (facebook/bart-large-cnn) through its API endpoint.
    The input data is processed, and the summary is generated based on specified length parameters.

    Returns:
        HTML: Renders the index.html template displaying the generated summary.
    """
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        # Extracting data and length parameters from the form
        data = req.form["data"]
        maxL = int(req.form["maxL"])
        minL = maxL // 4

        def query(payload):
            """
            Sends a POST request to the Hugging Face API.

            This function sends the data payload to the specified API endpoint
            using the requests module and returns the JSON response.

            Args:
                payload (dict): Input data and summarization parameters.

            Returns:
                dict: JSON response from the API containing the summary text.
            """
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        # Creating payload for the Hugging Face API request
        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]

        # Rendering the index.html template with the generated summary
        return render_template("index.html", result=output["summary_text"])
    else:
        # Renders the index.html template for GET requests
        return render_template("index.html")
