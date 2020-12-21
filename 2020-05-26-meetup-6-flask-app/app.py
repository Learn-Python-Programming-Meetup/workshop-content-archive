from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['task_content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception:
            return "DB operation failed"
    else:
        todo_tasks = Todo.query.order_by(Todo.date_added).all()
        return render_template('index.html', todo_tasks=todo_tasks)


@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except Exception:
        return "DB Delete went wrong!!"


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['task_update']
        try:
            db.session.commit()
            return redirect("/")
        except Exception:
            return "Something went wrong"
    else:
        return render_template('update.html', task_to_update=task_to_update)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
