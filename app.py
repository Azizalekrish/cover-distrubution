from flask import Flask, render_template
from assign_cover import assign_covers

app = Flask(__name__)

@app.route('/')
def home():
    df = assign_covers('teachers.xlsx', 'covers_needed.xlsx')
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
