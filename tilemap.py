

#tileset structure 
#width: 32
#height: 32
#zIndex = 1
#visible = True
#layers = {
#"background": 
#{
#"size": [32,32],
#"visible": True,
#"tiles": [[1,1,1,1,1,1],[1,1,1,1,2,2], [1,1,1,2,2,1,2]]
#}
#}
#tilesProperties = {
#"sprites":
#{
#"1": "grass.png"
#"2": "rocks.png"
#"3": "tree.png"
#"0": "void.png"
#},
#"properties": 
#{
#"1": {"collision": True, "evil": True, "slow": True}
#}
#}
class Tilemap:
    def __init__(self, position, size, tiles, tilesProperties):
        pass

    def render(self):
        pass
