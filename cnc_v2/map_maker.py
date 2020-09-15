#/bin/python

# CNC Easy Starter

# Cylinder style 8 player map generator

# Collect Data
import pygame
import cnc_classes as cncc
import random
import datetime


def get_names():
	# Returns an array of city names
	names = ["Calumet","Irons","Duluth","Cologne","Frankfurt","Alsance","Black Rock","Mass City","Marquette","Mackinac","Toledo","Ottowa","Cincinatti","Defiance","San Floyde","Marais","Mariucci","Bristol","Lancaster","Abney","Sherpa","McAlister","Monogahela","Charleston","Morgantown","Edray","Montrose","Sharpe","Calhammer","Ashville","MacInnis","Hancock","Houghton","Sandusky","Dresden","Brimingham","Wester","Nicolet","Ontonagon","Hiawatha","Hamtramck","Sarnia","Hamilton","Castle Danger","Lutsen","L\'Anse","Lang","Beach","Murello","Seeny","Escanaba","Fox Den","Huron","Gooseberry","Mississauga","Erie","Superior","Yost","The Soo"]
	return names

def pick(names):
	# Randomly gets an item from the array
	# Return choice and array
	this_name = random.choice(names)
	names.remove(this_name)
	return this_name,names

def chose_hex(cx,cy,names,box,a_nation):
	# Takes a list of names, a list of hex types, and a nation and turns this into a hex
	# Returns a hex to append to a map list
	# ONLY USE ON NEW MAPS!
	# Return the names and box arrays with a name/box removed
	hex_type,box = pick(box)
	if hex_type == "metro":
		this_name,names = pick(names)
		if a_nation:
			this_hex = cncc.map_hex(cx,cy,hex_type,a_nation,this_name,15,25,0,[])
		else:
			this_hex = cncc.map_hex(cx,cy,hex_type,None,this_name,0,25,25,[])
	elif hex_type == "mine":
		this_name,names = pick(names)
		if a_nation:
			this_hex = cncc.map_hex(cx,cy,hex_type,a_nation,this_name,5,25,250,[])
		else:
			this_hex = cncc.map_hex(cx,cy,hex_type,None,this_name,0,25,250,[])
	elif hex_type == "wilds":
		this_hex = cncc.map_hex(cx,cy,hex_type,None,"Wilds",0,25,50,[])
	elif hex_type == "wastes":
		this_hex = cncc.map_hex(cx,cy,hex_type,None,"Wastelands",0,0,0,[])

	return this_hex,names,box


