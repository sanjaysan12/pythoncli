class Argument:
    def __init__(self,arg):
        self.commands = []
        self.options = []
        self.options_values = {}
        self.arg = arg
        # print(self.arg)

        for arg in self.arg:
            if "-" in arg:
                if "=" in arg:
                    option = arg.split("=")
                    self.options.append(option[0])
                    self.options_values[option[0]] = option[1]
                    # print(self.options_values)
                else:
                    self.options.append(arg)
                    
            else:
                self.commands.append(arg)
                
    
    def hasOptions(self,options: list):
        useroptions = set(self.options)
        reqoptions = set(options)
        return list(reqoptions & useroptions)
    
    def hasCommands(self,commands: list):
        usercommand = set(self.commands)
        reqcommand = set(commands)
        return list(reqcommand & usercommand)
    
    def hasCommand(self,command):
        return command in self.hasCommands([command])
    
    def hasOptionValue(self, option):
        return option in self.options_values

    
    def hasOption(self,option):
        return option in self.hasOptions([option])
    
    def getOptionValue(self,option,default=None):
        if option in self.options_values:
            return self.options_values[option]
        else:
            default
    