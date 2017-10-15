from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    make_response
)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/results/<request>')
def results(request):
    return 'you\'d push {}'.format(request)


@app.route('/home/<string:name>')
def main(name):
    return redirect(url_for('results', request=name))


@app.route('/posts<int:post_id>')
def posts(post_id):
    """returns post message"""
    return 'you\'d open an {} post'.format(post_id)


@app.route('/evaluate/<int:value>')
def evaluate(value):
    """Evaluate given value and
    render the only template"""
    return render_template('index.html', value=value)


@app.route('/build_table/')
def build_table():
    dict = {
        'цена': 2,
        'время': '10:10',
        'цвет': 'white'
    }
    return render_template('table.html', dict=dict)


@app.route('/portrait')
def portrait():
    return render_template("portrait_desc.html")


@app.route('/portrait_description', methods=['GET', 'POST'])
def portrait_description():
    if request.method == 'POST':
        data_portrait = request.form
        return render_template('portrait_final.html', data=data_portrait)
    return render_template('portrait_desc.html')


@app.route('/set_cookie')
def set_cookie():
    resp = make_response(render_template('set_cookies.html'))
    resp.set_cookie('name', 'ваши куки')
    return resp


@app.route('/get_cookie')
def get_cookie():
    return render_template('get_cookies.html',
                           cookies=request.cookies.get('name'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
