from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    age = 25
    # pets = ['cat', 'dog', 'bird', 'fish']
    # pet_names = {'cat': 'cccc', 'dog': 'dddd'}
    # return render_template('hello.html', 
    #                         name=name, 
    #                         age=age,
    #                         pet_list= pets,
    #                         pet_names_dict= pet_names)
    # return render_template('hello.html', template_name=name)
    return 'Hallo'
if __name__ == '__main__':
    app.run(debug=True)