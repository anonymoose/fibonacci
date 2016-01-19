Introduction
=========================================



The Fibonacci API is an example project to show good practice in API design and microservice construction.

The system uses Flask to create a python 2.7 based microservice suitable for deployment to production via Docker.  In production, the system runs on a Gunicorn server proxied
by a Nginx webserver.  All of this is wrapped in a docker container using Docker Compose.

Features
----------------
- Dockerized deployment
- Scalabililty via Gunicorn's pre-fork server.
- Optional tokenized logging for transaction tracability.
- Iterative, intuitive algorithm in lieu of recurion for efficiency.

TODO
-----------------
- Caching with Redis/Memcached/Elasticache
- Redirect logging to centralized syslog collector.
- Centralized Authentication
