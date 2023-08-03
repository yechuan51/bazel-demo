from flask import Flask

from lib import rand_gen

app = Flask(__name__)


@app.route("/")
def generate_random():
    random_number = rand_gen.generate_random_number()
    return f"Random number: {random_number}"


if __name__ == "__main__":
    app.run()
