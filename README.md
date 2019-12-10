[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3a1190860c704585a6ed5cf78432bab1)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=benson40111/nlp_project&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.com/benson40111/nlp_project.svg?token=QFfTxqy7R93Bb7djst3q&branch=master)](https://travis-ci.com/benson40111/nlp_project)
## Introduction
It's a Undergraduate independent study project.
Get text from server then process that.
You can ask weather, yuntech course and easy calculate.
If you ask other questions, system will response a google search link to you.

## Based on
+  [Python](https://www.python.org/)
+  [Dialogflow](https://dialogflow.com/)
+  [pipenv](https://github.com/pypa/pipenv)

## Plugins
+  [flask](https://github.com/pallets/flask)
+  [ChatterBot](https://github.com/gunthercox/ChatterBot)
+  [mongoengine](https://github.com/MongoEngine/mongoengine)
+  [pytest](https://github.com/pytest-dev/pytest/)
+  [flask-paginate](https://github.com/lixxu/flask-paginate)

## How to use
First time we need install plugins in pipenv.
```
$ pipenv install
```
Running and test project in pipenv.
```
$ pipenv run python run.py
```
Go to your localhost 8080 port to see demo.

Now you can try something speech in url like:

your_localhost/get?speech=一加上一等於多少

or this

your_localhost/get?speech=資工系大三選修有哪些

and you will get a json file, that is the result.

## Thanks
[Weather API](https://works.ioa.tw/weather/api/doc/index.html)<br>
Thanks this great weather api that help me done my graduation project

