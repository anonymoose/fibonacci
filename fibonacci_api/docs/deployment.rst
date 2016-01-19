Deployment
=========================================

Docker Compose
------------------------

Steps required to configure a launch a Docker container running Fibonacci API, proxied by Nginx.

All instructions below assume successful installation of Docker consistent with your environment.

Create a docker machine.  Everything runs on here.
NOTE:  The default memory size will result in out-of-space errors.  Increase to 4096 for best results.

.. code:: console

          $ docker-machine create -d virtualbox --virtualbox-memory "4096" fibonacci

Set your shell to interact with the machine you just created.  The following injects relevant enviornment variables to your shell session.

.. code:: console

          $ eval "$(docker-machine env fibonacci)"


Combine everything described in $DEV_HOME docker-compose.yml into a running environment.

.. code:: console

          $ docker-compose build


Final launch and viewing logs.

.. code:: console

          $ docker-compose up -d
          $ docker-compose logs


Determine the IP address for this instance.

.. code:: console

          $ export DOCK_IP=$(docker-machine ip fibonacci)
          $ echo $DOCK_IP

Curl to see some results from your dockerized service.
NOTE:  Nginx is expoed on port 80

.. code:: console

          $ curl http://$DOCK_IP/fibonacci/list?count=10
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


Production Deployment
-------------------------------

Since this is docker, you can use any reference on the net to deploy to your production environment (AWS, bare metal, etc).
