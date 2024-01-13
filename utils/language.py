class Language: 
    def set_lang(self, lang):
        dictionary_eng = {
                        #main_menu
                        'menu_text_play': 'Play',
                        'menu_text_options': 'Options',
                        'menu_text_exit': 'Exit',
                        'menu_text_resolution': 'Resolution',
                        'menu_text_volume': 'Volume',
                        'menu_text_language': 'Language',
                        'menu_text_apply': 'Apply',
                        #campaing
                        'campaing_text_explore': 'Explore',
                        'campaing_text_level': 'Level'
                        }

        dictionary_pt = {
                        #main_menu
                        'menu_text_play': 'Iniciar',
                        'menu_text_options': 'Opções',
                        'menu_text_exit': 'Sair',
                        'menu_text_resolution': 'Resolução',
                        'menu_text_volume': 'Volume',
                        'menu_text_language': 'Linguagem',
                        'menu_text_apply': 'Aplicar',
                        #campaing
                        'campaing_text_explore': 'Explorar',
                        'campaing_text_level': 'Andar'
                        }

        if lang == 'eng':
            return dictionary_eng
        
        if lang == 'pt':
            return dictionary_pt