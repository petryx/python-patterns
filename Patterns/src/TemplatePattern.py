'''
Created on 23/06/2013

@author: ultrathin
'''
class AbstractReport(object):
    report = {}
    def __init__(self, *args, **kwargs):
        if self.__class__ is AbstractReport:
            raise NotImplementedError('abstract class cannot be instantiated')

    def head(self, *args, **kwargs):
        raise NotImplementedError('abstract class cannot be instantiated')
    
    def body(self, *args, **kwargs):
        raise NotImplementedError('abstract class cannot be instantiated')

    def footer(self, *args, **kwargs):
        raise NotImplementedError('abstract class cannot be instantiated')
    
    def show(self):
        try:
            print self.report['head']
            print self.report['body']
            print self.report['footer']
        except KeyError as error:
            
            
            if error.message == 'head':
                raise TypeError('abstract class not implemented head')
            elif error.message == 'body':
                raise TypeError('abstract class not implemented body')
            elif error.message == 'footer':
                raise TypeError('abstract class cannot implement footer')
        
class FinancialReport(AbstractReport):
    
    
    def head(self,title):
        self.report['head'] = title
        
    def body(self,body):
        self.report['body']= body
    
#    def show(self, *args, **kwargs):
#        self.head('Financial Report')
#        self.body("Year 2009= $ 5.000.000,00\nYear 2010= $ -5.000.000,00\Total $ 0.00")
        
        
    
finac = FinancialReport()
finac.head('Financial Report')
finac.body("Year 2009= $ 5.000.000,00\nYear 2010= $ -5.000.000,00\Total $ 0.00")
finac.show()