def quick_map():
	# Defines the hexes in an 8 player map for testing, will eventually take inputs 

	# Define 8 players
	# Load Sigils? - tbh 
	# 	self,playername,sigil_fp,color,god,colonies):
	nations = []
	nations.append(cncc.your_nation("Player 1","./images/sigils/sigil_blue.png",[0,0,255],True,0))
	nations.append(cncc.your_nation("Player 2","./images/sigils/sigil_cyan.png",[0,255,255],False,0))
	nations.append(cncc.your_nation("Player 3","./images/sigils/sigil_mag.png",[255,0,255],False,0))
	nations.append(cncc.your_nation("Player 4","./images/sigils/sigil_red.png",[255,0,0],False,0))
	nations.append(cncc.your_nation("Player 5","./images/sigils/sigil_green.png",[0,255,0],False,0))
	nations.append(cncc.your_nation("Player 6","./images/sigils/sigil_yellow.png",[255,255,0],False,0))
	nations.append(cncc.your_nation("Player 7","./images/sigils/sigil_pink.png",[255,153,255],False,0))
	nations.append(cncc.your_nation("Player 8","./images/sigils/sigil_orange.png",[255,100,100],False,0))

	# List of dispersed 
	# For each player:
		# 1 metro in the center
		# 1 "free" metro
		# 4 free mines
		# 1 waste
		# 7 Wildnerness tiles
	# In the equals
		# 2 per player
		# 1:3 metro:mine

	neutrals = ["metro","metro","metro","metro","mine","mine","mine","mine","mine","mine","mine","mine","mine","mine","mine","mine"]
	all_names = get_names()

	prov_1 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_2 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_3 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_4 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_5 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_6 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_7 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]
	prov_8 = ["mine","mine","mine","wilds","metro","wilds","wilds","wilds","wilds","wilds","wastes"]

	# Nations may have their own list of cities as well

	rows = 7
	columns = 16
	this_map = []

	#1-1, true neutral
	this_hex,all_names,neutrals = chose_hex(1,1,all_names,neutrals,None)
	this_map.append(this_hex)
	#1-2, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(1,2,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#1-3, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(1,3,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#1-4, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(1,4,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#1-5, true neutral
	this_hex,all_names,neutrals = chose_hex(1,5,all_names,neutrals,None)
	this_map.append(this_hex)
	#1-6, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(1,6,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#1-7, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(1,7,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#########################
	#2-1, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(2,1,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#2-2, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(2,2,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#2-3, Nation 1 Capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(2,3,"metro",nations[0],cap_name,30,25,0,[]))
	#2-4, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(2,4,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#2-5, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(2,5,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#2-6, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(2,6,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#2-7, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(2,7,all_names,prov_2,nations[1])
	this_map.append(this_hex)	
	#########################
	#3-1, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(3,1,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#3-2, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(3,2,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#3-3, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(3,3,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#3-4, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(3,4,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#3-5, Nation 2 capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(3,5,"metro",nations[1],cap_name,30,25,0,[]))
	#3-6, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(3,6,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#3-7, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(3,7,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#########################
	#4-1, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(4,1,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#4-2, Nation 1 outlier
	this_hex,all_names,prov_1 = chose_hex(4,2,all_names,prov_1,nations[0])
	this_map.append(this_hex)
	#4-3, True Neutral
	this_hex,all_names,neutrals = chose_hex(4,3,all_names,neutrals,None)
	this_map.append(this_hex)
	#4-4, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(4,4,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#4-5, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(4,5,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#4-6, Nation 2 outlier
	this_hex,all_names,prov_2 = chose_hex(4,6,all_names,prov_2,nations[1])
	this_map.append(this_hex)
	#4-7, True Neutral
	this_hex,all_names,neutrals = chose_hex(4,7,all_names,neutrals,None)
	this_map.append(this_hex)
	#########################
	#5-1,True neutral
	this_hex,all_names,neutrals = chose_hex(5,1,all_names,neutrals,None)
	this_map.append(this_hex)
	#5-2, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(5,2,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#5-3, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(5,3,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#5-4, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(5,4,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#5-5, True neutral
	this_hex,all_names,neutrals = chose_hex(5,5,all_names,neutrals,None)
	this_map.append(this_hex)
	#5-6, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(5,6,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#5-7, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(5,7,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#########################
	#6-1, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(6,1,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#6-2, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(6,2,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#6-3, Nation 3 Capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(6,3,"metro",nations[2],cap_name,30,25,0,[]))
	#6-4, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(6,4,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#6-5, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(6,5,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#6-6, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(6,6,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#6-7, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(6,7,all_names,prov_4,nations[3])
	this_map.append(this_hex)	
	#########################
	#7-1, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(7,1,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#7-2, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(7,2,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#7-3, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(7,3,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#7-4, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(7,4,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#7-5, Nation 4 capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(7,5,"metro",nations[3],cap_name,30,25,0,[]))
	#7-6, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(7,6,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#7-7, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(7,7,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#########################
	#8-1, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(8,1,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#8-2, Nation 3 outlier
	this_hex,all_names,prov_3 = chose_hex(8,2,all_names,prov_3,nations[2])
	this_map.append(this_hex)
	#8-3, True Neutral
	this_hex,all_names,neutrals = chose_hex(8,3,all_names,neutrals,None)
	this_map.append(this_hex)
	#8-4, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(8,4,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#8-5, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(8,5,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#8-6, Nation 4 outlier
	this_hex,all_names,prov_4 = chose_hex(8,6,all_names,prov_4,nations[3])
	this_map.append(this_hex)
	#8-7, True Neutral
	this_hex,all_names,neutrals = chose_hex(8,7,all_names,neutrals,None)
	this_map.append(this_hex)
	#########################
	#9-1,True neutral
	this_hex,all_names,neutrals = chose_hex(9,1,all_names,neutrals,None)
	this_map.append(this_hex)
	#9-2, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(9,2,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#9-3, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(9,3,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#9-4, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(9,3,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#9-5, True neutral
	this_hex,all_names,neutrals = chose_hex(9,5,all_names,neutrals,None)
	this_map.append(this_hex)
	#9-6, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(9,6,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#9-7, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(9,7,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#########################
	#10-1, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(10,1,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#10-2, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(10,2,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#10-3, Nation 5 Capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(10,3,"metro",nations[4],cap_name,30,25,0,[]))
	#10-4, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(10,4,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#10-5, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(10,5,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#10-6, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(10,6,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#10-7, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(10,7,all_names,prov_6,nations[5])
	this_map.append(this_hex)	
	#########################
	#11-1, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(11,1,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#11-2, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(11,2,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#11-3, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(11,3,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#11-4, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(11,4,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#11-5, Nation 6 capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(11,5,"metro",nations[5],cap_name,30,25,0,[]))
	#11-6, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(11,6,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#11-7, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(11,7,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#########################
	#12-1, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(12,1,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#12-2, Nation 5 outlier
	this_hex,all_names,prov_5 = chose_hex(12,2,all_names,prov_5,nations[4])
	this_map.append(this_hex)
	#12-3, True Neutral
	this_hex,all_names,neutrals = chose_hex(12,3,all_names,neutrals,None)
	this_map.append(this_hex)
	#12-4, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(12,4,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#12-5, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(12,5,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#12-6, Nation 6 outlier
	this_hex,all_names,prov_6 = chose_hex(12,6,all_names,prov_6,nations[5])
	this_map.append(this_hex)
	#12-7, True Neutral
	this_hex,all_names,neutrals = chose_hex(12,7,all_names,neutrals,None)
	this_map.append(this_hex)
	#########################
	#13-1,True neutral
	this_hex,all_names,neutrals = chose_hex(13,1,all_names,neutrals,None)
	this_map.append(this_hex)
	#13-2, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(13,2,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#13-3, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(13,3,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#13-4, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(13,3,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#13-5, True neutral
	this_hex,all_names,neutrals = chose_hex(13,5,all_names,neutrals,None)
	this_map.append(this_hex)
	#13-6, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(13,6,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#13-7, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(13,7,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#########################
	#14-1, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(14,1,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#14-2, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(14,2,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#14-3, Nation 7 Capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(14,3,"metro",nations[6],cap_name,30,25,0,[]))
	#14-4, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(14,4,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#14-5, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(14,5,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#14-6, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(14,6,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#14-7, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(14,7,all_names,prov_8,nations[7])
	this_map.append(this_hex)	
	#########################
	#15-1, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(15,1,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#15-2, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(15,2,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#15-3, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(15,3,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#15-4, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(15,4,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#15-5, Nation 8 capital
	cap_name,all_names = pick(all_names)
	this_map.append(cncc.map_hex(15,5,"metro",nations[7],cap_name,30,25,0,[]))
	#15-6, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(15,6,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#15-7, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(15,7,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#########################
	#16-1, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(16,1,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#16-2, Nation 7 outlier
	this_hex,all_names,prov_7 = chose_hex(16,2,all_names,prov_7,nations[6])
	this_map.append(this_hex)
	#16-3, True Neutral
	this_hex,all_names,neutrals = chose_hex(16,3,all_names,neutrals,None)
	this_map.append(this_hex)
	#16-4, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(16,4,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#16-5, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(16,5,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#16-6, Nation 8 outlier
	this_hex,all_names,prov_8 = chose_hex(16,6,all_names,prov_8,nations[7])
	this_map.append(this_hex)
	#16-7, True Neutral
	this_hex,all_names,neutrals = chose_hex(16,7,all_names,neutrals,None)
	this_map.append(this_hex)

	# Get map size for the map
	row_d = columns*this_map[0].hex_width

	# Make a basic world

	# Get first orders due date based on map setup
	# 	def __init__(self,season,year,weather,due_date):

	d1 = datetime.datetime.now() + datetime.timedelta(minutes=15)

	

	# Fill map with units
	# Each nation starts with 1 ariship over the metropolis
	# (name,controller,cord_x,cord_y)



	this_world = cncc.world("spring",1,"clear",d1)

	# Return nations, map,world
	return nations,this_map,this_world,row_d



def big_8():
	pass

def big_6():
	pass