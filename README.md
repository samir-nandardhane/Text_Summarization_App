# Text_Summarization_App

---
Problem Overview:
This project aims to create a Text summarization tool using the Hugging Face model `facebook/bart-large-cnn`. It takes input text data and generates a summary based on specified length parameters.

Solution Outline:
- HTML Interface: `index.html` provides a user interface to input data and view the generated summary.
- Flask Backend: `app.py` handles the incoming requests, processes the data through the Hugging Face API, and renders the output on the HTML interface.
- Requirements: `requiremt.txt` lists the necessary Python packages and dependencies required to run the system.

Example Input and Output:
- Input: User enters the data into the provided text area.
- Output: The system generates a summary of the input text based on defined length parameters.

Setup Instructions:
1. Install Dependencies: Use `pip install -r requiremt.txt` to install the required packages.
2. Run the System: Execute `python app.py` and navigate to `http://localhost:5000` in your browser.
3. Usage: Enter text in the input field, set the summary length, and click "Submit" to generate the summary.

Additional Information:
- Dataset Link: The system doesn’t require a specific dataset as it utilizes the Hugging Face model.
- Re-compiling and Re-running: Ensure dependencies are installed, and Flask is running to re-compile and re-run the system.

---

Detailed Comments (in source code)

In `index.html` and `app.py`, detailed comments should be added explaining the functionality of each section and clearly identifying the authors of specific sections or functionalities. Focus on making the comments easy to understand for other developers.

---

Project Functionality

The project successfully implements data summarization using the specified Hugging Face model. It handles user inputs, interacts with the model's API, generates summaries based on given parameters, and displays the output on the HTML interface. Additionally, it should be tested with various datasets to ensure consistent and accurate summarization.

---

Code References/Acknowledgements

- The HTML and backend code structure are based on Flask and Hugging Face's API documentation.
- Proper attribution should be given to Hugging Face for the model usage and to Flask for the web framework.
---
