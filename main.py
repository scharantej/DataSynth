
# main.py

from flask import Flask, render_template, request, redirect, url_for, send_file
import faker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_rows = int(request.form['num_rows'])
    num_cols = int(request.form['num_cols'])
    data_types = request.form.getlist('data_types')

    fake = faker.Faker()
    data = []
    for _ in range(num_rows):
        row = []
        for data_type in data_types:
            if data_type == 'name':
                row.append(fake.name())
            elif data_type == 'email':
                row.append(fake.email())
            elif data_type == 'address':
                row.append(fake.address())
            elif data_type == 'date':
                row.append(fake.date())
        data.append(row)

    return render_template('results.html', data=data)

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/download')
def download():
    data = request.args.get('data')
    filename = 'data.csv'
    with open(filename, 'w') as f:
        f.write(data)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
