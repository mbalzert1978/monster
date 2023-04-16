from BasicClasses.player_classes import Paladin, Rogue

available_player_classes = [Paladin(), Rogue()]
for class_ in available_player_classes:
    var = class_.__str__()
    print(var[: var.find("(")])
