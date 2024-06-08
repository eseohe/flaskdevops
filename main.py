from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class MyModel(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(500))


def init_db():
    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    return "hello"


@app.route("/base")
def base():
    my_list = MyModel.query.all()
    var = "variable"
    return render_template("base.html", var=var, my_list=my_list)


@app.route("/insert", methods=["POST"])
def add():
    c_name = request.form.get("c_name")
    new_c_name = MyModel(c_name=c_name)
    db.session.add(new_c_name)
    db.session.commit()
    return redirect(url_for("base"))


@app.route("/delete/<int:c_id>")
def remove(c_id):
    c_name = MyModel.query.get_or_404(c_id)
    db.session.delete(c_name)
    db.session.commit()
    return redirect(url_for("base"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
