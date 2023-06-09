from flask import Flask, render_template, request, redirect, url_for
import os
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_upload():
    return render_template(template_name_or_list='upload.html')

@app.route('/result')
def hello():
    
    benfordValues = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

    # get data from flat file
    #'7_2009'
    #return a generic error page in case of bad column name
    #Stretch goal: change input from text to dropdown with only valid column names
    try:
        values = utils.get_list_from_flat_file(os.path.join(app.static_folder, request.args.get('filename')), request.args.get('column'))
    except:
        return render_template(template_name_or_list='error.html', msg='You have provided an invalid column name. Please check your work and try again.')

    total = len(values)

    #get expected values using
    expected = utils.get_expected_values_numeric(total)
    
    #capture occurences as number for 1-9, skip values starting with 0, error on unexpected values
    try:
        observed = utils.get_occurences_by_first_digit(values)
    except Exception:
        return render_template(template_name_or_list='error.html', msg='The targeted column does not conform to the required values.')

    #populate observed percentages
    observedPercent = utils.get_observed_percentages(observed, total)

    # return graph of sorted values
    return render_template(
        template_name_or_list='graphresults.html',
        data=observedPercent,
        labels=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        benvals=benfordValues,
        benford=utils.get_does_data_pass_benfords_law(benfordValues, observedPercent),
        expected=expected,
        observed=observed
    )

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    column = request.form.get('target_column_name')
    if os.path.splitext(uploaded_file.filename)[1] not in ['.csv', ''] or uploaded_file.filename == '':
        return render_template(template_name_or_list='error.html', msg='Only flat files with non-empty names are permitted.')
    else:
        uploaded_file.save(os.path.join(app.static_folder, uploaded_file.filename))
    return redirect(url_for('hello', column=column, filename=uploaded_file.filename))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
