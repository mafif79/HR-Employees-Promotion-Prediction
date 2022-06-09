from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)



LABEL = ['Not Promoted', 'Promoted']
columns = ['education', 'age', 'previous_year_rating', 'length_of_service', 'no_of_trainings', 'avg_training_score', 'awards_won']
with open("HR_analytics_pipe.pkl", "rb") as f:
    model_HR_analytics = pickle.load(f)



@app.route("/")
def homepage():
    return "<h1>Backend Pemodelan HR Analytics </h1>"



@app.route("/hranalytics", methods=['GET','POST'])
def hranalytics_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [data['Education'], 
                    data['Age'],
                    data['Previous Year Rating'],
                    data['Length of Service'],
                    data['How many times do you do the training?'],
                    data['Average Training Score'],
                    data['Have you won an awards while working here?']]
        
        new_data = pd.DataFrame([new_data],columns=columns)
        


        res = model_HR_analytics.predict(new_data)
        response = {'code':200, 'status':'OK',
                    'result':{'prediction':str(res[0]),
                                'classes': LABEL[res[0]]}}
        return jsonify(response)
    return 'Silahkan gunakan method psot untuk mengakses model HR Analytics'

app.run(debug=True)

