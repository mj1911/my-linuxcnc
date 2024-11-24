#!/bin/env python3
from functools import partial

toolrad_enabled = False

def startup(parent):
	parent.tool_rad_pb.clicked.connect(partial(toolrad_pb, parent))

def toolrad_pb(parent):
	global toolrad_enabled
	# create a toggle-able button for on/off
	if toolrad_enabled:
		# since cannot disable, skip this
		return
		toolrad_enabled = False
		parent.tool_rad_pb.setText('Enable')
		# faults: TypeError: 'functools.partial' object is not connected, etc.
		# tried many variants, could not find a way to disable this timer
		#parent.var_watch_timer.timeout.disconnect(partial(toolrad, parent))
	else:
		toolrad_enabled = True
		parent.tool_rad_pb.setText('Restart to Disable')
		toolrad(parent)
		# hook our function to a 0.1s timer
		parent.var_watch_timer.timeout.connect(partial(toolrad, parent))

def toolrad(parent):
	# get diameter from widget (which gets it from .var file)
	dia = parent.doubleSpinBox_tool_dia.value()
	rad = dia / 2.0
	x2 = float(parent.dro_lb_x.text())
	y2 = float(parent.dro_lb_y.text())
	x2p = x2 + rad
	x2n = x2 - rad
	y2p = y2 + rad
	y2n = y2 - rad
	parent.dro_lb_x2.setText(parent.dro_lb_x.text())
	parent.dro_lb_x2p.setText(f'{x2p:.4f}')
	parent.dro_lb_x2n.setText(f'{x2n:.4f}')
	parent.dro_lb_y2.setText(parent.dro_lb_y.text())
	parent.dro_lb_y2p.setText(f'{y2p:.4f}')
	parent.dro_lb_y2n.setText(f'{y2n:.4f}')
