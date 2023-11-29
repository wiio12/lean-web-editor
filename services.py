from flask import Flask, render_template, send_file, request, stream_with_context, Response, jsonify
from waitress import serve
import time

app = Flask(__name__, static_folder='dist', static_url_path='')

@app.route('/')
def index():
    return send_file('dist/index.html')

@app.post('/api/problem_gpt-3.5__solve')
def problem_gpt35_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/FsToIs')
def FsToIs():
    content = request.json
    data = content['data']
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/IsToFs')
def IsToFs():
    content = request.json
    data = content['data']
    print(f'IsToFs: {data}')
    return jsonify({'out': data})
    
@app.post('/api/IpToFp')
def IpToFp():
    content = request.json
    data = content['data']
    print(f'IpToFp: {data}')
    return jsonify({'out': data})

@app.post('/api/IsToIp')
def IsToIp():
    content = request.json
    data = content['data']
    print(f'IsToIp: {data}')
    return jsonify({'out': data})


@app.post('/api/FsToFp')
def FsToFp():
    content = request.json
    data = content['data']
    print(f'FsToFp: {data}')
    return jsonify({'out': data})

@app.post('/api/FpToIp')
def FpToIp():
    content = request.json
    data = content['data']
    print(f'FpToIp: {data}')
    return jsonify({'out': data})

print("Server is running...")
serve(app, host='0.0.0.0', port='8080')