from flask import Flask,render_template,redirect,url_for
from forms import Signup,Login,ItemScanner,PackageScanner,DataRequired
from models import User,session,Model
from checkout import Cart
from flask_bootstrap import Bootstrap4
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
boostrap = Bootstrap4(app)

app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup(): 
    form = Signup()
    if form.validate_on_submit(): 
        pwd = generate_password_hash(form.password.data,'pbkdf2',salt_length=16)
        new_user = User(
            full_name = form.full_name.data,
            email = form.email.data,
            password = pwd,
        )
        session.add(new_user)
        session.commit()
        return redirect('/')

    return render_template('signup.html',form=form)
@app.route('/login',methods=['GET','POST'])
def login(): 
    form = Login()
    if form.validate_on_submit():
        saved_pwd = Model.fetch_user_password(email=form.email.data)
        form_pwd = generate_password_hash(form.password.data,'pbkdf2',salt_length=16)
        print(saved_pwd)
        print(form_pwd)
        if saved_pwd != form_pwd: 
            return "<h1> Signed in Successfully</h1>"
        else: 
            return redirect('/login')

    return render_template('login.html',form= form)


if __name__ == '__main__': 
    app.run(debug=True)
