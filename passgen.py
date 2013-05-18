#!/usr/bin/python

#Written in Python 2.7 syntax

#Passgen is a random password generator

#Features to implement:
#Feature name - Implemented(X)
#-Generate a random password
#-Set a default pw length
#-Allow user to specify pw length
#-Set a default number of pw to generate
#-Allow user to specify number of pw to generate
#-Allow user to specify upper/lower/both cases
#-Allow user to specify use of special characters
#-Allow user to specify no similar characters
#-Allow user to specify how many times a character is repeated
#-Allow user to seed with input


print "Welcome to Passgen!"

#Imports
import string
import random

#Set variable defaults
# Length of passwords
def_pw_len = 8
# Number of passwords to create
def_pw_num = 10
#Use upercase, lowercase, or both
def_pw_case = "both"
#Use special characters
def_pw_spec = "no"
#Use similar characters (0 & O, etc)
def_pw_sim = "no"
#How many times to reuse a character in a password
def_pw_rep = "2"
#Use a user supplied seed?
#def_pw_seed = "no"

#Get user input
pw_len = raw_input("How long do you want your password to be? (Default: 8): ")
pw_num = raw_input("How many passwords would you like to generate? (Default: 10): ")
pw_case = raw_input("What case should letters be in? Choices are: lower, upper, both. (Default: both): ")
pw_spec = raw_input("Do you want to use special characters? (Default: no): ")
pw_sim = raw_input("Do want to use similar characters? (Default: no): ")
pw_rep = raw_input("What is the maximum you want any charachter to be repeated? (Default: 2): ")
#pw_seed = raw_input("Do you want to use a seed to generate your password? (Default: no): ")
#set_pw_seed = raw_input("Please enter your seed: ")

#Password resource lists
pw_lower_lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pw_upper_lst = pw_lower.upper()
pw_spec_lst = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "-", "=", "+", "<", ">", ",", ".", "?"]

#Diag
print pw_lower_lst
print pw_upper_lst
print pw_spec_lst

#Useful info:
#random.choice(string.ascii_letters + string.digits)

