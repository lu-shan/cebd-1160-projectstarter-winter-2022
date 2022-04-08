from flask import Flask, jsonify
import BAL.workstats


def workstats_service():

    app = Flask(__name__)
    # app.config["DEBUG"] = True

    @app.route('/v1/stats/data/full', methods=['GET'])
    def get_full_data():
        return jsonify(BAL.workstats.get_full_data())

    @app.route('/v1/stats/data/students', methods=['GET'])
    def get_students():
        return jsonify(BAL.workstats.get_students())

    @app.route('/v1/stats/data/province/<name>', methods=['GET'])
    def get_data_by_province_name(name):
        return jsonify(BAL.workstats.get_data_by_province_name(name))

    @app.route('/v1/stats/data/lfs/<lfs>', methods=['GET'])
    def get_data_by_labour_force_status(lfs):
        return jsonify(BAL.workstats.get_data_by_labour_force_status(lfs))

    @app.route('/', methods=['GET'])
    def home():
        return """<h1>Canada Work Statistics</h1><p>This site is a prototype API for reporting work
         statistics for use with Python and Pandas clients.</p>"""

    app.run(host='0.0.0.0')