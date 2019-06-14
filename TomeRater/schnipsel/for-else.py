#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:14:51 2019

@author: ben
"""
 def add_user(name, email, user_books=None):
    tlds = [".com", ".edu", ".org"]
    for i in tlds:
            if i in email:
                return User(name, email)
    else:
        