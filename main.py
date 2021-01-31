from flask import Flask, render_template
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def index():
    return render_template('index.html', x = '0')


def main():
    app.run(host='0.0.0.0')
	
if __name__ == "__main__":
    main()
