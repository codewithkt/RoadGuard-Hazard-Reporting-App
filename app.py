from flask import Flask, render_template, request, jsonify 

app = Flask(__name__) 

# Sample data for demonstration purposes (replace with a real database in a real implementation) 

# Sample data for demonstration purposes (replace with a real database in a real implementation)
hazard_reports = [
    {
        'location': 'Plano',
        'type': 'Accident',
        'description': 'Car accident on Coit Road'
    },
    {
        'location': 'Allen',
        'type': 'Road work',
        'description': 'Construction on Renner Road'
    },
    {
        'location': 'Frisco',
        'type': 'Accident',
        'description': 'Accident on Custor Pkwy'
    }
]

@app.route('/') 

def index(): 

    return render_template('index.html') 

@app.route('/submit_hazard', methods=['POST']) 

def submit_hazard(): 

    location = request.form['location'] 

    hazard_type = request.form['type'] 

    description = request.form['description'] 

    # In a real implementation, add the hazard report to the database 

    hazard_report = { 

        'location': location, 

        'type': hazard_type, 

        'description': description 

    } 
    hazard_reports.append(hazard_report) 
    return jsonify({'status': 'success'}) 

@app.route('/get_hazard_reports', methods=['GET']) 

def get_hazard_reports(): 

    # In a real implementation, retrieve hazard reports from the database 

    return jsonify({'hazard_reports': hazard_reports}) 


if __name__ == '__main__': 

    app.run(debug=True) 

 