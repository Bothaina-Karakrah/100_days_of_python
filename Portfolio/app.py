from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Passing dynamic params
    portfolio_data = {
        'name': 'Bothaina Karakrah',
        'title': 'Software Engineer',
        'email': 'bothaina.karakrah@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/bothaina-karakrah-57458219a/',
        'github': 'https://github.com/Bothaina-Karakrah',
        'about_text': [
            "Software Engineer with 3+ years at Meta,"
            "I've led backend migrations, designed soultions used by 30+ engineers, and built fraud detection systems while achieving 97% test coverage."
        ],
        'skills': ['Python', 'C++', 'PHP (Hack)', 'SQL'],
        'projects': [
            {
                'title': 'Backend Services Migration ',
                'description': 'Led migration from Python to PHP (Hack), improving system latency by 25%',
                'technologies': ['Python', 'PHP', 'SQL'],
                'github_url': '#'
            },
            {
                'title': 'Fraud Detection Engine',
                'description': 'Developed rules-based system for Shops onboarding, increasing fraud catch rate by 20%',
                'technologies': ['PHP', 'SQL'],
                'github_url': '#'
            },
            {
                'title': 'Snake Game',
                'description': "Built the classic Snake Game",
                'technologies': ['Python', 'OOP', 'turtle'],
                'github_url': 'https://github.com/Bothaina-Karakrah/100_days_of_python/tree/main/day20_snake_game'
            },
            {
                'title': 'quizzler',
                'description': "Interactive quiz app using tkinter with OOP and dynamic question flow via API",
                'technologies': ['Python', 'OOP', 'tkinter'],
                'github_url': 'https://github.com/Bothaina-Karakrah/100_days_of_python/tree/main/day34_quizzler'
            }
        ]
    }

    return render_template('index.html', data=portfolio_data)


if __name__ == '__main__':
    app.run(debug=True)