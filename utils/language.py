class Language: 
    def set_lang(self, lang):
        dictionaryeng = {
                        'menu_text_play': 'Play',
                        'menu_text_options': 'Options',
                        'menu_text_exit': 'Exit',
                        'menu_text_resolution': 'Resolution',
                        'menu_text_volume': 'Volume',
                        'menu_text_language': 'Language',
                        'menu_text_apply': 'Apply'
                        }

        dictionarypt = {
                        'menu_text_play': 'Iniciar',
                        'menu_text_options': 'Opções',
                        'menu_text_exit': 'Sair',
                        'menu_text_resolution': 'Resolução',
                        'menu_text_volume': 'Volume',
                        'menu_text_language': 'Linguagem',
                        'menu_text_apply': 'Aplicar'
                        }

        if lang == 'eng':
            return dictionaryeng
        
        if lang == 'pt':
            return dictionarypt