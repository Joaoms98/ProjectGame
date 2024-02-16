from utils.enums.SkillType import SkillType

class Skill:
    def __init__(self, name: str, skillType: SkillType, damage: int, mp: int, attribute_test: str):
        self.name = name
        self.skillType = skillType
        self.damage = damage
        self.mp = mp
        self.attribute_test = attribute_test