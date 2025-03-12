from flask import Flask,render_template
import info
app = Flask(__name__)

@app.route('/')
def home():
    up = info.update
    count = info.count_update()
    pro = info.project
    count_project = info.count_project()
    return render_template('index.html', section= up ,index = count,project = pro,count_project=count_project)

if __name__ == '__main__':
    app.run(debug=True)