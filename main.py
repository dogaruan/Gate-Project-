from flask import Flask, request, jsonify
from models import AccessLog
from database import SessionLocal

app = Flask(__name__)

@app.route('/api/access', methods=['POST'])
def log_access():
    data = request.json
    session = SessionLocal()
    log = AccessLog(
        person_id=data['idPersoana'],
        access_time=data['data'],
        direction=data['sens'],
        gate_id=data['idPoarta']
    )
    session.add(log)
    session.commit()
    session.close()
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
