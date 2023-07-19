from flask import Flask, url_for, request, make_response, Response, abort, redirect, render_template, jsonify, session
from markupsafe import escape

app = Flask(__name__)

# VARIABLES RULES, ROUTING, REDIRECTION BEHAVIOUR
# @app.route('/')
# def index():
#     return "<h1>hello world!</h1>"
# @app.route('/<name>')
# def hello_name(name):
#     return f"haloo {name}"
# @app.route('/user/<username>')
# def hello_username(username):
#     safe = escape(username)
#     return f"haloo {safe}"
# @app.route('/path/<string:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'
# @app.route('/users/')
# def users():
#     return "halooo userss"
# @app.route('/about')
# def about():
#   return "halooo about"


# URL BUILDING
# @app.route('/')
# @app.route('/')
# def home():
#     return 'Home Page'
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User {username} Profile'
# @app.route('/product/<int:product_id>')
# def show_product(product_id):
#     return f'Product ID: {product_id}'
# @app.route('/dashboard')
# def dashboard():
#     # Menggunakan url_for() untuk membangun URL berdasarkan nama rute
#     home_url = url_for('home')
#     user_url = url_for('show_user_profile', username='john')
#     product_url = url_for('show_product', product_id=123)
#     # Menampilkan URL yang dibangun
#     return f'''
#         <h1>Dashboard</h1>
#         <p><a href="{home_url}">Home</a></p>
#         <p><a href="{user_url}">User Profile</a></p>
#         <p><a href="{product_url}">Product</a></p>
#     '''


# HTTP METHODS
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         text = 'request method: ' + request.method
#         print(f'request method: {request.method}')
#         return text
#     else:
#         text = 'request method: ' + request.method
#         print(f'request method: {request.method}')
#         return text
# @app.get('/login')
# def login():
#     text = 'request method: ' + request.method
#     return f'''
#         <h1>{text}</h1>
#     '''
# @app.post('/login')
# def login_post():
#     text = 'request method: ' + request.method
#     return text


# QUERY URLs
# def validator(value, value2):
#     if value is None or value2 is None:
#         raise TidakValid("Tidak Bisa diterima")
#     else:
#         return "berhasil"
# @app.route('/login', methods=['GET'])
# def login():
#     error = None
#     pesan = None
#     if request.method == 'POST':
#         try:
#             pesan = validator(request.form["username"], request.form["password"])
#         except TidakValid as err:
#             print(err)
#     print(pesan)
#     params = request.args.get('key')
#     if params:
#         return params
#     else:
#         return pesan


# COOKIES
# @app.route('/')
# def set_cookies():
#     response = Response('berhasil membuat coookies')
#     response.set_cookie('refreshToken', '1234567')
#     return response
# @app.route('/token')
# def get_cookies():
#     cookies = request.cookies.get('refreshToken')
#     return f'<h1>refreshToken: {cookies}</h1>'


# REDIRECT AND ERRORS
# @app.route('/')
# def index():
#     response = redirect('login')
#     response.set_cookie('token', '123')
#     return response
# @app.route('/login')
# def login():
#     cookies = request.cookies.get('token')
#     if cookies:
#         return f'<h1>token: {cookies}</h1>', 201
#     else:
#         abort(401)
# @app.errorhandler(404)
# def error_404(error):
#     print(error)
#     return render_template('error404.html'), 404
# @app.errorhandler(401)
# def error_401(error):
#     print(error)
#     return render_template('error401.html')


# WITH JSON
# user_data = (
#     ("JohnDoe", "dark", "profile1.jpg"),
#     ("JaneSmith", "light", "profile2.jpg"),
#     ("MikeJohnson", "dark", "profile3.jpg"),
#     ("SarahWilliams", "light", "profile4.jpg"),
#     ("DavidBrown", "dark", "profile5.jpg")
# )
# def to_json(username,theme,image):
#     return {
#         "username": username,
#         "theme": theme,
#         "image": image
#     }
# jsonify() untuk men json kan dict or list
# @app.route('/')
# def send_json():
#     data = [to_json(user[0],user[1],user[2]) for user in user_data]
#     return data


# SESSION
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def index():
    url_login = url_for('login')
    url_logout = url_for('logout')
    if 'logged' in session:
        return f'<h1>your login is {session["logged"]} and here for <a href="{url_logout}">logout</a></h1>'
    return f'<p>you are not login yet go to <a href="{url_login}">login</a></p>'
@app.route('/login')
def login():
    session['logged'] = 'yes'
    return redirect(url_for('index'))
@app.route('/logout')
def logout():
    session.pop('logged', None)
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)