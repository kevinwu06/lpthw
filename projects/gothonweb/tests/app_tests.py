from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    
    # test our first GET request to /hello
    resp = app.request("/you_died")
    assert_response(resp)
    
    # make sure the default values work for the form
    resp = app.request("/show_room", method="POST")
    assert_response(resp, contains="Play Agains?")
    
    # test that we get expected values
    # data = {'name' : 'central_corridor', 'description' : """
            # The Gothons of Planet Percal #25 have invaded your ship and destroyed
            # your entire crew.  You are the last surviving member and your last
            # mission is to get the neutron destruct bomb from the Weapons Armory,
            # put it in the bridge, and blow the ship up after getting into an 
            # escape pod.

            # You're running down the central corridor to the Weapons Armory when
            # a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
            # flowing around his hate filled body.  He's blocking the door to the
            # Armory and about to pull a weapon to blast you.
            # """}
    # resp = app.request("/show_room", method="POST", data=data)
    # assert_response(resp, contains="Zed")