from utils.enums.SkillType import SkillType

class DamageCalculateService():
    def __init__(self, allies, enemies):
        self.allies = allies
        self.enemies = enemies

    def PlayerAttackDamage(self, attack_index, enemy_choice, allie_choice):
        damage = 5
        allie_choice.st = allie_choice.st -1

        if allie_choice.st <= 0:
            allie_choice.hp = allie_choice.hp - 1
            allie_choice.st = 10

        if allie_choice.skills[attack_index].skillType == SkillType.DIRECT:
            enemy_choice.hp = enemy_choice.hp - damage
            prompt_text = f"{allie_choice.name} atacou com o ataque{allie_choice.skills[attack_index].name} causando {damage} de dano"

        if allie_choice.skills[attack_index].skillType == SkillType.AREA:
            for enemy in self.enemies:
                enemy.hp = enemy.hp - damage

            prompt_text = f"{allie_choice.name} lançou {allie_choice.skills[attack_index].name} causando {damage} de dano"

        if allie_choice.skills[attack_index].skillType == SkillType.HEAL:
            for allie in self.allies:
                allie.hp = allie.hp + 1

            prompt_text = f"{allie_choice.name} lançou {allie_choice.skills[attack_index].name} curando {damage} do hp da equipe "

        return prompt_text

    def EnemyAttackDamage(self, attack_index, enemy_choice, allie_choice):
        damage = 5

        if allie_choice.skills[attack_index].skillType == SkillType.DIRECT:
            enemy_choice.hp = enemy_choice.hp - damage
            prompt_text = f"{allie_choice.name} atacou com {enemy_choice.name} com o ataque{allie_choice.skills[attack_index].name} causando {damage} de dano"
        
        if allie_choice.skills[attack_index].skillType == SkillType.AREA:
            for enemy in self.allies:
                enemy.hp = enemy.hp - damage

            prompt_text = f"{allie_choice.name} lançou {allie_choice.skills[attack_index].name} causando {damage} de dano"

        if allie_choice.skills[attack_index].skillType == SkillType.HEAL:
            for allie in self.enemies:
                allie.hp = allie.hp + 1

            prompt_text = f"{allie_choice.name} lançou {allie_choice.skills[attack_index].name} curando {damage} do hp da equipe "

        return prompt_text
