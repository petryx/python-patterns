'''
Created on 23/06/2013

@author: ultrathin

Implementation to Command pattern with dinamic factory pattern
'''
class BaseCommand(object):
    def execute( self ):
        raise NotImplementedError( "Should have implemented this" )
    
class SendMailCommand(BaseCommand):
    
    def execute(self):
        print "send MAIL" 

class PrintCommand(BaseCommand):
    
    def execute(self):
        print "print command" 

class ExitCommad(BaseCommand):
    
    def execute(self):
        print "Exit command"
        
        
class FactoryCommand(object):
    factory_cmds={}
    def register(self,name,klass):
        self.factory_cmds[name] = klass
        
    def get_command(self, command_name):
        """get a command"""
        return self.factory_cmds[command_name]()
        
        
    
factoryCmd = FactoryCommand()
factoryCmd.register("send_mail", SendMailCommand)
factoryCmd.register("print", PrintCommand)
factoryCmd.register("exit", ExitCommad)

factoryCmd.get_command("print").execute()
factoryCmd.get_command("exit").execute()
factoryCmd.get_command("send_mail").execute()