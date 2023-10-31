from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

categories = {
    "Inspirational Quotes": [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
    ],
    "Jokes": [
        "Why don't scientists trust atoms? Because they make up everything.",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "Hear about the new restaurant called Karma? There’s no menu: You get what you deserve."
    ],
    "Fun Facts": ["The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space.",
    "Australia is wider than the moon. The moon sits at 3400km in diameter, while Australia’s diameter from east to west is almost 4000km.",
    "Human teeth are the only part of the body that cannot heal themselves. Teeth are coated in enamel which is not a living tissue."]
    # Add more categories and content here
}

@app.route('/')
def index():
    return render_template('index.html', category_names=list(categories.keys()))

@app.route('/get_content/<category>')
def get_content(category):
    if category in categories:
        content = random.choice(categories[category])
        return jsonify({"content": content})
    else:
        return jsonify({"content": "Category not found."})

if __name__ == "__main__":
    app.run(debug=True)
