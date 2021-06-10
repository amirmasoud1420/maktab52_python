from flask import Flask, request, render_template


class User:
    def __init__(self, fname, lname, phone, gender):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.gender = gender


user_list = []

app = Flask(__name__, template_folder='templates')


# @app.route('/')
def just_get():
    return render_template('t3.html')


# @app.route('/', methods=['POST'])
def register():
    args = request.form
    u = User(args['fname'], args['lname'], args['phone'], args['gender'])
    user_list.append(u)
    print(user_list)
    return f"name = {u.fname} {u.lname} <br>phone = {u.phone} <br>gender = {u.gender}"


# @app.route('/<phone>')
def show_user(phone):
    for i in user_list:
        if i.phone == phone:
            return i.fname
    else:
        return "not found"


# @app.route('/list')
def show_list():
    s = ""
    for i in user_list:
        s += i.fname + "<br>"
    return s

app.add_url_rule('/','index',just_get,methods=['GET'])
app.add_url_rule('/','register',register,methods=['POST'])
app.add_url_rule('/<phone>','get-user',show_user)
app.add_url_rule('/list','user-list',show_list)

app.run()
