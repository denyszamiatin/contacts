class ConsoleManager(object):

    def input(self, prompt):
        return raw_input(prompt)
        
    def output(self, message):
        print message
