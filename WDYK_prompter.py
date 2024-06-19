from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="INPUT YOUR API KEY HERE")
model = genai.GenerativeModel("gemini-1.5-flash")

knowledge = ["basic math"]
topic = "Beginner Python"
response = ""


@app.route("/")
def index():
    return render_template(
        "index.html", knowledge=", ".join(knowledge), topic=topic, response=response
    )


@app.route("/suggest", methods=["POST"])
def suggest_topic():
    global response, knowledge, topic
    new_knowledge = request.form.get("knowledge")
    new_topic = request.form.get("topic")

    if new_knowledge:
        knowledge = new_knowledge.split(", ")

    if new_topic:
        topic = new_topic

    prompt = f"""
    Based on my current knowledge:
    {", ".join(knowledge)}
    
    What new topic should I learn next?
    Please suggest only one topic, and please only include that topic in your response.
    Feel free to get really creative with it! Choose something that's fun and interesting.
    It doesn't strictly need to be related to what I already know.
    Do not suggest {topic} or anything similar to it.
    """
    suggestion = model.generate_content(prompt).text.strip()
    return jsonify({"suggested_topic": suggestion})


@app.route("/generate", methods=["POST"])
def generate_response():
    global response, knowledge, topic
    new_knowledge = request.form.get("knowledge")
    new_topic = request.form.get("topic")

    if new_knowledge:
        knowledge = new_knowledge.split(", ")

    if new_topic:
        topic = new_topic

    prompt = f"""
    I know:
    {", ".join(knowledge)}
    
    What prerequisites do I need to know to learn {topic}?
    Please list the topics ONLY in a list separated by commas.
    Begin this list with "Prerequisites: ".
    If none are needed, say "None".
    If any prerequisites are already accounted for by things I know, do not include them.
    If all prerequisites are already accounted for by things I know, say "None".
    
    What subjects will I learn by studying {topic}?
    Please list the topics ONLY in a list separated by commas.
    Begin this list with "Subjects: ".
    If none are needed, say "None".
    If any subjects are already accounted for by things I know, do not include them.
    
    What subjects should I try learning after I study {topic}? 
    Please list the topics ONLY in a list separated by commas.
    Begin this list with "Subjects to Try: ".
    If none are needed, say "None".
    
    Your output should look like this:
    Prerequisites: <The prerequisites>
    
    Subjects: <The subjects>
    
    Subjects to Try: <The subjects to try>
    
    If the topic doesn't make sense, use the word "None" for all of the above.
    
    """
    response = (
        model.generate_content(prompt)
        .text.replace("Subjects:", "\nSubjects:")
        .replace("Subjects to Try:", "\nSubjects to Try:")
    )
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
