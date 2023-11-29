from flask import Flask, render_template, send_file, request, stream_with_context, Response, jsonify
from waitress import serve
import time

app = Flask(__name__, static_folder='dist', static_url_path='')

@app.route('/')
def index():
    return send_file('dist/index.html')



# informal statement to informal solution
@app.post('/api/problem_gpt-3.5__solve')
def problem_gpt35_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/problem_gpt-4__solve')
def problem_gpt4_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/problem_llama2-7b__solve')
def problem_llama27b_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})




# informal statement to formal statement
@app.post('/api/problem_gpt-3.5__formalize')
def problem_gpt35_formalize():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/problem_gpt-4__formalize')
def problem_gpt4_formalize():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/problem_llama2-7b__formalize')
def problem_llama27b_formalize():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})




# informal solution to formal proof
@app.post('/api/solution_gpt-3.5__formalize')
def solution_gpt35_formalize():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/solution_gpt-4__formalize')
def solution_gpt4_formalize():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/solution_llama2-7b__formalize')
def solution_llama27b_formalize():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})




# formal statement to formal proof
@app.post('/api/formal_gpt-3.5__solve')
def formal_gpt35_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/formal_gpt-4__solve')
def formal_gpt4_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})

@app.post('/api/formal_llama2-7b__solve')
def formal_llama27b_solve():
    content = request.json
    data = content['problem_data']
    time.sleep(10)
    print(f'FsToIs: {data}')
    return jsonify({'out': data})


print("Server is running...")
serve(app, host='0.0.0.0', port='8080')