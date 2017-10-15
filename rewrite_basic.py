from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/post/<int:post_id>/')
def posts(post_id):
    return 'You\'re at post number {}'.format(post_id)
