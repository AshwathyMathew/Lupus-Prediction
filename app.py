import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/',methods=['Get','Post'])
def home():
     return render_template('Dashboard.html')
@app.route('/Lupusprediction', methods=['GET', 'POST'])
def Lupusprediction():
    msg=''
    output=""
    if request.method == 'POST':
        age = int(request.form['Age'])
        gender = int(request.form['Gender'])
        Sickness_time_duration = int(request.form['Sickness_time_duration'])
        Esbach = int(request.form['Esbach'])
        MBL_Level = int(request.form['MBL_Level'])
        ESR = int(request.form['ESR'])
        C3 = int(request.form['C3'])
        C4 = int(request.form['C4'])
        CRP = int(request.form['CRP'])
        ANA = int(request.form['ANA'])
        ANTIdsDNA = int(request.form['ANTIdsDNA'])
        SLE_DAI = int(request.form['SLE_DAI'])
        test_data=[age,gender, Sickness_time_duration ,Esbach,MBL_Level,ESR,C3,C4,CRP,ANA,ANTIdsDNA,SLE_DAI]
        print("test_data",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score
        data = pd.read_csv("static/data_lupus.csv")
        data.head()

        data.info()
        Y= data['Lupus']
        X= data.drop('Lupus', axis=1)
        

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        model = DecisionTreeClassifier(criterion='entropy', random_state=1)
        model.fit(X_train, Y_train)

        Predictions = model.predict([test_data])
        print(Predictions)
        if(Predictions[0]==0):
                print("No Lupus Disease")
                output="No Lupus Disease"
        else:
                print("Lupus Disease")
                output="Lupus Disease"

    return render_template('Lupus_Prediction.html', msg=msg, output= output, Title="Lupus Disease Prediction")
@app.route('/Dashboard', methods=['GET', 'POST'])
def Dashboard():
    return render_template('Dashboard.html', Title="Lupus Disease Prediction")
  
if __name__ == '__main__':
    app.run(port=5000,debug=True)
