import random
pantsCover = [
    'pelvis',
    'rleg',
    'lleg',
    'rknee',
    'lknee',
    'rfoot',
    'lfoot'
]

shirtCover = [
    'torso',
    'rshoulder',
    'lshoulder',
    'relbow',
    'lelbow',
    'rhand',
    'lhand'
]

smallAxe = {
    'name':'Small axe',
    'damage':5,
    'state':'normal',
    'type':'axe',
    'wield':'oneHanded',
    'material':'Steel',
    'equipped': True
}

pike = {
    'name':'Pike',
    'damage':5,
    'state':'normal',
    'type':'spear',
    'wield':'dual',
    'material':'Steel',
    'equipped': True
}

helmet = {
    'name':'Crusader helmet',
    'defense':'50',
    'state':'normal',
    'type':'rhemlet',
    'material':'Steel',
    'equipped':True,
    '':''
}

gorget = {
    'name':'Gorget',
    'defense':'50',
    'state':'normal',
    'type':'rneck',
    'material':'Steel',
    'equipped': True,
    '':''
}

breastplate = {
    'name':'Steel full breastplate',
    'defense':'50',
    'state':'normal',
    'type':'rchest',
    'material':'Steel',
    'equipped': True,
    '':''
}

pauldron = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

elbowCop = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

gauntlet = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

beltArmor = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

belt = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

codpiece = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

legArmor = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

kneeCop = {
    'name':'',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

jamb = {
    'name':'Steel jamb',
    'defense':'50',
    'state':'normal',
    'type':'',
    'material':'Steel',
    'equipped': True,
    '':''
}

shirt = {
    'name':'Shirt',
    'health':1,
    'state':'normal',
    'type':'shirt',
    'material':'Fabric',
    'equipped': True,
    'cover': shirtCover
}

pants = {
    'name':'Pants',
    'health':1,
    'state':'normal',
    'type':'pants',
    'material':'Fabric',
    'equipped': True,
    'cover': pantsCover
}



knightSet = {
    'rwield':pike,
    'lwield':pike,
    'helmet':helmet,
    'rhelmet': None,
    'neck':'',
    'rneck':'',
    'chest':'',
    'rchest':'',
    'bag':'',
    'belt':'',
    'rbelt':'',
    'pants':'',
    'rpants':'',
    'rleg':'',
    'lleg':'',
    'rknee':'',
    'lknee':'',
    'rfoot':'',
    'lfoot':'',
    'rshoulder':'', 
    'lshoulder':'',
    'relbow':'',
    'lelbow':'',
    'rhand':'',
    'lhand':'',
    'rring1':'',
    'lring1':'',
    'rring2':'',
    'lring2':'',
    'rring3':'',
    'lring3':'',
    'rring4':'',
    'lring4':''
}

adventurerSet = {
    'rwield':smallAxe,
    'lwield':None,
    'helmet':None,
    'rhelmet':None,
    'neck':None,
    'rneck':None,
    'chest':shirt,
    'rchest':None,
    'bag':None,
    'belt':None,
    'rbelt':None,
    'pants':pants,
    'rpants':None,
    'rleg':None,
    'lleg':None,
    'rknee':None,
    'lknee':None,
    'rfoot':None,
    'lfoot':None,
    'rshoulder':None, 
    'lshoulder':None,
    'relbow':None,
    'lelbow':None,
    'rhand':None,
    'lhand':None,
    'rring1':None,
    'lring1':None,
    'rring2':None,
    'lring2':None,
    'rring3':None,
    'lring3':None,
    'rring4':None,
    'lring4':None
}

Set = {
    'rwield':'',
    'lwield':'',
    'helmet':'',
    'rhelmet':'',
    'neck':'',
    'rneck':'',
    'chest':'',
    'rchest':'',
    'bag':'',
    'belt':'',
    'rbelt':'',
    'pants':'',
    'rpants':'',
    'rleg':'',
    'lleg':'',
    'rknee':'',
    'lknee':'',
    'rfoot':'',
    'lfoot':'',
    'rshoulder':'', 
    'lshoulder':'',
    'relbow':'',
    'lelbow':'',
    'rhand':'',
    'lhand':'',
    'rring1':'',
    'lring1':'',
    'rring2':'',
    'lring2':'',
    'rring3':'',
    'lring3':'',
    'rring4':'',
    'lring4':''
}

Set = {
    'rwield':'',
    'lwield':'',
    'helmet':'',
    'rhelmet':'',
    'neck':'',
    'rneck':'',
    'chest':'',
    'rchest':'',
    'bag':'',
    'belt':'',
    'rbelt':'',
    'pants':'',
    'rpants':'',
    'rleg':'',
    'lleg':'',
    'rknee':'',
    'lknee':'',
    'rfoot':'',
    'lfoot':'',
    'rshoulder':'', 
    'lshoulder':'',
    'relbow':'',
    'lelbow':'',
    'rhand':'',
    'lhand':'',
    'rring1':'',
    'lring1':'',
    'rring2':'',
    'lring2':'',
    'rring3':'',
    'lring3':'',
    'rring4':'',
    'lring4':''
}

#
# PREBUILD LOCATIONS TILES
# FOREST

fwoods = {
    'fwall': 1,
    'rwall': 0,
    'lwall': 0,
    'bwall': 0
}

rwoods = {
    'fwall': 0,
    'rwall': 1,
    'lwall': 0,
    'bwall': 0
}

lwoods = {
    'fwall': 0,
    'rwall': 0,
    'lwall': 1,
    'bwall': 0
}

bwoods = {
    'fwall': 0,
    'rwall': 0,
    'lwall': 0,
    'bwall': 1
}
forest_location_list = [fwoods, rwoods, lwoods, bwoods]
# DUNGEON
room1 = {
    'fwall': 0,
    'rwall': 1,
    'lwall': 1,
    'bwall': 0
}

room2 = {
    'fwall': 0,
    'rwall': 0,
    'lwall': 0,
    'bwall': 0
}

room3 = {
    'fwall': 0,
    'rwall': 0,
    'lwall': 1,
    'bwall': 1
}

room4 = {
    'fwall': 1,
    'rwall': 0,
    'lwall': 1,
    'bwall': 0
}

room5 = {
    'fwall': 1,
    'rwall': 1,
    'lwall': 0,
    'bwall': 0
}

room6 = {
    'fwall': 0,
    'rwall': 1,
    'lwall': 0,
    'bwall': 1
}

room7 = {
    'fwall': 1,
    'rwall': 0,
    'lwall': 0,
    'bwall': 1
}
dungeon_location_list = [room1, room2, room3, room4, room5, room6, room7]
# VOID

void = {
    'fwall': 0,
    'rwall': 0,
    'lwall': 0,
    'bwall': 0
    }

#print(adventurerSet.items())


print(random.choice(list(forest_location_list)))
print(random.choice(list(dungeon_location_list)))