from utils.enums.SkillType import SkillType
import utils.Config as config
from utils.DiceRow import DiceRow
import pygame


class DamageCalculateService():
    def AttackDamage(self, attack_index, chosen_striker, chosen_defender, team_striker, team_defender, equipment = None):
        # verify striker and attack selected
        out_of_mana_text = ""

        if chosen_striker is None:
            return "Você precisa selecionar o aliado, você perdeu a vez"

        if attack_index is None:
            return "Você precisa selecionar o ataque, você perdeu a vez"
        
        skill = chosen_striker.skills[attack_index]

        # verify dead attacker
        if chosen_striker.dead == True:
            return "O personagem escolhido está morto, você perdeu a vez"

        # verify mp
        if chosen_striker.mp < skill.mp and attack_index != 0:
            attack_index = 0
            out_of_mana_text = "MP insuficiente para a habilidade, foi selecionado o ataque básico. "
        
        skill = chosen_striker.skills[attack_index]
        chosen_striker.mp = chosen_striker.mp - skill.mp

        # verify stamina
        chosen_striker.st = chosen_striker.st -1

        if chosen_striker.st <= 0:
            chosen_striker.hp = chosen_striker.hp - 1
            chosen_striker.st = 10

        ## calculate damage for direct skill type ##
        if skill.skillType == SkillType.DIRECTD6 or skill.skillType == SkillType.DIRECTD12 or skill.skillType == SkillType.DIRECTD20:
            if skill.skillType == SkillType.DIRECTD6:
                dice_row = DiceRow.dice6()

            if skill.skillType == SkillType.DIRECTD12:
                dice_row = DiceRow.dice12()

            if skill.skillType == SkillType.DIRECTD20:
                dice_row = DiceRow.dice20()

            damage = (skill.damage + dice_row) - chosen_defender.defense

            if damage < 0:
                damage = 0

            chosen_defender.hp = chosen_defender.hp - damage
            prompt_text = f"{out_of_mana_text}{chosen_striker.name} usou a habilidade {skill.name}, causando {damage} de dano em {chosen_defender.name}"

        ## calculate damage for area skill type ##
        if skill.skillType == SkillType.AREAD6 or skill.skillType == SkillType.AREAD12 or skill.skillType == SkillType.AREAD20:
            if skill.skillType == SkillType.AREAD6:
                dice_row = DiceRow.dice6()
            if skill.skillType == SkillType.AREAD12:
                dice_row = DiceRow.dice12()
            if skill.skillType == SkillType.AREAD20:
                dice_row = DiceRow.dice20()

            for defender in team_defender:
                damage = (skill.damage + dice_row) - defender.defense
                if damage < 0:
                    damage = 0
                defender.hp = defender.hp - damage

            prompt_text = f"{chosen_striker.name} usou a habilidade {skill.name}, causando {damage} de dano em área"

        ## calculate damage for heal skill type ##
        if skill.skillType == SkillType.HEALD6 or skill.skillType == SkillType.HEALD12 or skill.skillType == SkillType.HEALD20:
            if skill.skillType == SkillType.HEALD6:
                dice_row = DiceRow.dice6()
            if skill.skillType == SkillType.HEALD12:
                dice_row = DiceRow.dice12()
            if skill.skillType == SkillType.HEALD20:
                dice_row = DiceRow.dice20()

            heal_points = skill.damage + dice_row

            for striker in team_striker:
                if striker.dead == False:
                    striker.hp = striker.hp + heal_points

                prompt_text = f"{chosen_striker.name} usou a habilidade {skill.name} restaurando {heal_points} de hp de sua equipe"

        ## calculate damage for mana steal type ##
        if skill.skillType == SkillType.MANASTEALD6 or skill.skillType == SkillType.MANASTEALD12 or skill.skillType == SkillType.MANASTEALD20:
            if skill.skillType == SkillType.MANASTEALD6:
                dice_row = DiceRow.dice6()
            if skill.skillType == SkillType.MANASTEALD12:
                dice_row = DiceRow.dice12()
            if skill.skillType == SkillType.MANASTEALD20:
                dice_row = DiceRow.dice20()

            mana_points = skill.damage + dice_row

            if mana_points < 0:
                mana_points = 0

            for defender in team_defender:
                defender.mp = defender.mp - mana_points

                prompt_text = f"{chosen_striker.name} usou a habilidade {skill.name} removendo {mana_points} de mp"

        ## calculate damage for mana regen type ##
        if skill.skillType == SkillType.MANAREGEND6 or skill.skillType == SkillType.MANAREGEND12 or skill.skillType == SkillType.MANAREGEND20:
            if skill.skillType == SkillType.MANAREGEND6:
                dice_row = DiceRow.dice6()
            if skill.skillType == SkillType.MANAREGEND12:
                dice_row = DiceRow.dice12()
            if skill.skillType == SkillType.MANAREGEND20:
                dice_row = DiceRow.dice20()

            mana_points = skill.damage + dice_row

            if mana_points < 0:
                mana_points = 0

            for striker in team_striker:
                if striker.dead == False:
                    striker.mp = striker.mp + mana_points

                prompt_text = f"{chosen_striker.name} usou a habilidade {skill.name} restaurando {mana_points} de mana de sua equipe "

        # set all hp to 0
        for defender, striker in zip(team_defender, team_striker):
            if defender.hp < 0:
                defender.hp = 0
            if defender.mp < 0:
                defender.mp = 0
            if striker.hp < 0:
                striker.hp = 0
            if striker.mp < 0:
                striker.mp = 0

        song= pygame.mixer.Sound(skill.sfx)
        song_volume = (config.volume - 15) / 100
        if song_volume <= 0:
            song_volume = 0.10
        song.set_volume(song_volume)
        song.play()

        return prompt_text

    def PotionHeal(self, chosen_striker):

        if chosen_striker.inventory.potion > 0:
            chosen_striker.hp = chosen_striker.hp + 45
            chosen_striker.mp = chosen_striker.mp + 30
            chosen_striker.inventory.potion -= 1
            prompt_text = f"{chosen_striker.name} usou uma poção de cura restaurando 45 de hp e 30 mp"
        else:
            prompt_text = f"{chosen_striker.name} não possui nenhuma poção, você perdeu a vez"


        return prompt_text


        
