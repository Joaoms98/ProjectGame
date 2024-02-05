from utils.enums.SkillType import SkillType

class Skill:
    def __init__(self, name: str, skillType: SkillType, damage: int, mp: int):
        self.name = name
        self.skillType = skillType
        self.damage = damage
        self.mp = mp