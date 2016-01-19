from fibonacci import fibonacci_calc
from nose.tools import ok_, eq_
from flask import json
import main

test_app = main.app.test_client()

def check_fibonacci_calc_output_ok(expected_array):
    """
    function:  check_fibonacci_calc_output_ok

    notes:     take some of the boilerplate out of testing fibonacci number calculations.
                see test_fibonacci_calc() for examples
    """
    l = len(expected_array)
    out = fibonacci_calc(l)
    eq_(len(out), l, "Should be array of length %s" % l)
    eq_(out, expected_array, "Should be array %s" % l)


def test_fibonacci_calc():
    """
    function:  test_fibonacci_calc

    notes:     Test all branches of the fibonacci_calc method
    """
    check_fibonacci_calc_output_ok([0])
    check_fibonacci_calc_output_ok([0,1])
    check_fibonacci_calc_output_ok([0,1,1])
    check_fibonacci_calc_output_ok([0,1,1,2])
    check_fibonacci_calc_output_ok([0,1,1,2,3])
    check_fibonacci_calc_output_ok([0,1,1,2,3,5])


def test_fibonacci_calc_negative():
    """
    function:  test_fibonacci_calc_negative

    notes:     ensure that all assertions behave as expected.
    """
    try:
        fibonacci_calc(-1)
        ok_(False, "fibonacci_calc(-1) should fail.")
    except: pass

    try:
        fibonacci_calc("A")
        ok_(False, "fibonacci_calc('A') should fail.")
    except: pass


STATUS_OK = 200
STATUS_REDIR = 302
STATUS_CLIENT_ERROR = 403

def check_fibonacci_api_output_ok(test_app, expected_array):
    """
    function:  check_fibonacci_api_output_ok

    notes:     take some of the boilerplate out of testing fibonacci number calculations through the API.
                see test_fibonacci_api() for examples
    """
    l = len(expected_array)
    resp = test_app.get('/fibonacci/list?count=%d' % l)
    out = json.loads(resp.data)
    eq_(resp.status_code, STATUS_OK, "Response code != %s" % STATUS_OK)
    eq_(out[u'answer'], expected_array, "/fibonacci/list returning wrong answer. Should be: %s" % expected_array)


def test_fibonacci_docs():
    """
    function:  test_fibonacci_docs
    notes:     Ensure that /fibonacci/docs redirects to the right place
    """
    resp = test_app.get('/fibonacci/docs')
    eq_(resp.status_code, STATUS_REDIR, "Response code %s is not != %s for /fibonacci/docs redirection" % (resp.status_code, STATUS_REDIR))


def test_fibonacci_api():
    """
    function:  test_fibonacci_api

    notes:      Test the api calls through flask to ensure API calls interpret requirements.
    """
    check_fibonacci_api_output_ok(test_app, [0])
    check_fibonacci_api_output_ok(test_app, [0,1])
    check_fibonacci_api_output_ok(test_app, [0,1,1])
    check_fibonacci_api_output_ok(test_app, [0,1,1,2])
    check_fibonacci_api_output_ok(test_app, [0,1,1,2,3])
    check_fibonacci_api_output_ok(test_app, [0,1,1,2,3,5])


def test_fibonacci_api_negative():
    """
    function:  test_fibonacci_api_negative

    notes:     Make sure that all assertions and validations complain like they should.
    """

    # test with no argument, both ways
    resp = test_app.get('/fibonacci/list?count=')
    out = json.loads(resp.data)
    eq_(resp.status_code, STATUS_CLIENT_ERROR, "Response is %s, should be %s" % (resp.status_code, STATUS_CLIENT_ERROR))
    ok_('ERR_NO_ARG' in out['error'], "Response should contain ERR_NO_ARG error message")

    resp = test_app.get('/fibonacci/list')
    out = json.loads(resp.data)
    eq_(resp.status_code, STATUS_CLIENT_ERROR, "Response is %s, should be %s" % (resp.status_code, STATUS_CLIENT_ERROR))
    ok_('ERR_NO_ARG' in out['error'], "Response should contain ERR_NO_ARG error message")

    # test with invalid parameter type.
    resp = test_app.get('/fibonacci/list?count=J')
    out = json.loads(resp.data)
    eq_(resp.status_code, STATUS_CLIENT_ERROR, "Response is %s, should be %s" % (resp.status_code, STATUS_CLIENT_ERROR))
    ok_('ERR_INVALID_TYPE' in out['error'], "Response should contain ERR_INVALID_TYPE error message")

    # test with negative number input
    resp = test_app.get('/fibonacci/list?count=-1')
    out = json.loads(resp.data)
    eq_(resp.status_code, STATUS_CLIENT_ERROR, "Response is %s, should be %s" % (resp.status_code, STATUS_CLIENT_ERROR))
    ok_('ERR_OUT_OF_BOUNDS' in out['error'], "Response should contain ERR_OUT_OF_BOUNDS error message")
