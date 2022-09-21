from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/posttest', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        print('post')
        print(request.form)
        print(request.form['inputtext'])
        return render_template('index.html')
    elif request.method == 'GET':
        print('get')
        return render_template('index.html')


# if __name__ == '__main__:':
app.run(host="0.0.0.0", port=5001, debug=True)
