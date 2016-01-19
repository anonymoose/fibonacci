API
=========================================

The Fibonacci API is a REST api with one call.  All data is returned in JSON format.


/fibonacci/list
------------------------

Purpose: Return a list containing the requested count of Fibonacci numbers.

Method:  GET

Inputs:  count - GET query parameter that must be a positive integer.

Success Outputs: JSON formatted hashmap containing a list of numbers under the "answer" key.  This list is returned in increasing order per the Fibonacci Sequence.

Example Success Output:

Default call:

.. code:: console

          $ curl http://localhost:5000/fibonacci/api?count=10
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

Api Traced Call

.. code:: console

          $ curl -H "Apitrace: 124asdfq23" http://localhost:5000/fibonacci/api?count=10
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

This logging header key is logged to provide tracability across multiple microservices and is not required.

Errors:

All errors are returned in JSON format, with the "error" key containing the string describing the error.

- ERR_NO_ARG - Count argument was not present.  Returns a HTTP 403 error in its status code.
- ERR_INVALID_TYPE - Count argument was present, but not in parsable into a long.  Returns a HTTP 403 error in its status code.
- ERR_OUT_OF_BOUNDS - Count argument was present, but not greater than or equal to zero. Returns a HTTP 403 error in its status code.
- All other errors return HTTP 500 with the message from the exception.

Example Error Output:

.. code:: console

           $ curl http://192.168.99.100/fibonacci/api?count=BOGUS
            {
              "error": "ERR_INVALID_TYPE:  'count' parameter must be an integer"
            }
