from flask import Flask, render_template, request, redirect, url_for
import subprocess
import shlex

app = Flask(__name__)

# Define allowed commands
ALLOWED_COMMANDS = ['ls', 'pwd', 'df', 'top', 'whoami', 'tail']

# Sanitize the command by checking if it is in the allowed commands list
def sanitize_command(command):
    command_parts = command.split(' ')
    base_command = command_parts[0]

    if base_command in ALLOWED_COMMANDS:
        # Use shlex.split to safely handle arguments (avoiding injection issues)
        return shlex.split(command)
    else:
        return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', output="")

@app.route('/run-command', methods=['POST'])
def run_command():
    command = request.form['command']
    sanitized_command = sanitize_command(command)

    if sanitized_command is None:
        return render_template('index.html', output="Command not allowed.")
    
    try:
        # Execute the command using subprocess
        result = subprocess.check_output(sanitized_command, stderr=subprocess.STDOUT, universal_newlines=True)
        return render_template('index.html', output=result)
    except subprocess.CalledProcessError as e:
        return render_template('index.html', output=f"Error: {e.output}")
    except Exception as e:
        return render_template('index.html', output=f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
