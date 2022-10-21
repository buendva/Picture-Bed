from flask import Flask, render_template
import config
from file import bp as bp_file

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(bp_file)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
