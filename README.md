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

---

Next you need to activate the virtual environment to ensure your python
dependencies are being installed only into the venv folder within the 
project directory. To activate the virtual environment run this command

**For Windows**
```bash
$ venv/Scripts/activate.bat
```

**For Linux/Mac OSx**
```bash
$ . venv/bin/activate
```

Now you have activated your virtual environment!! Lets install our required 
dependencies that are used for this project e.g. third party dependencies 
that are not built in with python.

---
Lastly, you need to install any of the third party libraries, as mentioned
above, so that the script can run. These dependencies are stored in 
a file called `requirements.txt`. To install all the requirements run 
the following command:

```bash
$ pip install -r requirements.txt
```

If everything works without any error messages then you have successfully
installed the required libraries needed to run your script.

---

 All thats 
left to do is test the script now :D - lets do this by running this command

```bash
$ python truth_game.py
```

If you see a question and answer game, then you have succeeded! w00t

## Notes about the script, its author, and the author of this read me

The author of the script itself was **Landon Hart** who is currently 12 years
 of age and is just learning python! The author of the documentation and some
 guidance was me, **Andrew Hart**, proud father. I've been doing python for 8+ years and 
 wanted to get my son involved, so after many tutorials and a paid course,
 plus a few hours of me "lecturing", we have ended up with a pretty neat
 little game that we intend to run on a raspberry pie with a small screen.
 
## Some info about the questions/clues API and its creator 
 API used for the question, category, and answer data came from 
 [http://jservice.io/](http://jservice.io/) and has been a great help in 
 teaching my son about REST'ful web services as well as transforming JSON
 into actual python data structures that can be manipulated. Much thanks to 
 [https://github.com/sottenad/jService](sottenad) for his github project! 
