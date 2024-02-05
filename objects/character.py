from utils.enums.SkillType import SkillType

class Character:
    def __init__(self, name: str, picture: str, pictureDead: str, hp: int, mp: int, defense: int, dexterity: int, strength: int,
                  intelligence: int, faith: int, charisma: int, skills: list[SkillType],  st: int, dead: bool):
        self.name = name
        self.picture = picture
        self.pictureDead = pictureDead
        self.hp = hp
        self.mp = mp
        self.defense = defense
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.faith = faith
        self.charisma = charisma
        self.skills = skills
        self.st = st
        self.dead = dead