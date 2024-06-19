# WDYK Prompter

WDYK Prompter is a Flask-based web application designed to help users understand the prerequisites, main subjects, and subsequent topics they can explore after studying a specific topic in Python programming.

## Features

- **Dynamic Knowledge Input**: Users can input what they currently know, and the system will adjust its responses based on this knowledge.
- **Topic Exploration**: Users can query about any topic related to Python, and the system will provide detailed information about prerequisites, the main subjects covered under the topic, and suggestions for further study.
- **Intelligent Response Generation**: Leveraging the Gemini-1.5-flash model from Google's generative AI, the application provides accurate and context-aware responses.

## How to Use

0. **Input your Gemini API key**: I almost uploaded my own. Please get your own key [here](https://ai.google.dev/gemini-api/docs/api-key). Put it into WDYK_prompter.py to use the application.
1. **Start the Application**: Run the Flask server by executing `python WDYK_prompter.py`.
2. **Access the Web Interface**: Open a web browser and go to `http://127.0.0.1:5000/`.
3. **Enter Knowledge and Topic**: Use the web form to enter the knowledge you already possess and the topic you want to explore.
4. **Generate Information**: Submit the form, and the system will generate information about the prerequisites, the subjects covered, and further topics to explore.

## Installation

To set up the WDYK Prompter on your local machine, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Install the required Python packages using `pip install -r requirements.txt`.
3. **Set Up Environment Variables**: Ensure you have set the necessary API keys and environment configurations.
4. **Run the Application**: Execute the Flask application with `python WDYK_prompter.py`.

## Disclaimer

Ashton Andrepont is lazy and asked an AI to do all of this. It's useful nonetheless!
