Fibonacci API
=============================

Example project to implement a Fibonacci API microservice.


Getting Started
-------------------------
Simple instructions to get set up in development environment are provided [here](https://github.com/anonymoose/fibonacci/blob/master/fibonacci_api/docs/development.rst)


Deployment
-------------------------
The API is Docker-capable.  Full instructions for getting started are [here](https://github.com/anonymoose/fibonacci/blob/master/fibonacci_api/docs/deployment.rst)


Documentation
-------------------------
Documentation root for the project is provided [here](https://github.com/anonymoose/fibonacci/tree/master/fibonacci_api/docs)

To build the docs into html:

```
$ cd fibonacci_api/docs
$ make html
```

Documentation appears in $DEV_HOME/fibonacci_api/static/index.html


Testing
-------------------------------
Run the tests with nosetests
```
$ cd $DEV_HOME/fibonacci_api
$ nosetests --with-coverage --cover-html --cover-package=fibonacci_api --cover-erase
.....

Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
fibonacci_api.py                 0      0   100%   
fibonacci_api/common.py         16      2    88%   37-38
fibonacci_api/fibonacci.py      13      0   100%   
fibonacci_api/main.py           31      4    87%   23, 53-54, 75
----------------------------------------------------------
TOTAL                           60      6    90%   
----------------------------------------------------------------------
Ran 5 tests in 0.027s

```


Quick Start for the impatient
------------------------------
```
$ git clone https://github.com/anonymoose/fibonacci.git
$ cd fibonacci/fibonacci_api
$ virtualenv --no-site-packages python
$ source python/bin/activate               # ensure you are using the correct virtualenv python
$ pip install -r requirements.txt
$ python main.py
```

Use curl to interact with the API.

```
$ curl http://localhost:5000/fibonacci/list?count=10
{
  "answer": [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34
  ]
}
```        

Technology Stack / Dependencies
-------------------------------
- Python 2.7  - All components are build in Python
- Nginx       - HTTP Proxy to sitting in front of the Python Service
- Flask       - Web application framework suitable for creating microservices in Python.
- Gunicorn    - Pre-fork application server to efficiently serve the Flask application in production.
- Docker      - Container technology to create simple and consistent deployments.
- Nose        - Unit testing framework.
- Sphinx      - Documentation generator
