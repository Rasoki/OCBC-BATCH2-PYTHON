# from flask import Flask
# app = Flask(__name__)

# # @app.route('/shop')
# @app.route('/<page_name>')
# # def hello_world():    
# def hello_world(page_name):    
#     html = 'Hello, World! <br> <h1>Hello World!</h1>'
#     html += '<h2>This is {} page</h2>'.format(page_name)
#     return html

# @app.route('/hello')
# def hello():    
#     return 'Hello, World! <br> <h1>This is Home</h1>'

# if __name__ == '__main__':    
#     app.run()

# @app.route('/user/<username>')
# def show_user_profile(username):    
#     # show the user profile for that user    
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):    
#     # show the post with the given id, the id is an integer    
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):   
#      # show the subpath after /path/    
#      return f'Subpath {escape(subpath)}'

from flask import Flask, request
# from markupsafe import escape

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login() :
    if request.method == 'POST':
        return do_the_login()
    else: 
        return show_the_login_form()

def do_the_login():
    return f'Do the login :: used HTTP Request is {request.method}' 

def show_the_login_form():
    return f'Show the login form :: used HTTP Request is {request.method} <br> and this is the login form' 
if __name__ == '__main__':
    app.run()
