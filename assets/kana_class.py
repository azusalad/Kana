class kana:
    def __init__(self, key, values, pp):
        self.key = key
        self.values = values
        self.pp = pp
        
    def __str__(self):
        return(f'Kana with key: {self.key}, values: {self.values}, pp: {self.pp}')
    
    
    def alter_pp(self, result, answer_time, average_time):
        """Alter performance points based on the result and time taken."""
        import config
        
        # first do correct, wrong, easy stuff
            # 0 for correct
            # 1 for incorrect
            # 2 for easy
        if result == 0:
            self.pp +=  config.pp_correct
        elif result == 1:
            self.pp += config.pp_wrong
        else:
            self.pp += config.pp_easy
            
        # adjust pp based on time
        if answer_time < 0.5 * average_time and result == 0:
            self.pp += config.pp_05bonus
        elif answer_time > 1.5 * average_time:
            self.pp += config.pp_15penalty
        elif answer_time > 2 * average_time:
            self.pp += config.pp_2penalty
            
    def update_pp(self):
        """Update inactive kana."""
        import config
        self.pp += config.pp_inactive
    
