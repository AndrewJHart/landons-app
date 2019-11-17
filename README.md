## Landon's Science Questionnaire

> This is a simple test app to prove a theory for a science fair project

## How to setup 

> This project uses python 3, so ensure you're using any version of
> python 3, then this script should work fine.

Use your terminal to CD into your the root of your project code. For example
our project is located in `~/repos/landons-app` so we would go to that directory
like so:
```bash
$ cd ~/repos/landons-app
```
> note, replace landons-app with your project name

Next, create a python 3 virtual environment: 
```bash
$ python -m venv venv
```
This will create a folder in your project directory named venv that contains
all the dependencies you need to run your python project in a local scope 
so as not to affect global python packages or versions.

Lastly, you need to activate the virtual environment to ensure your python
dependencies are being installed only into the venv folder within the 
project directory. To activate the virtual environment run this command

```bash
$ venv/Scripts/activate.bat
```
