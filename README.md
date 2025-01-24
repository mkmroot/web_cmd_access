# web_cmd_access
💡   This is using for run commands on host server by the browser web page.


📝 **steps:**

Creating a virtual environment in Ubuntu 20.04 is quite straightforward. Here's a step-by-step guide to setting it up:

**Step 1:**  Install Python and pip
First, ensure that Python and pip are installed on your system.

Update the package list:

```bash 
sudo apt update
```
Install Python 3 and pip: Python 3 is likely already installed on Ubuntu 20.04, but you can install it if needed along with pip.

```bash 
sudo apt install python3 python3-pip
```

**Step 2:**   Install virtualenv

Install virtualenv:

```bash 
sudo apt install python3-virtualenv
```
**Step 3:**   Create a Virtual Environment
Now that you have virtualenv or venv installed, you can create a virtual environment.

Navigate to your project directory (or where you want to create the environment):

```bash 
cd /path/to/your/project
```
Create a virtual environment: If you're using virtualenv:

```bash 
python3 -m venv myenv
```
Or if you're using virtualenv (which has more features):

```bash 
virtualenv myenv
```


Activate the virtual environment:

```bash
source myenv/bin/activate
```

-------------------------------------------------------------------------------------------------------------
Flask module install
```bash
pip install flask
```
```bash
python app.py
```
![image](https://github.com/user-attachments/assets/caa3ccba-ef5f-433e-aa9a-bdc037239fdf)

