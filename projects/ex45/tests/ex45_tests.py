from nose.tools import *
import ex45.game

def test_room():
	blade = BladeRoom()
	assert_equal(blade.name(), "blade_room")
	namerm = NameRoom()
	assert_equal(namerm.name(), "name_room")
	bridge = BridgeRoom()
	assert_equal(bridge.name(), "bridge_room")
	grail = GrailRoom()
	assert_equal(grail.name(), "grail_room")