from utils.enums.SkillType import SkillType
from utils.DiceRow import DiceRow

class DamageCalculateService():
    def AttackDamage(self, attack_index, chosen_striker, chosen_defender, team_striker, team_defender, equipment = None):
        skill = chosen_striker.skills[attack_index]

        # verify dead attacker
        if chosen_striker.dead == True:
            return "O personagem escolhido está morto, você perdeu a vez"

        # verify stamina
        chosen_striker.st = chosen_striker.st -1

        if chosen_striker.st <= 0:
            chosen_striker.hp = chosen_striker.hp - 1
            chosen_striker.st = 10

        # calculate damage for direct skill type
        if skill.skillType == SkillType.DIRECT:
            damage = (skill.damage + DiceRow.dice6()) - chosen_defender.defense

            if damage < 0:
                damage = 0

            chosen_defender.hp = chosen_defender.hp - damage
            prompt_text = f"{chosen_striker.name} atacou com o ataque {skill.name}, causando {damage} de dano no {chosen_defender.name}"

        # calculate damage for area skill type
        if skill.skillType == SkillType.AREA:

            if chosen_striker.mp > skill.mp:
                chosen_striker.mp = chosen_striker.mp - skill.mp
                for defender in team_defender:
                    dice_row = DiceRow.dice6()
                    damage = (skill.damage + dice_row) - defender.defense
                    if damage < 0:
                        damage = 0

                    defender.hp = defender.hp - damage
                prompt_text = f"(Rolagem do dado: {dice_row}) {chosen_striker.name} lançou {skill.name} causando {damage} de dano em area"
            else:
                prompt_text = f"{chosen_striker.name} lançou {skill.name} porém não teve poder o suficiente "

        # calculate damage for heal skill type
        if skill.skillType == SkillType.HEAL:

            if chosen_striker.mp > skill.mp:
                chosen_striker.mp = chosen_striker.mp - skill.mp
                for striker in team_striker:
                    if striker.dead == False:
                        striker.hp = striker.hp + skill.damage

                prompt_text = f"{chosen_striker.name} lançou {skill.name} curando {skill.damage} de hp de sua equipe "
            else:
                prompt_text = f"{chosen_striker.name} lançou {skill.name} porém não teve poder o suficiente "

        # set all hp to 0
        for defender in team_defender:
            if defender.hp < 0:
                defender.hp = 0

        for striker in team_striker:
            if striker.hp < 0:
                striker.hp = 0

        return prompt_text
