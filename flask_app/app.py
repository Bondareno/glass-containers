from flask import Flask, render_template
from utils.files_count import files_count
from utils.extensions_count import extensions_count
from utils.top_by_size import top_by_size

app = Flask(__name__)

db_path = 'data/index.sqlite'

@app.route('/')
def index():
    mod_time = f"Last Modified: {time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(db_path)))}"
    files_count = f_count(db_path)
    return render_template('index.html', mod_time=mod_time, files_count=files_count)

@app.route('/ext_stat')
def ext_stat():
    res = extensions_count(db_path, 10)
    return render_template('ext_stat.html', extensions=res)

@app.route('/top_10_by_size')
def top_10_by_size():
    res = top_by_size(db_path, 10)
    return render_template('top_10_by_size.html', top_files=res)

if __name__ == '__main__':
    app.run(debug=True)
