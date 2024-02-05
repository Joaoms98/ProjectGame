from enum import Enum

class SkillType(Enum):

    AREA = 1

    HEAL = 2

    DIRECT = 3

SkillType = Enum('SkillType', ['AREA', 'HEAL', 'DIRECT'])