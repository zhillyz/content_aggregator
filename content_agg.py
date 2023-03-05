from abc import ABC, abstractmethod
import praw
import os

class Source(ABC):
    ''' base source class which will be inherited by different source child
    classes such as Reddit etc'''
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def fetch(self):
        pass