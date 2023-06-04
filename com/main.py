from flask import Flask, jsonify
import ScrapeCurrency

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p> Example URL: /api/v1/use-eur</p>'


@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = ScrapeCurrency.get_currency(in_cur, out_cur)
    res_dict = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': rate}
    return jsonify(res_dict)


app.run()
