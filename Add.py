##############################################################
# Add Attribute Tool
# Version: 1.00
# Author: Aashi Shukla
# --------------------------------------------------------------
# This tool  has all the features you need to add attributes  to
# your already existing Ctrls. This script provides you with the
# option of choosing  preset  attributes according to your  need.
# All options that don't work together are already disabled. 
# ---------------------------------------------------------------
# To run this  script, just  paste this file in your Maya Scripts
# Directory, open the Scrit Editor and paste the following bit of
# code:
# import Add
# reload(Add)
# Add.GUI()
# and Run!
# ---------------------------------------------------------------
# I hope you find this useful. 
# Kindly report bugs on: aashi4127@gmail.com
# ###############################################################

import maya.cmds as cmds
import functools

def GUI():
	if cmds.window('add_attr_UI', exists=True):
		cmds.deleteUI('add_attr_UI')
	Win = cmds.window('add_attr_UI', t='Add Attribute', bgc= (0.2, 0.2, 0.2), wh=(300,500), s=False, mnb=1, mxb=0)
	tabs = cmds.tabLayout(imh=5, imw=5)
	main_tab = cmds.formLayout(p= tabs)
	cmds.formLayout(main_tab, edit=True)
	help_tab = cmds.formLayout(p= tabs)
	cmds.formLayout(help_tab, edit=True)
	cmds.tabLayout(tabs, edit=True, tabLabel=((main_tab, "Main"), (help_tab,"Help")) )
	# main tab
	scroll_tab = cmds.scrollLayout(p=main_tab, w=300, h=500)
	main_col = cmds.columnLayout(adj= 1, p= scroll_tab)
	# add attributes frame
	add_attr_frame = cmds.frameLayout(l='Add Attributes',mh=5 , mw=5, cll=True, cl=True, bgc=(0.585,0.123,1), w=300, p= main_col)
	clm_01 = cmds.columnLayout(adj=1, p=add_attr_frame)
	#--------------------------------------------------
	add_limb_attr = cmds.frameLayout(l='Global Attributes', mh=3, mw=3, cl=True, cll=True,p=clm_01, bgc= (.45,.45,.45))
	cmds.rowColumnLayout(p = add_limb_attr, nc=2, cw=[(1, 130),(2,130)],co=([1, "both",10], [2,"both",10]) )
	global_attr_01 = cmds.checkBox(l= 'Global Scale')
	global_attr_02 = cmds.checkBox(l= 'Mesh Display')
	global_attr_03 = cmds.checkBox(l= 'Mesh Vis')
	global_attr_04 = cmds.checkBox(l= 'Ctrl Vis')
	global_attr_05 = cmds.checkBox(l= 'Jnt Vis')
	global_attr_06 = cmds.checkBox(l= 'Facial Vis')
	global_all = cmds.checkBox(l= 'All')
	cmds.button(l='Add Attributes', bgc=(.45,.45,.45), w=150, c=lambda x:Add_Global_Attr(global_attr_01,global_attr_02,global_attr_03,global_attr_04,global_attr_05,global_attr_06,global_all))
	# enable all checkboxes with All checkbox
	cmds.checkBox(global_all, e=1, onc= functools.partial(all_global_sel, global_attr_01, global_attr_02, global_attr_03, global_attr_04, global_attr_05, global_attr_06, True))
	cmds.checkBox(global_all, e=1, ofc= functools.partial(all_global_sel, global_attr_01, global_attr_02, global_attr_03, global_attr_04, global_attr_05, global_attr_06,False))
	#--------------------------------------------------
	add_limb_attr = cmds.frameLayout(l='Limb Attributes', mh=3, mw=3, cl=True, cll=True,p=clm_01, bgc= (.45,.45,.45))
	cmds.rowColumnLayout(p = add_limb_attr, nc=2, cw=[(1, 130),(2,130)],co=([1, "both",10], [2,"both",10]) )
	limb_attr_01 = cmds.checkBox(l= 'FKIK')
	limb_attr_02 = cmds.checkBox(l= 'Curls')
	limb_attr_03 = cmds.checkBox(l= 'Scrunch')
	limb_attr_04 = cmds.checkBox(l= 'Splay')
	limb_attr_05 = cmds.checkBox(l= 'Relax')
	limb_attr_06 = cmds.checkBox(l= 'Point')
	limb_attr_07 = cmds.checkBox(l= 'Fist')
	limb_attr_08 = cmds.checkBox(l= 'Cup')
	limb_attr_09 = cmds.checkBox(l= 'Stretchy')
	limb_attr_10 = cmds.checkBox(l= 'Bendy Vis')
	limb_attr_11 = cmds.checkBox(l= 'Finger Vis')
	limb_attr_12 = cmds.checkBox(l= 'Length 01')
	limb_attr_13 = cmds.checkBox(l= 'Length 01 Vol')
	limb_attr_14 = cmds.checkBox(l= 'Length 02')
	limb_attr_15 = cmds.checkBox(l= 'Length 02 Vol')
	limb_attr_16 = cmds.checkBox(l= 'Sep Index Ctrls')
	limb_attr_17 = cmds.checkBox(l= 'Sep Middle Ctrls')
	limb_attr_18 = cmds.checkBox(l= 'Sep Ring Ctrls')
	limb_attr_19 = cmds.checkBox(l= 'Sep Pinky Ctrls')
	limb_attr_20 = cmds.checkBox(l= 'Sep Thumb Ctrls')
	limb_attr_all = cmds.checkBox(l= 'All')
	cmds.button(l='Add Attributes', bgc=(.45,.45,.45), w=150, c=lambda x:Add_Limb_Attr(limb_attr_01,limb_attr_02,limb_attr_03,limb_attr_04,limb_attr_05,limb_attr_06,limb_attr_07,limb_attr_08,limb_attr_09,limb_attr_10,limb_attr_11,limb_attr_12,limb_attr_13,limb_attr_14,limb_attr_15,limb_attr_16,limb_attr_17,limb_attr_18,limb_attr_19,limb_attr_20) )
	# enable all checkboxes with All checkbox
	cmds.checkBox(limb_attr_all, e=1, onc= functools.partial(all_limb_sel, limb_attr_01, limb_attr_02, limb_attr_03, limb_attr_04, limb_attr_05, limb_attr_06, limb_attr_07, limb_attr_08, limb_attr_09, limb_attr_10,limb_attr_11,limb_attr_12,limb_attr_13,limb_attr_14,limb_attr_15,limb_attr_16,limb_attr_17,limb_attr_18,limb_attr_19,limb_attr_20, True))
	cmds.checkBox(limb_attr_all, e=1, ofc= functools.partial(all_limb_sel, limb_attr_01, limb_attr_02, limb_attr_03, limb_attr_04, limb_attr_05, limb_attr_06, limb_attr_07, limb_attr_08, limb_attr_09, limb_attr_10,limb_attr_11,limb_attr_12,limb_attr_13,limb_attr_14,limb_attr_15,limb_attr_16,limb_attr_17,limb_attr_18,limb_attr_19,limb_attr_20, False))
	#--------------------------------------------------
	add_feet_attr = cmds.frameLayout(l='Feet Attributes', mh=3, mw=3, cl=True, cll=True,p=clm_01, bgc= (.45,.45,.45))
	cmds.rowColumnLayout(p = add_feet_attr, nc=2, cw=[(1, 130),(2,130)],co=([1, "both",10], [2,"both",10]) )
	feet_attr_01 = cmds.checkBox(l= 'FKIK')
	feet_attr_02 = cmds.checkBox(l= 'Length 01')
	feet_attr_03 = cmds.checkBox(l= 'Length 01 Vol')
	feet_attr_04 = cmds.checkBox(l= 'Length 02')
	feet_attr_05 = cmds.checkBox(l= 'Length 02 Vol')
	feet_attr_06 = cmds.checkBox(l= 'Stretchy')
	feet_attr_07 = cmds.checkBox(l= 'Bendy Vis')
	feet_attr_08 = cmds.checkBox(l= 'PV space')
	feet_attr_09 = cmds.checkBox(l= 'Twist')
	feet_attr_10 = cmds.checkBox(l= 'Soft IK')
	feet_attr_11 = cmds.checkBox(l= 'Foot Roll')
	feet_attr_12 = cmds.checkBox(l= 'Roll Angle')
	feet_attr_13 = cmds.checkBox(l= 'Heel Raise')
	feet_attr_14 = cmds.checkBox(l= 'Ball Raise')
	feet_attr_15 = cmds.checkBox(l= 'Toe Raise')
	feet_attr_16 = cmds.checkBox(l= 'Heel Slide')
	feet_attr_17 = cmds.checkBox(l= 'Ball Slide')
	feet_attr_18 = cmds.checkBox(l= 'Toe Slide')
	feet_attr_19 = cmds.checkBox(l= 'Rock')
	feet_attr_20 = cmds.checkBox(l= 'Banking')
	feet_attr_all = cmds.checkBox(l= 'All')
	cmds.button(l='Add Attributes', bgc=(.45,.45,.45), w=150, c=lambda x:Add_Feet_Attr(feet_attr_01, feet_attr_02, feet_attr_03, feet_attr_04, feet_attr_05, feet_attr_06, feet_attr_07, feet_attr_08, feet_attr_09, feet_attr_10, feet_attr_11, feet_attr_12, feet_attr_13, feet_attr_14, feet_attr_15, feet_attr_16, feet_attr_17, feet_attr_18, feet_attr_19, feet_attr_20) )
	# enable all checkboxes with All checkbox
	cmds.checkBox(feet_attr_all, e=1, onc= functools.partial(all_feet_sel, feet_attr_01, feet_attr_02, feet_attr_03, feet_attr_04, feet_attr_05, feet_attr_06, feet_attr_07, feet_attr_08, feet_attr_09, feet_attr_10, feet_attr_11, feet_attr_12, feet_attr_13, feet_attr_14, feet_attr_15, feet_attr_16, feet_attr_17, feet_attr_18, feet_attr_19, feet_attr_20,True))
	cmds.checkBox(feet_attr_all, e=1, ofc= functools.partial(all_feet_sel, feet_attr_01, feet_attr_02, feet_attr_03, feet_attr_04, feet_attr_05, feet_attr_06, feet_attr_07, feet_attr_08, feet_attr_09, feet_attr_10, feet_attr_11, feet_attr_12, feet_attr_13, feet_attr_14, feet_attr_15, feet_attr_16, feet_attr_17, feet_attr_18, feet_attr_19, feet_attr_20,False))
	#--------------------------------------------------
	add_space_switch = cmds.frameLayout(l='Space Switch Attributes', mh=3, mw=3, cl=True, cll=True,p=clm_01, bgc= (.45,.45,.45))
	cmds.rowColumnLayout(p = add_space_switch, nc=2, cw=[(1, 130),(2,130)],co=([1, "both",10], [2,"both",10]) )
	ss_attr_01 = cmds.checkBox(l= 'LOCAL')
	ss_attr_02 = cmds.checkBox(l= 'WORLD')
	ss_attr_03 = cmds.checkBox(l= 'COG')
	ss_attr_04 = cmds.checkBox(l= 'Head')
	ss_attr_05 = cmds.checkBox(l= 'All')
	cmds.button(l='Add Attributes', bgc=(.45,.45,.45), w=150, c=lambda x:Add_Space_Attr(ss_attr_01,ss_attr_02,ss_attr_03,ss_attr_04))
	# enable all checkboxes with All checkbox
	cmds.checkBox(ss_attr_05, e=1, onc = functools.partial(all_ss_sel, ss_attr_01, ss_attr_02, ss_attr_03, ss_attr_04, ss_attr_05, True))
	cmds.checkBox(ss_attr_05, e=1, ofc = functools.partial(all_ss_sel, ss_attr_01, ss_attr_02, ss_attr_03, ss_attr_04, ss_attr_05, False))
	#--------------------------------------------------
	add_custom_attr = cmds.frameLayout(l='Add Custom Attributes', mh=3, mw=3, cl=True, cll=True,p=clm_01, bgc= (.45,.45,.45))
	cmds.rowColumnLayout(p=add_custom_attr, nc=4, co=([1, "both",5], [2,"both",5], [3,"both",5], [4,"both",5]) )
	cmds.text(l='Data Type:')
	cmds.radioCollection(nci=3)
	add_integer = cmds.radioButton(l='Integer', select=True)
	add_float = cmds.radioButton(l='Float')
	add_boolean = cmds.radioButton(l='Boolean')
	
	cmds.rowColumnLayout(p=add_custom_attr, nc=2, co=([1, "both",15], [2,"both",15]), cw=[(1, 130),(2,130)] )
	Attribute = cmds.text(l= 'Attribute Name')
	Boolean = cmds.text(l= 'enum Name', enable=False)
	LongName = cmds.textField(w=120, editable=True)
	BooleanName = cmds.textField(w=120, text=' ### : ### : ### ',enable=False)
	
	cmds.rowColumnLayout(p=add_custom_attr, nc=3, co=([1, "both",10], [2,"both",10], [3,"both",10]) )
	min_txt = cmds.text(l='Min Value')
	max_txt = cmds.text(l='Max Value')
	def_txt = cmds.text(l='Default Value')
	min_val = cmds.floatField(w=70)
	max_val = cmds.floatField(w=70)
	def_val = cmds.floatField(w=70)
	cmds.columnLayout(p=add_custom_attr,adj=1, bgc=(.45,.45,.45) )
	cmds.button(l= 'Add', h=50, c=lambda x:Add_Custom_Attr(add_integer,add_float,add_boolean,LongName,BooleanName,min_val,max_val,def_val) )
	
	# disable boolean functions:
	cmds.radioButton(add_boolean, e=1, onc = functools.partial(enable_boolean_func, Attribute, LongName, Boolean, BooleanName, min_txt, max_txt, def_txt, min_val, max_val, def_val, True))
	cmds.radioButton(add_boolean, e=1, ofc = functools.partial(enable_boolean_func, Attribute, LongName, Boolean, BooleanName, min_txt, max_txt, def_txt, min_val, max_val, def_val,False))
	
	lock_and_hide_frame = cmds.frameLayout(l='Lock and Show Attributes', mh=5 , mw=5, cl=True, cll=True, bgc=(0.257,0,0.257),w=300, p= main_col)
	clm_02 = cmds.columnLayout(adj=1, p= lock_and_hide_frame)
	cmds.rowColumnLayout(p=clm_02, nc=5, co=([1,"both",5],[2,"both",5],[3,"both",5],[4,"both",5],[5,"both",5]), cw=[(1, 100),(2,30),(3,30),(4,30),(5,30)])
	cmds.separator(w=50,st='none')
	cmds.text(l='X  ')
	cmds.text(l='Y  ')
	cmds.text(l='Z  ')
	cmds.text(l='All  ')
	cmds.text(l='Translate : ')
	trans_X = cmds.checkBox(l= '')
	trans_Y = cmds.checkBox(l= '')
	trans_Z = cmds.checkBox(l= '')
	trans_All = cmds.checkBox(l= '')
	cmds.text(l='Rotate : ')
	rot_X = cmds.checkBox(l= '')
	rot_Y = cmds.checkBox(l= '')
	rot_Z = cmds.checkBox(l= '')
	rot_All = cmds.checkBox(l= '')
	cmds.text(l='Scale : ')
	scl_X = cmds.checkBox(l= '')
	scl_Y = cmds.checkBox(l= '')
	scl_Z = cmds.checkBox(l= '')
	scl_All = cmds.checkBox(l= '')
	cmds.text(l='Visibility:')
	vis = cmds.checkBox(l='')
	cmds.rowColumnLayout(p=clm_02, nc= 4, cw= [(1,100),(2,50),(3,50),(4,100)] )
	cmds.separator(w=100, st='none')
	cmds.radioCollection(nci=2)
	select_All = cmds.radioButton(l='All')
	select_None = cmds.radioButton(l='None', select=True)
	# trans all
	cmds.checkBox(trans_All, e=1, onc= functools.partial( sel_trans_all, trans_X,trans_Y,trans_Z, True) )
	cmds.checkBox(trans_All, e=1, ofc= functools.partial( sel_trans_all, trans_X,trans_Y,trans_Z,False) )
	# rot all
	cmds.checkBox(rot_All, e=1, onc= functools.partial( sel_rot_all, rot_X,rot_Y,rot_Z, True) )
	cmds.checkBox(rot_All, e=1, ofc= functools.partial( sel_rot_all, rot_X,rot_Y,rot_Z,False) )
	# scale all
	cmds.checkBox(scl_All, e=1, onc= functools.partial( sel_scl_all, scl_X, scl_Y, scl_Z, True) )
	cmds.checkBox(scl_All, e=1, ofc= functools.partial( sel_scl_all, scl_X, scl_Y, scl_Z,False) )
	# partial All Checkboxes
	cmds.radioButton(select_All, e=1, onc= functools.partial( radio_sel_all, trans_All,rot_All,scl_All,trans_X,trans_Y,trans_Z, rot_X,rot_Y,rot_Z, scl_X, scl_Y, scl_Z, vis, True) )
	cmds.radioButton(select_All, e=1, ofc= functools.partial( radio_sel_all, trans_All,rot_All,scl_All,trans_X,trans_Y,trans_Z, rot_X,rot_Y,rot_Z, scl_X, scl_Y, scl_Z, vis,False) )
	cmds.separator(w=100, st='none')
	cmds.rowColumnLayout(p=clm_02, nc=3, cw=[(1,90),(2,90),(3,90)] )
	cmds.button(l='lock', bgc=(.25, .25, .25), c=lambda x:Lock_attributes(trans_X, trans_Y, trans_Z, rot_X, rot_Y, rot_Z, scl_X, scl_Y, scl_Z, vis) )
	cmds.button(l='hide', bgc=(.25, .25, .25), c=lambda x:Hide_attributes(trans_X, trans_Y, trans_Z, rot_X, rot_Y, rot_Z, scl_X, scl_Y, scl_Z, vis) )
	cmds.button(l='show', bgc=(.25, .25, .25), c=lambda x:Show_attributes(trans_X, trans_Y, trans_Z, rot_X, rot_Y, rot_Z, scl_X, scl_Y, scl_Z, vis) )
	# help tab
	cmds.columnLayout(p= help_tab)
	help_text = 'Add Attribute Tool \n\nVersion: 1.00 \n\nAuthor: Aashi Shukla \n\n-----------------------------------------\n\n\nAn easy-to-use script for adding your custom attributes with a variety of presets to choose from and lock, hide and show options, without having to go through the entire channel box again and again. '
	cmds.scrollField( text = help_text, editable=False, wordWrap=True, w= 300, h=500,p= help_tab)
	cmds.showWindow()

