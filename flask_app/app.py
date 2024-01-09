from flask import Flask, render_template
from utils import count_files, top_10_ext, top_10_files_weight
from filesmeta import common_minion, doc_minion, gru, img_minion, pdf_minion

app = Flask(__name__)

@app.route('/')
def index():
    num_of_files = count_files.get_num_of_files()
    top_extensions = top_10_ext.get_top_10_extensions()
    top_files_weight = top_10_files_weight.get_top_10_files_weight()

    return render_template('index.html', num_of_files=num_of_files, top_extensions=top_extensions, top_files_weight=top_files_weight)

if __name__ == '__main__':
    app.run(debug=True)
