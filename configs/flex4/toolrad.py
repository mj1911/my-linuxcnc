#!/bin/env python3
''' This file adds X and Y DRO values, plus and minus tool radius, to the UI.
Useful for manual milling; say you have an imperial machine, throw in an M6 mill-
end, and want to cut something accurately by hand.  Use (an imperial) caliper to
measure the mill-end, enter its diameter, and the X and Y positions are shown
along with +/- tool radius.  So it becomes easy to "see" where the edge of the
cutter is, without having to calculate anything by hand. '''
from functools import partial

my_toolrad_enabled = False	# state var to toggle button
my_timer_enabled = False	# flag for only hooking timer once

def startup(parent):
	''' the startup code, which links a Flex GUI action to a function here '''
	parent.my_tool_rad_pb.clicked.connect(partial(my_toolrad_pb, parent))

def my_toolrad_pb(parent):
	''' handles state changes to the pushbutton on/off '''
	global my_toolrad_enabled, my_timer_enabled
	if my_toolrad_enabled:
		my_toolrad_enabled = False
		parent.my_tool_rad_pb.setText('Enable')
		# faults: TypeError: 'functools.partial' object is not connected, etc.
		# tried many variants, could not find a way to disable this timer
		#parent.var_watch_timer.timeout.disconnect(partial(my_toolrad, parent))
		# since we cannot disable a timer elegantly, just skip over toolrad()
	else:
		my_toolrad_enabled = True	# this toggles
		parent.my_tool_rad_pb.setText('Disable')
		if not my_timer_enabled: 	# hook our function (once) to a 0.1s timer
			parent.var_watch_timer.timeout.connect(partial(my_toolrad, parent))
			my_timer_enabled = True		# latch this true
	return

def my_toolrad(parent):
	''' reads current DRO value, calculates +/- tool diameter '''
	global my_toolrad_enabled
	if my_toolrad_enabled:
		# get diameter from widget (which gets it from .var file)
		dia = parent.doubleSpinBox_tool_dia.value()
		rad = dia / 2.0
		# get the actual X and Y DRO values as floats
		x2 = float(parent.dro_lb_x.text())
		y2 = float(parent.dro_lb_y.text())
		x2p = x2 + rad
		x2n = x2 - rad
		y2p = y2 + rad
		y2n = y2 - rad
		# these are additional controls to display the +/- values
		parent.dro_lb_x2.setText(parent.dro_lb_x.text())
		parent.dro_lb_x2p.setText(f'{x2p:.4f}')
		parent.dro_lb_x2n.setText(f'{x2n:.4f}')
		parent.dro_lb_y2.setText(parent.dro_lb_y.text())
		parent.dro_lb_y2p.setText(f'{y2p:.4f}')
		parent.dro_lb_y2n.setText(f'{y2n:.4f}')
		parent.dro_lb_z2.setText(parent.dro_lb_z.text())
	return
