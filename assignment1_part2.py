#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book:
    def __init__(self, author, title):
        self.a = author
        self.t = title
        
OfMineMen = Book("John Steinbeck", "Of Mice and Men")
ToKillMock = Book("Harper Lee", "To Kill a Mickingbird")

def display(Book):
    print(Book.t + ", written by " + Book.a)
    

display(OfMineMen)
display(ToKillMock)