if __name__== "__main__":
	GUI()














def Lock_attributes(trans_X, trans_Y, trans_Z, rot_X, rot_Y, rot_Z, scl_X, scl_Y, scl_Z, vis):
	list = cmds.ls(sl=True)
	i=0
	for obj in list:
		cmds.select(cl=True)
		cmds.select(list[i])
		print 'working on: ', list[i]
		if cmds.checkBox(trans_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateX', l=1)
		if cmds.checkBox(trans_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateY', l=1)
		if cmds.checkBox(trans_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateZ', l=1)
		if cmds.checkBox(rot_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateX', l=1)
		if cmds.checkBox(rot_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateY', l=1)
		if cmds.checkBox(rot_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateZ', l=1)
		if cmds.checkBox(scl_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleX', l=1)
		if cmds.checkBox(scl_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleY', l=1)
		if cmds.checkBox(scl_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleZ', l=1)
		if cmds.checkBox(vis, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.visibility', l=1)
		i+=1

def Hide_attributes(trans_X, trans_Y, trans_Z, rot_X, rot_Y, rot_Z, scl_X, scl_Y, scl_Z, vis):
	list = cmds.ls(sl=True)
	i=0
	for obj in list:
		cmds.select(cl=True)
		cmds.select(list[i])
		print 'working on: ', list[i]
		if cmds.checkBox(trans_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateX', cb=0, k=0)
		if cmds.checkBox(trans_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateY', cb=0, k=0)
		if cmds.checkBox(trans_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateZ',cb=0, k=0)
		if cmds.checkBox(rot_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateX', cb=0, k=0)
		if cmds.checkBox(rot_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateY', cb=0, k=0)
		if cmds.checkBox(rot_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateZ',cb=0, k=0)
		if cmds.checkBox(scl_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleX', cb=0, k=0)
		if cmds.checkBox(scl_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleY',cb=0, k=0)
		if cmds.checkBox(scl_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleZ', cb=0, k=0)
		if cmds.checkBox(vis, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.visibility', cb=0, k=0)
		i+=1

def Show_attributes(trans_X, trans_Y, trans_Z, rot_X, rot_Y, rot_Z, scl_X, scl_Y, scl_Z, vis):
	list = cmds.ls(sl=True)
	i=0
	for obj in list:
		cmds.select(cl=True)
		cmds.select(list[i])
		print 'working on: ', list[i]
		if cmds.checkBox(trans_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateX', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.translateX', k=1)
		if cmds.checkBox(trans_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateY', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.translateY', k=1)
		if cmds.checkBox(trans_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.translateZ', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.translateZ', k=1)
		if cmds.checkBox(rot_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateX', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.rotateX', k=1)
		if cmds.checkBox(rot_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateY', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.rotateY', k=1)
		if cmds.checkBox(rot_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.rotateZ', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.rotateZ', k=1)
		if cmds.checkBox(scl_X, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleX', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.scaleX', k=1)
		if cmds.checkBox(scl_Y, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleY', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.scaleY', k=1)
		if cmds.checkBox(scl_Z, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.scaleZ', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.scaleZ', k=1)
		if cmds.checkBox(vis, query=True, value=True):
			cmds.setAttr( str(list[i]) + '.visibility', cb=1, k=0, l=0)
			cmds.setAttr( str(list[i]) + '.visibility', k=1)
		i+=1
	
def Add_Custom_Attr(add_integer,add_float,add_boolean,LongName,BooleanName,min_val,max_val,def_val):
	name = cmds.textField(LongName, query=True, text=True)
	Min = cmds.floatField(min_val, q=1, v=1)
	Max = cmds.floatField(max_val, q=1, v=1)
	default = cmds.floatField(def_val, q=1, v=1)
	enum_names = cmds.textField(BooleanName, q=1, text=True)
	i=0
	j=0
	k=0
	if cmds.radioButton(add_integer, query=True, select=True):
		list = cmds.ls(sl=True)
		for obj in list:
			cmds.addAttr(ln= name, at='float', min = Min, max = Max, dv = default, k=1)
			i+=1
	if cmds.radioButton(add_float, query=True, select=True):
		fl_list = cmds.ls(sl=True)
		for obj in fl_list:
			cmds.addAttr(ln= name, at='float', min = Min, max = Max, dv = default, k=1)
			j+=1
	if cmds.radioButton(add_boolean, query=True, select=True):
		bl_list = cmds.ls(sl=True)
		for obj in bl_list:
			cmds.addAttr(ln= name, at='enum', en = str(enum_names), k=1)
			k+=1


def Add_Global_Attr(global_attr_01,global_attr_02,global_attr_03,global_attr_04,global_attr_05,global_attr_06,global_all):
	i=0
	list = cmds.ls(sl=True)
	print list
	for obj in enumerate(list):
		print str(list[i])
		cmds.select(cl=True)
		cmds.select(list[i])
		if cmds.checkBox(global_attr_01, query=True, value=True):
			cmds.addAttr(ln= 'Global_Scale', at='float', dv=1, min=0.1, max=10, k=1)
			cmds.setAttr(str(list[i]) + '.Global_Scale', cb=1, k=0)
		
		if cmds.checkBox(global_attr_02, query=True, value=True):
			cmds.addAttr(ln= 'Mesh_Display', at='enum', enumName = "normal:template:reference",k=1)
			cmds.setAttr(str(list[i]) + '.Mesh_Display', cb=1, k=0)
			
		if cmds.checkBox(global_attr_03, query=True, value=True):
			cmds.addAttr(ln = 'Mesh_Vis', at='float', dv=0, min=0, max=1, k=1)
			cmds.setAttr(str(list[i]) + '.Mesh_Vis', cb=1, k=0)
			
		if cmds.checkBox(global_attr_04, query=True, value=True):
			cmds.addAttr(ln = 'Ctrl_Vis', at='float', dv=0, min=0, max=1, k=1)
			cmds.setAttr(str(list[i]) + '.Ctrl_Vis', cb=1, k=0)
			
		if cmds.checkBox(global_attr_05, query=True, value=True):
			cmds.addAttr(ln = 'Jnt_Vis', at='float', dv=0, min=0, max=1, k=1)
			cmds.setAttr(str(list[i]) + '.Jnt_Vis', cb=1, k=0)
			
		if cmds.checkBox(global_attr_06, query=True, value=True):
			cmds.addAttr(ln = 'Facial_Vis', at='float', dv=0, min=0, max=1, k=1)
			cmds.setAttr(str(list[i]) + '.Facial_Vis', cb=1, k=0)
		i+=1
		
def Add_Limb_Attr(limb_attr_01,limb_attr_02,limb_attr_03,limb_attr_04,limb_attr_05,limb_attr_06,limb_attr_07,limb_attr_08,limb_attr_09,limb_attr_10,limb_attr_11,limb_attr_12,limb_attr_13,limb_attr_14,limb_attr_15,limb_attr_16,limb_attr_17,limb_attr_18,limb_attr_19,limb_attr_20):
	i=0
	limb_list = cmds.ls(sl=True)
	print limb_list
	for obj in limb_list:
		print 'adding to:', str(limb_list[i]) 
		cmds.select(cl=True)
		cmds.select(limb_list[i])
		if cmds.checkBox( limb_attr_01, query=True, value=True):
			cmds.addAttr(ln='fkik', nn='---', at= 'enum', en = '---', k=1)
			cmds.setAttr(str(limb_list[i]) + '.fkik', cb=1, k=0, l=1)
			cmds.addAttr(ln= 'FKIK', at= 'float', dv=0, min=0, max=10, k=1)
			print('FKIK attr added')
		if cmds.checkBox( limb_attr_02, query=True, value=True):
			cmds.addAttr(ln='curls', nn='---',at='enum', enumName = 'Curls', k=1)
			cmds.setAttr(str(limb_list[i]) + '.curls', cb=1, k=0, l=1)
			cmds.addAttr(ln='Index_Curl', at='float', dv=0, min= -10, max= 10, k=1)
			cmds.addAttr(ln='Middle_Curl', at='float', dv=0, min= -10, max= 10, k=1)
			cmds.addAttr(ln='Ring_Curl', at='float', dv=0, min= -10, max= 10, k=1)
			cmds.addAttr(ln='Pinky_Curl', at='float', dv=0, min= -10, max= 10, k=1)
			cmds.addAttr(ln='Thumb_Curl', at='float', dv=0, min= -10, max= 10, k=1)
			print('curls attr added')
		if cmds.checkBox(limb_attr_03, query=True, value=True):
			cmds.addAttr(ln='Scrunch', at='float', min= -10, dv = 0, max= 10, k=1)
			print('scrunch attr added')
		if cmds.checkBox(limb_attr_04, query=True, value=True):
			cmds.addAttr(ln='Splay', at='float', min= -10, dv= 0, max= 10, k=1)
			print('splay attr added')
		if cmds.checkBox(limb_attr_05, query=True, value=True):
			cmds.addAttr(ln='Relax', at='float', min= -10, dv= 0, max= 10, k=1)
			print('relax attr added')
		if cmds.checkBox(limb_attr_06, query=True, value=True):
			cmds.addAttr(ln='Point', at='float', min= 0, dv= 0, max= 10, k=1)
			print('point attr added')
		if cmds.checkBox(limb_attr_07, query=True, value=True):
			cmds.addAttr(ln='Fist', at='float', min= 0, dv= 0, max= 10, k=1)
			print('fist attr added')
		if cmds.checkBox(limb_attr_08, query=True, value=True):
			cmds.addAttr(ln='Cup', at='float', min= 0, dv= 0, max= 10, k=1)
			print('cup attr added')
		if cmds.checkBox(limb_attr_09, query=True, value=True):
			cmds.addAttr(ln='Stretchy', at='float', min= 0, dv= 0, max= 10, k=1)
			print('stretchy attr added')
		if cmds.checkBox(limb_attr_10, query=True, value=True):
			cmds.addAttr(ln='Bendy_Vis', at='float', min= 0, dv= 0, max= 1, k=1)
			print('bendy attr added')
		if cmds.checkBox(limb_attr_11, query=True, value=True):
			cmds.addAttr(ln='Finger_Vis', at='float', min= 0, dv= 0, max= 1, k=1)
			print('finger attr added')
		if cmds.checkBox(limb_attr_12, query=True, value=True):
			cmds.addAttr(ln= 'Length_01', dv=0, min= -10, max= 10, k=1)
			print('length 01 attr added')
		if cmds.checkBox(limb_attr_13, query=True, value=True):
			cmds.addAttr(ln= 'Length_01_Vol', dv=0, min= -10, max= 10, k=1)
			print('length 01 Vol attr added')
		if cmds.checkBox(limb_attr_14, query=True, value=True):
			cmds.addAttr(ln= 'Length_02', dv=0, min= -10, max= 10, k=1)
			print('length 02 attr added')
		if cmds.checkBox(limb_attr_15, query=True, value=True):
			cmds.addAttr(ln= 'Length_02_Vol', dv=0, min= -10, max= 10, k=1)
			print('length 02 Vol attr added')
		if cmds.checkBox(limb_attr_16, query=True, value=True):
			cmds.addAttr(ln= 'INDEX', at= 'enum', en='---', k=1)
			cmds.setAttr(str(limb_list[i]) + '.INDEX', k=0, cb=1, l=1)
			cmds.addAttr(ln= 'Index_01', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Index_02', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Index_03', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Index_04', at='float', min= -10, max= 10, dv= 0, k=1)
			print('sep index attr added')
		if cmds.checkBox(limb_attr_17, query=True, value=True):
			cmds.addAttr(ln= 'MIDDLE', at= 'enum', en='---', k=1)
			cmds.setAttr(str(limb_list[i]) + '.MIDDLE', k=0, cb=1, l=1)
			cmds.addAttr(ln= 'Middle_01', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Middle_02', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Middle_03', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Middle_04', at='float', min= -10, max= 10, dv= 0, k=1)
			print('sep middle attr added')
		if cmds.checkBox(limb_attr_18, query=True, value=True):
			cmds.addAttr(ln= 'RING', at= 'enum', en='---', k=1)
			cmds.setAttr(str(limb_list[i]) + '.RING', k=0, cb=1, l=1)
			cmds.addAttr(ln= 'Ring_01', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Ring_02', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Ring_03', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Ring_04', at='float', min= -10, max= 10, dv= 0, k=1)
			print('sep ring attr added')
		if cmds.checkBox(limb_attr_19, query=True, value=True):
			cmds.addAttr(ln= 'PINKY', at= 'enum', en='---', k=1)
			cmds.setAttr(str(limb_list[i]) + '.PINKY', k=0, cb=1, l=1)
			cmds.addAttr(ln= 'Pinky_01', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Pinky_02', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Pinky_03', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Pinky_04', at='float', min= -10, max= 10, dv= 0, k=1)
			print('sep pinky attr added')
		if cmds.checkBox(limb_attr_20, query=True, value=True):
			cmds.addAttr(ln= 'THUMB', at= 'enum', en='---', k=1)
			cmds.setAttr(str(limb_list[i]) + '.THUMB', k=0, cb=1, l=1)
			cmds.addAttr(ln= 'Thumb_01', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Thumb_02', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Thumb_03', at='float', min= -10, max= 10, dv= 0, k=1)
			cmds.addAttr(ln= 'Thumb_04', at='float', min= -10, max= 10, dv= 0, k=1)
			print('sep thumb attr added')
		i+=1
	
def Add_Feet_Attr(feet_attr_01, feet_attr_02, feet_attr_03, feet_attr_04, feet_attr_05, feet_attr_06, feet_attr_07, feet_attr_08, feet_attr_09, feet_attr_10, feet_attr_11, feet_attr_12, feet_attr_13, feet_attr_14, feet_attr_15, feet_attr_16, feet_attr_17, feet_attr_18, feet_attr_19, feet_attr_20):
	i=0
	feet_list = cmds.ls(sl=True)
	print feet_list
	for obj in feet_list:
		cmds.select(cl=True)
		cmds.select(feet_list[i])
		print 'working on: ', feet_list[i]
		if cmds.checkBox(feet_attr_01, query=True, value=True):
			cmds.addAttr(ln='fkik', nn='---', at= 'enum', en = '---', k=1)
			cmds.setAttr(str(feet_list[i]) + '.fkik', cb=1, k=0, l=1)
			cmds.addAttr(ln= 'FKIK', at= 'float', dv=0, min=0, max=10, k=1)
			print('FKIK attr added')
		if cmds.checkBox(feet_attr_02, query=True, value=True):
			cmds.addAttr(ln= 'Length_01', dv=0, min= -10, max= 10, k=1)
			print('length_01 attr added')
		if cmds.checkBox(feet_attr_03, query=True, value=True):
			cmds.addAttr(ln= 'Length_01_Vol', dv=0, min= -10, max= 10, k=1)
			print('length_01_vol attr added')
		if cmds.checkBox(feet_attr_04, query=True, value=True):
			cmds.addAttr(ln= 'Length_02', dv=0, min= -10, max= 10, k=1)
			print('length_02 attr added')
		if cmds.checkBox(feet_attr_05, query=True, value=True):
			cmds.addAttr(ln= 'Length_02_Vol', dv=0, min= -10, max= 10, k=1)
			print('length_02_vol attr added')
		if cmds.checkBox(feet_attr_06, query=True, value=True):
			cmds.addAttr(ln= 'Stretchy', dv=0, min= 0, max= 10, k=1)
			print('stretchy attr added')
		if cmds.checkBox(feet_attr_07, query=True, value=True):
			cmds.addAttr(ln='Bendy_Vis', at='float', min= 0, dv= 0, max= 1, k=1)
			print('bendy_vis attr added')
		if cmds.checkBox(feet_attr_08, query=True, value=True):
			cmds.addAttr(ln= 'PV_Space', at='enum', en= 'World:COG:Feet', k=1)
			print('pv_space attr added')
		if cmds.checkBox(feet_attr_09, query=True, value=True):
			cmds.addAttr(ln= 'Twist', at='float', min= -180, max= 180, dv=0, k=1)
			print('twist attr added')
		if cmds.checkBox(feet_attr_10, query=True, value=True):
			cmds.addAttr(ln= 'Soft_IK', at='float', min=0, dv=0, max=10)
			print('soft IK attr added')
		if cmds.checkBox(feet_attr_11, query=True, value=True):
			cmds.addAttr(ln= 'foot_Roll', at='float', min=-10, dv=0, max=10, k=1)
			print('foot roll attr added')
		if cmds.checkBox(feet_attr_12, query=True, value=True):
			cmds.addAttr(ln= 'Roll_angle', at='float', min=-60, dv=0, max=60, k=1)
			print('roll angle attr added')
		if cmds.checkBox(feet_attr_13, query=True, value=True):
			cmds.addAttr(ln= 'Heel_Raise', at='float', min=-10, dv=0, max=10, k=1)
			print('heel raise attr added')
		if cmds.checkBox(feet_attr_14, query=True, value=True):
			cmds.addAttr(ln= 'Ball_Raise', at='float', min=-10, dv=0, max=10, k=1)
			print('attr added')
		if cmds.checkBox(feet_attr_15, query=True, value=True):
			cmds.addAttr(ln= 'Toe_Raise', at='float', min=-10, dv=0, max=10, k=1)
			print('ball raise attr added')
		if cmds.checkBox(feet_attr_16, query=True, value=True):
			cmds.addAttr(ln= 'Heel_Slide', at='float', min=-10, dv=0, max=10, k=1)
			print('heel slide attr added')
		if cmds.checkBox(feet_attr_17, query=True, value=True):
			cmds.addAttr(ln= 'Ball_Slide', at='float', min=-10, dv=0, max=10, k=1)
			print('ball slide attr added')
		if cmds.checkBox(feet_attr_18, query=True, value=True):
			cmds.addAttr(ln= 'Toe_Slide', at='float', min=-10, dv=0, max=10, k=1)
			print('toe slide attr added')
		if cmds.checkBox(feet_attr_19, query=True, value=True):
			cmds.addAttr(ln= 'Rock', at='float', min=-10, dv=0, max=10, k=1)
			print('rock attr added')
		if cmds.checkBox(feet_attr_20, query=True, value=True):
			cmds.addAttr(ln= 'Banking', at='float', min=-10, dv=0, max=10, k=1)
			print('banking attr added')
		i+=1

def Add_Space_Attr(ss_attr_01,ss_attr_02,ss_attr_03,ss_attr_04):
	i=0
	ss_list = cmds.ls(sl=True)
	print ss_list
	Boolean_list = []
	if cmds.checkBox(ss_attr_01, query=True, value=True):
		Boolean_list.append('LOCAL:')
	if cmds.checkBox(ss_attr_02, query=True, value=True):
		Boolean_list.append('World:')
	if cmds.checkBox(ss_attr_03, query=True, value=True):
		Boolean_list.append('COG:')
	if cmds.checkBox(ss_attr_04, query=True, value=True):
		Boolean_list.append('Head')
	print str(Boolean_list)
	var = ""
	for item in Boolean_list:
		var = var + item 
		
	for obj in ss_list:
		cmds.select(cl=True)
		cmds.select(ss_list[i])
		print 'working on: ', ss_list[i]
		cmds.addAttr(ln= 'Space', at= 'enum', en= var , k=1)
		i+=1
		
		
#----------------------------------------------------------
def sel_trans_all(trans_X,trans_Y,trans_Z, state, *args):
	if state:
		cmds.checkBox(trans_X, e=1, v=1)
		cmds.checkBox(trans_Y, e=1, v=1)
		cmds.checkBox(trans_Z, e=1, v=1)
	else:
		cmds.checkBox(trans_X, e=1, v=0)
		cmds.checkBox(trans_Y, e=1, v=0)
		cmds.checkBox(trans_Z, e=1, v=0)

def sel_rot_all(rot_X,rot_Y,rot_Z, state, *args):
	if state:
		cmds.checkBox(rot_X, e=1, v=1)
		cmds.checkBox(rot_Y, e=1, v=1)
		cmds.checkBox(rot_Z, e=1, v=1)
	else:
		cmds.checkBox(rot_X, e=1, v=0)
		cmds.checkBox(rot_Y, e=1, v=0)
		cmds.checkBox(rot_Z, e=1, v=0)

def sel_scl_all(scl_X, scl_Y, scl_Z, state, *args):
	if state:
		cmds.checkBox(scl_X, e=1, v=1)
		cmds.checkBox(scl_Y, e=1, v=1)
		cmds.checkBox(scl_Z, e=1, v=1)
	else:
		cmds.checkBox(scl_X, e=1, v=0)
		cmds.checkBox(scl_Y, e=1, v=0)
		cmds.checkBox(scl_Z, e=1, v=0)
		
def radio_sel_all(trans_All, rot_All, scl_All,trans_X,trans_Y,trans_Z, rot_X,rot_Y,rot_Z, scl_X, scl_Y, scl_Z, vis, state, *args):
	if state:
		cmds.checkBox(trans_All, e=1, v=1)
		cmds.checkBox(rot_All, e=1, v=1)
		cmds.checkBox(scl_All, e=1, v=1)
		cmds.checkBox(vis, e=1, v=1)
		cmds.checkBox(trans_X, e=1, v=1)
		cmds.checkBox(trans_Y, e=1, v=1)
		cmds.checkBox(trans_Z, e=1, v=1)
		cmds.checkBox(rot_X, e=1, v=1)
		cmds.checkBox(rot_Y, e=1, v=1)
		cmds.checkBox(rot_Z, e=1, v=1)
		cmds.checkBox(scl_X, e=1, v=1)
		cmds.checkBox(scl_Y, e=1, v=1)
		cmds.checkBox(scl_Z, e=1, v=1)
	else:
		cmds.checkBox(trans_All, e=1, v=0)
		cmds.checkBox(rot_All, e=1, v=0)
		cmds.checkBox(scl_All, e=1, v=0)
		cmds.checkBox(vis, e=1, v=0)
		cmds.checkBox(trans_X, e=1, v=0)
		cmds.checkBox(trans_Y, e=1, v=0)
		cmds.checkBox(trans_Z, e=1, v=0)
		cmds.checkBox(rot_X, e=1, v=0)
		cmds.checkBox(rot_Y, e=1, v=0)
		cmds.checkBox(rot_Z, e=1, v=0)
		cmds.checkBox(scl_X, e=1, v=0)
		cmds.checkBox(scl_Y, e=1, v=0)
		cmds.checkBox(scl_Z, e=1, v=0)
	
def enable_boolean_func(Attribute, LongName, Boolean, BooleanName, min_txt, max_txt, def_txt, min_val, max_val, def_val, state, *args):
	if state:
		cmds.textField(LongName, e=1, en= True)
		cmds.floatField(min_val, e=1, en= False)
		cmds.floatField(max_val, e=1, en= False)
		cmds.floatField(def_val, e=1, en= False)
		cmds.text(Attribute, e=1, en=True)
		cmds.text(min_txt, e=1, en=False)
		cmds.text(max_txt, e=1, en=False)
		cmds.text(def_txt, e=1, en=False)
		cmds.text(Boolean , e=1, en= True)
		cmds.textField(BooleanName, e=1, en=True)
	else:
		cmds.textField(LongName, e=1, en= True)
		cmds.floatField(min_val, e=1, en= True)
		cmds.floatField(max_val, e=1, en= True)
		cmds.floatField(def_val, e=1, en= True)
		cmds.text(Attribute, e=1, en=True)
		cmds.text(min_txt, e=1, en=True)
		cmds.text(max_txt, e=1, en=True)
		cmds.text(def_txt, e=1, en=True)
		cmds.text(Boolean , e=1, en= False)
		cmds.textField(BooleanName, e=1, en=False)

def all_global_sel(global_attr_01, global_attr_02, global_attr_03, global_attr_04, global_attr_05, global_attr_06, state, *args):
	if state:
		cmds.checkBox(global_attr_01, e=1, v=1)
		cmds.checkBox(global_attr_02, e=1, v=1)
		cmds.checkBox(global_attr_03, e=1, v=1)
		cmds.checkBox(global_attr_04, e=1, v=1)
		cmds.checkBox(global_attr_05, e=1, v=1)
		cmds.checkBox(global_attr_06, e=1, v=1)
	else:
		cmds.checkBox(global_attr_01, e=1, v=0)
		cmds.checkBox(global_attr_02, e=1, v=0)
		cmds.checkBox(global_attr_03, e=1, v=0)
		cmds.checkBox(global_attr_04, e=1, v=0)
		cmds.checkBox(global_attr_05, e=1, v=0)
		cmds.checkBox(global_attr_06, e=1, v=0)
		
def all_limb_sel(limb_attr_01,limb_attr_02,limb_attr_03,limb_attr_04,limb_attr_05,limb_attr_06,limb_attr_07,limb_attr_08,limb_attr_09,limb_attr_10,limb_attr_11,limb_attr_12,limb_attr_13,limb_attr_14,limb_attr_15,limb_attr_16,limb_attr_17,limb_attr_18,limb_attr_19,limb_attr_20, state, *args):
	if state:
		cmds.checkBox(limb_attr_01, e=1, v=1)
		cmds.checkBox(limb_attr_02, e=1, v=1)
		cmds.checkBox(limb_attr_03, e=1, v=1)
		cmds.checkBox(limb_attr_04, e=1, v=1)
		cmds.checkBox(limb_attr_05, e=1, v=1)
		cmds.checkBox(limb_attr_06, e=1, v=1)
		cmds.checkBox(limb_attr_07, e=1, v=1)
		cmds.checkBox(limb_attr_08, e=1, v=1)
		cmds.checkBox(limb_attr_09, e=1, v=1)
		cmds.checkBox(limb_attr_10, e=1, v=1)
		cmds.checkBox(limb_attr_11, e=1, v=1)
		cmds.checkBox(limb_attr_12, e=1, v=1)
		cmds.checkBox(limb_attr_13, e=1, v=1)
		cmds.checkBox(limb_attr_14, e=1, v=1)
		cmds.checkBox(limb_attr_15, e=1, v=1)
		cmds.checkBox(limb_attr_16, e=1, v=1)
		cmds.checkBox(limb_attr_17, e=1, v=1)
		cmds.checkBox(limb_attr_18, e=1, v=1)
		cmds.checkBox(limb_attr_19, e=1, v=1)
		cmds.checkBox(limb_attr_20, e=1, v=1)
	else:
		cmds.checkBox(limb_attr_01, e=1, v=0)
		cmds.checkBox(limb_attr_02, e=1, v=0)
		cmds.checkBox(limb_attr_03, e=1, v=0)
		cmds.checkBox(limb_attr_04, e=1, v=0)
		cmds.checkBox(limb_attr_05, e=1, v=0)
		cmds.checkBox(limb_attr_06, e=1, v=0)
		cmds.checkBox(limb_attr_07, e=1, v=0)
		cmds.checkBox(limb_attr_08, e=1, v=0)
		cmds.checkBox(limb_attr_09, e=1, v=0)
		cmds.checkBox(limb_attr_10, e=1, v=0)
		cmds.checkBox(limb_attr_11, e=1, v=0)
		cmds.checkBox(limb_attr_12, e=1, v=0)
		cmds.checkBox(limb_attr_13, e=1, v=0)
		cmds.checkBox(limb_attr_14, e=1, v=0)
		cmds.checkBox(limb_attr_15, e=1, v=0)
		cmds.checkBox(limb_attr_16, e=1, v=0)
		cmds.checkBox(limb_attr_17, e=1, v=0)
		cmds.checkBox(limb_attr_18, e=1, v=0)
		cmds.checkBox(limb_attr_19, e=1, v=0)
		cmds.checkBox(limb_attr_20, e=1, v=0)
		
def all_feet_sel(feet_attr_01, feet_attr_02, feet_attr_03, feet_attr_04, feet_attr_05, feet_attr_06, feet_attr_07, feet_attr_08, feet_attr_09, feet_attr_10, feet_attr_11, feet_attr_12, feet_attr_13, feet_attr_14, feet_attr_15, feet_attr_16, feet_attr_17, feet_attr_18, feet_attr_19, feet_attr_20, state, *args):
	if state:
		cmds.checkBox(feet_attr_01, e=1, v=1)
		cmds.checkBox(feet_attr_02, e=1, v=1)
		cmds.checkBox(feet_attr_03, e=1, v=1)
		cmds.checkBox(feet_attr_04, e=1, v=1)
		cmds.checkBox(feet_attr_05, e=1, v=1)
		cmds.checkBox(feet_attr_06, e=1, v=1)
		cmds.checkBox(feet_attr_07, e=1, v=1)
		cmds.checkBox(feet_attr_08, e=1, v=1)
		cmds.checkBox(feet_attr_09, e=1, v=1)
		cmds.checkBox(feet_attr_10, e=1, v=1)
		cmds.checkBox(feet_attr_11, e=1, v=1)
		cmds.checkBox(feet_attr_12, e=1, v=1)
		cmds.checkBox(feet_attr_13, e=1, v=1)
		cmds.checkBox(feet_attr_14, e=1, v=1)
		cmds.checkBox(feet_attr_15, e=1, v=1)
		cmds.checkBox(feet_attr_16, e=1, v=1)
		cmds.checkBox(feet_attr_17, e=1, v=1)
		cmds.checkBox(feet_attr_18, e=1, v=1)
		cmds.checkBox(feet_attr_19, e=1, v=1)
		cmds.checkBox(feet_attr_20, e=1, v=1)
	else:
		cmds.checkBox(feet_attr_01, e=1, v=0)
		cmds.checkBox(feet_attr_02, e=1, v=0)
		cmds.checkBox(feet_attr_03, e=1, v=0)
		cmds.checkBox(feet_attr_04, e=1, v=0)
		cmds.checkBox(feet_attr_05, e=1, v=0)
		cmds.checkBox(feet_attr_06, e=1, v=0)
		cmds.checkBox(feet_attr_07, e=1, v=0)
		cmds.checkBox(feet_attr_08, e=1, v=0)
		cmds.checkBox(feet_attr_09, e=1, v=0)
		cmds.checkBox(feet_attr_10, e=1, v=0)
		cmds.checkBox(feet_attr_11, e=1, v=0)
		cmds.checkBox(feet_attr_12, e=1, v=0)
		cmds.checkBox(feet_attr_13, e=1, v=0)
		cmds.checkBox(feet_attr_14, e=1, v=0)
		cmds.checkBox(feet_attr_15, e=1, v=0)
		cmds.checkBox(feet_attr_16, e=1, v=0)
		cmds.checkBox(feet_attr_17, e=1, v=0)
		cmds.checkBox(feet_attr_18, e=1, v=0)
		cmds.checkBox(feet_attr_19, e=1, v=0)
		cmds.checkBox(feet_attr_20, e=1, v=0)
		
def all_ss_sel(ss_attr_01, ss_attr_02, ss_attr_03, ss_attr_04, ss_attr_05, state, *args):
	if state:
		cmds.checkBox(ss_attr_01, e=1, v=1)
		cmds.checkBox(ss_attr_02, e=1, v=1)
		cmds.checkBox(ss_attr_03, e=1, v=1)
		cmds.checkBox(ss_attr_04, e=1, v=1)
		cmds.checkBox(ss_attr_05, e=1, v=1)
	else:
		cmds.checkBox(ss_attr_01, e=1, v=0)
		cmds.checkBox(ss_attr_02, e=1, v=0)
		cmds.checkBox(ss_attr_03, e=1, v=0)
		cmds.checkBox(ss_attr_04, e=1, v=0)
		cmds.checkBox(ss_attr_05, e=1, v=0)
