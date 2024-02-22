from enum import Enum

class SkillType(Enum):

    AREA = 1

    HEAL = 2

    DIRECTD6 = 3

    DIRECTD12 = 4

    DIRECTD20 = 5

SkillType = Enum('SkillType', ['AREA', 'HEAL', 'DIRECTD6', 'DIRECTD12', 'DIRECTD20'])