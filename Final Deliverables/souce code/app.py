from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('knn.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/riskpred', methods=['GET', 'POST'])
def predict_risk():
    if request.method == "POST":
        pred = [
            float(request.form['Sector_score']),
            float(request.form['PARA A']),
            float(request.form['Risk A']),
            float(request.form['PARA_B']),
            float(request.form['Risk B']),
            float(request.form['TOTAL']),
            float(request.form['numbers']),
            float(request.form['Money_Value']),
            float(request.form['Score_MV']),
            float(request.form['District_Loss']),
            float(request.form['History']),
            float(request.form['Score']),
            float(request.form['Inherent Risk']),
            float(request.form['Audit_Risk'])
        ]
        output = model.predict([pred])[0]
        return render_template('result.html', predict="The Predicted Risk value is: " + str(output))
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
