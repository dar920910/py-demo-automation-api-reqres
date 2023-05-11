""" output.py: This module contains functions for output of info about test execution. """

def print_fake_testcase_details(testcase, fake_request_title, fake_request_url, fake_obj):
    print("\nINFO: Fake test is created to demonstrate scaling test automation project.\n")
    print("TEST CASE EXECUTION: {0}\n", format(testcase))
    print("FAKE REQUEST: {0}\n".format(fake_request_title))
    print("FAKE URL: {0}\n".format(fake_request_url))
    print("FAKE OBJECT: {0}\n".format(fake_obj))
