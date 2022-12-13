import readline

class session(object):
    def __init__(self, complete_state):
        self.complete_state = sorted(complete_state)
    def readlike(self, text, state):
        if state == 0:
            if text:
                self.current = [stat for stat in self.complete_state if stat and stat.startswith(text)]
            else:
                self.current = self.complete_state[:] # disini atur readlike ... 
        try: 
            return self.current[state]
        except IndexError:
            return None
    @classmethod
    def prompt_readlike(self, inputer : str , completer  : list , keybind : None):
        """ 
        note : lebih enak kalau di buat class lagi ...
        ---------
        1. inputer: >>> session.prompt_readlike(inputer='<bebas>')
        2. completer: >>> session.prompt_readlike(...,completer=[list: <bebas>] )
        3. keybind: >>> session.prompt_readlike(...,..., keybind='<bebas>')
           |__ 1. tab
               2. space
               3. ctrl -> c 
               4. escape
               5. enter 
               6. dll 
        """
        readline.set_completer(session(complete_state=completer).readlike)
        readline.parse_and_bind(f'{keybind}: complete')
        self.inputer = inputer
        self.completer = completer
        self.keybind = keybind
        return self.cursor_(inputer)
    @staticmethod
    def cursor_(prompt):
        try:
            getcursor = input(prompt)
            return getcursor
        except (KeyboardInterrupt): raise SystemExit(1)
        except (EOFError): raise SystemExit(1)


