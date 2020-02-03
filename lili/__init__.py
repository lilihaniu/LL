'''
Created on 2018Äê7ÔÂ17ÈÕ

@author: Jerry
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.test = 'hello,world!'

    def out_wo (self):
        print(self.test)

if __name__ == '__main__':
    obj_spider = MyClass()
    obj_spider.out_wo()
