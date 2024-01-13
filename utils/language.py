class Language: 
    def set_lang(self, lang):
        dictionary_eng = {
                        #main_menu 
                        #Main Menu
                        'play': 'Play',
                        'options': 'Options',
                        'how_to_play' : "How to play",
                        'exit': 'Exit',
                        #Play Screen
                        'save_game' : 'Save game',
                        'continue' : 'Continue',
                        'load_game' : 'Load game',
                        'new_game' : 'New game' ,
                        #Options Screen
                        'volume': 'Volume',
                        'menu_text_language': 'Language',
                        'apply': 'Apply',
                        #How To Play Screen
                        'Next' : 'Next',
                        'Previous' : 'Previous',
                        #campaing
                        'campaing_text_explore': 'Explore',
                        'campaing_text_level': 'Level'
                        }

        dictionary_pt = {
                        #main_menu
                        'play': 'Iniciar',
                        'options': 'Opções',
                        'how_to_play' : "Como jogar",
                        'exit': 'Sair',
                        #play screen
                        'save_game' : 'Salvar jogo',
                        'continue' : 'Continuar',
                        'load_game' : 'Carregar jogo',
                        'new_game' : 'Novo jogo' ,
                        #Options Screen
                        'volume': 'Volume',
                        'menu_text_language': 'Linguagem',
                        'apply': 'Aplicar',
                        #How To Play Screen
                        'Next' : 'Próximo',
                        'Previous' : 'Anterior',
                        #campaing
                        'campaing_text_explore': 'Explorar',
                        'campaing_text_level': 'Andar'
                        }

        if lang == 'English':
            return dictionary_eng
        
        if lang == 'Português-Brasil':
            return dictionary_pt