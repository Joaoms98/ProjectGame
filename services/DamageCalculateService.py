from utils.enums.SkillType import SkillType

class DamageCalculateService():
    def AttackDamage(self, attack_index, chosen_striker, chosen_defender, team_striker, team_defender):
        damage = 5
        skill = chosen_striker.skills[attack_index]        

        # verify dead attacker
        if chosen_striker.dead == True:
            return "O personagem escolhido está morto"

        # verify stamina
        chosen_striker.st = chosen_striker.st -1

        if chosen_striker.st <= 0:
            chosen_striker.hp = chosen_striker.hp - 1
            chosen_striker.st = 10

        # calculate damage for direct skill type
        if skill.skillType == SkillType.DIRECT:
            chosen_defender.hp = chosen_defender.hp - damage
            prompt_text = f"{chosen_striker.name} atacou com o ataque {skill.name}, causando {damage} de dano no {chosen_defender.name}"

        # calculate damage for area skill type
        if skill.skillType == SkillType.AREA:
            for defender in team_defender:
                defender.hp = defender.hp - damage

            prompt_text = f"{chosen_striker.name} lançou {skill.name} causando {damage} de dano em area"

        # calculate damage for heal skill type
        if skill.skillType == SkillType.HEAL:
            for striker in team_striker:
                if striker.dead == False:
                    striker.hp = striker.hp + 1

            prompt_text = f"{chosen_striker.name} lançou {skill.name} curando o hp de sua equipe "

        # set all hp to 0
        for defender in team_defender:
            if defender.hp < 0:
                defender.hp = 0

        for striker in team_striker:
            if striker.hp < 0:
                striker.hp = 0

        return prompt_text
