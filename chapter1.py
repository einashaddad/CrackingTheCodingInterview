#!/usr/bin/python
# -*- coding: utf-8 -*- 

'''
Implement an algorithm to determine if a string has all unique characters What if you 
can not use additional data structures?
'''

import string

def all_unique(s):
    all_the_letters = string.letters[:26]
    dictionary = [letter for letter in all_the_letters]
    for i, letter in enumerate(s):
        if letter in dictionary:
            dictionary.remove(letter)
        else:
            return False
    return True

#print all_unique('abcdef')

'''
Write a method to decide if two strings are anagrams or not 
'''

def anagrams(str1, str2):
    for letter in str1:
        if letter not in str2:
            return False
    for letter in str2:
        if letter not in str1:
            return False
    return True

#print anagrams('mary', 'armys')

'''
Write a method to replace all spaces in a string with ‘%20’ 
'''

def replace_spaces(s):
    letters = s.split(' ')
    return ('%20').join(letters)

#print replace_spaces('this is a string')

'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees Can you do this in place?
'''

def rotate_90_clockwise(mat):
    n = len(mat[0])
    mat.reverse()
    new_mat = [[] for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            new_mat[i].append(mat[j][i])

    return new_mat


# mat = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]

# print rotate_90_clockwise(mat)


