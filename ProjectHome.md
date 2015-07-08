![http://www.pomodoroworld.com/_export/i-use-the-pomodoro.png](http://www.pomodoroworld.com/_export/i-use-the-pomodoro.png)


# Description #

Software timer to deal with the Pomodoro Technique.

(quote):

The Pomodoro Technique™ is a way to get the most out of time management. Turn time into a valuable ally to accomplish what we want to do and chart continuous improvement in the way we do it.

Francesco Cirillo created the Pomodoro Technique™ in 1992. It is now practiced by professional teams and individuals around the world.

# Requirements #

  1. python 2.5.`*` or higher.
  1. wxpython http://wxpython.org/
  1. if you are going to install version 2.0 or higher you also need Python client library for Google data APIs 2.0.6 http://pypi.python.org/pypi/gdata/2.0.6

# Installing pyPomodoro #

Download the latest stable version of pyPomodoro:
```
$ wget http://pypomodoro.googlecode.com/files/pyPomodoro2.4.tgz
$ tar -xvzf pyPomodoro2.4.tgz 
$ chmod +x run.py
$ python run.py
```


# Screenshot #

> ![![](http://pypomodoro.googlecode.com/files/Screenshot.gif)](http://pypomodoro.googlecode.com/files/Screenshot.gif)

# Configurations #

The only two configurations you can change are the time frame
and the csv file separator

all these values are in conf/settings.py file.

```
MAX_TIME=25

CSV_SEPARATOR=','

file archive used to store the counter: number of pomodoro completed since pyPomodoro was installed.

COUNTER_FILE_NAME='.pyPomodoro'

this is new in release 2.0: type your google calendar account whether you don't want to
type it every time in the login dialog.

google_calendar_account=''



```

Moreover, you can change all the GUI massages, labels and title: they are placed in conf/messages.py file.

# Contribute #

Issues report, requirements and idea are welcome.

Please, contact me.

![http://static03.linkedin.com/img/logos/logo_linkedin_88x22.png](http://static03.linkedin.com/img/logos/logo_linkedin_88x22.png) http://it.linkedin.com/in/wtraspad



