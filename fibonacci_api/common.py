from flask import jsonify

def notify_error(msg, status_code):
    """
    function:  notify_error

    params:    msg - message to send back to the client.
               status_code - http status code to send to the client.

    returns:   flask response object suitable for return to the client.  Will have an "error" key with the message from our caller.

    notes:     Common status codes for client side problems:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error
               Common status codes for server side problems:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error

    examples:

    if 'count' not in request.args:
        return notify_error("'count' argument required to /fibonacci/api", 403)

    """
    resp = jsonify(error=str(msg))
    resp.status_code = status_code
    return resp
