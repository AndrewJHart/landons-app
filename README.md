## Landon's Science Questionnaire

I'm proud of my son and this was first attempt at applying his programming skills, at
age 11, to a real competition aka the science fair :) He did well, but did not win. The UI
was console based (NOT SHINY) as he was not familiar with how to build a fancy frontend at the time
and i'm not the type of parent to do his work for him. Ergo, I believe the judges didn't really 
understand the amount of work he put into completing this project, or how the project really
worked.

## Notes about the script, its author, and the author of this read me

This is a simple python application that my 11 year old son wrote for his
science fair. I wanted to teach him about web applications and consuming API's
so we found a RESTful API oriented around real jeopardy questions. Thus, the goal
was that given a category, the app would grab the first page of questions (100 per page)
and ask those questions, checking the users answer to see if it is correct or as close
as possible. We had to limit some categories due to types of answers and look for keywords
as well as filter out markup that was returned in some of the answers. 

The author of the documentation was me and I provided guidance as well. I've been doing python 
for 10+ years and javascript even longer, and c since I was ~13 years old, so I wanted to get my son involved
as early as possible but also when he became interested via his own curiousity and volition.
So after some time, some tutorials and a paid course, plus a few hours of me teaching, we have 
ended up with a pretty neat little game that we ran on a raspberry pi with a 10 inch HDMI LCD screen
designed for connecting to the pi, as well as a battery and a specially crafted case to which the pi,
battery, and screen were all mounted. This would allow him to simply close the container, pack it up,
take it to school and then put it on display at the science fair. I felt the modularity alone was
interesting but most people don't think like developers. 

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

 
## Some info about the questions/clues API and its creator 
 API used for the question, category, and answer data came from 
 [http://jservice.io/](http://jservice.io/) and has been a great help in 
 teaching my son about REST'ful web services as well as transforming JSON
 into actual python data structures that can be manipulated. Much thanks to 
 [https://github.com/sottenad/jService](sottenad) for his github project! 
