from chatbot import chatbot

from flask import Flask, render_template, request

from coronavirus import Coronavirus

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    if ('status' in user_text) or ('Covid status' in user_text) or ('Coronavirus status' in user_text):
        bot = Coronavirus()
        return bot.get_data()
    else:
        return str(chatbot.get_response(user_text))


if __name__ == "__main__":
    app.run()
