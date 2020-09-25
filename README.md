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

Clone the project into whatever directory you typically keep your code or repos. 
For example, a folder in home named `repos`. Note that you must have git installed,
so if you do not please search on installing git for version control or perhaps using
git-bash if you're running on windows. I highly recommend configuring git to use SSH
and Github has easy steps to aid you in getting your ssh key generated as well as placing
the right parts in the github settings page. 

First, we will change directories and go into the directory where we want to clone the project,
in this case thats the example folder named `repos`. Therefore, 
```bash
$ cd ~/repos
$ git clone git@github.com:AndrewJHart/landons-app.git
```

Use your terminal to CD into your the root of your project code. For example
our project is located in `~/repos/landons-app` and since we should already be
inside the repos direclty, we should be able to simply change directories to the
project name and enter that folder like so:
```bash
$ cd landons-app
```
> note, if for some reason you have issues getting into the directory, try the full path.
> note also that the `~` tilde key in terminal represents home. Thus, if the previous step
> failed for you, try this:
```bash
$ cd ~/repos/landons-app
```

Now, if you want rename the app to your own, simply change the folder from landons-app to
whatever.

Next, if you already have python 3.x.x on your system then by all means please feel free to skip
the next 2 steps and go down to the part of the document where we create the python3 virtual environment.
Otherwise, please take heed and read these bits.

Next make sure you're running python3 and not the default install (on OSx anyway of 2.7) by
typing 
```bash
$ python --version
```

If the output is less than version 3, you need to install python 3. There is a fantastic tool
called `homebrew` that will easily install the latest version, or whatever version you want, of
python for you. Here is a guide on how to run both python 2 (which OSx requires) and python 3, so
that you can use python 3 development and forget about python 2. Go [here](https://opensource.com/article/19/5/python-3-default-mac)
to learn how to install homebrew, and the latest version of python. In the end you should be able
to run the command 

```bash
$ python3 --version
```
and see the output you are expecting, e.g. 3.7.4 - just take caution to ensure you're including the
number 3 after python when running code or building virtual environments or you may unwittingly cause 
your code to fail to run.

Assuming that you are successfully running the latest version of python 3, follow the next step.

Now we need to create a virtual environment. Why? Because unfortunately the python package manager
`pip` installs all packages globally and this can cause a huge mess when you have multiple python apps
depending on different versions of dependencies. You can look more into virtual env's later but for now 
lets create a python 3 virtual environment: 
```bash
$ python -m venv venv
```
This will create a folder in your project directory named `venv` that will
hold all the python package dependencies needed to run your project, without
affecting any other projects. Essentially, you can now activate your virtualenv and
all the dependencies you need to run your python project, will be stored in this local
folder `venv` so as not to affect global python packages or versions.

---

Next you need to activate the virtual environment to ensure your python
dependencies are being installed only into the venv folder within the 
project directory. To activate the virtual environment run one of these
two commands based on your operating system.

**For Mac/OSx or Linux**
```bash
$ . venv/bin/activate
```

**For Windows**
```bash
$ venv/Scripts/activate.bat
```

Now you have activated your virtual environment and it should show by prefacing 
your terminal prompt with the word `(venv)` in parenthesis!! Now, lets finally install 
all of our required dependencies that are used for this project e.g. third party dependencies 
that are not built in with python. All of these dependencies are stored in a file at the
root of the project called `requirements.txt`. You can pass the `-r` flag to pip to tell
it look inside this file and install the required dependencies into your local virtual environment.

To install all the required dependencies run the following command, calling pip install:
```bash
(venv)$ pip install -r requirements.txt
```

If everything works without any error messages then you have successfully
installed the required libraries needed to run your script. Tada :)

## Running the code

All thats left to do now is run the script :D - you can do this by
executing this command in the terminal

```bash
(venv)$ python3 truth_game.py
```

If you see some questions popup on your terminal, answer them and then the game will begin!
Then you have succeeded in running this python script (and most other python projects work
similarly so you've gained some knowledge on how to manage python dependencies as well)

 
## Some info about the questions/clues API and its creator 

The RESTful API used for the questions, category, and answer data came from 
[jservice.io/](https://jservice.io/) and has been a great help in 
teaching my son about RESTful web services, how to fetch data from such services,
as well as manipulating `Lists` and `Dictionaries` and transforming JSON response data 
into the these actual python data structures that can be manipulated. Much thanks to 
[https://github.com/sottenad/jService](sottenad) for his github project! 

## Contributors

Author of documentation: Andrew Hart 
Author of python code: Landon Hart

## Version Log
We didn't get to semver yet so... 
