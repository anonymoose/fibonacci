Fibonacci API
=============================

Example project to implement a Fibonacci API microservice.


Documentation
-------------------------
Documentation root for the project is provided [here](https://github.com/anonymoose/fibonacci/tree/master/fibonacci_api/docs)


Getting Started
-------------------------
Simple instructions to get set up in development environment are provided [here](https://github.com/anonymoose/fibonacci/blob/master/fibonacci_api/docs/development.rst)


Deployment
-------------------------
The API is Docker-capable.  Full instructions for getting started are [here](https://github.com/anonymoose/fibonacci/blob/master/fibonacci_api/docs/deployment.rst)


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

