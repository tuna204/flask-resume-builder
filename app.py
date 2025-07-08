from flask import Flask, render_template, request
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form
    return render_template('preview.html', data=data)

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # use your actual path
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@app.route('/download', methods=['POST'])
def download():
    data = request.form
    rendered = render_template('preview.html', data=data)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = app.response_class(pdf, mimetype='application/pdf')
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response



if __name__ == '__main__':
    app.run(debug=True)
