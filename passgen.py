#!/usr/bin/python

#Written in Python 2.7 syntax

#Passgen is a random password generator

#Features to implement:
#Feature name - Implemented(X)
#-Generate a random password (X)
#-Set a default pw length  (X)
#-Allow user to specify pw length  (X)
#-Set a default number of pw to generate  (X)
#-Allow user to specify number of pw to generate  (X)
#-Allow user to specify upper/lower/both cases  (X)
#-Allow user to specify use of special characters  (X)
#-Allow user to specify no similar characters
#-Allow user to specify how many times a character is repeated
#-Allow user to seed with input
#-Allow user to print phonetics as an option


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
#def_pw_case = "both"
#Use special characters
#def_pw_spec = "no"
#Use similar characters (0 & O, etc)
#def_pw_sim = "no"
#How many times to reuse a character in a password
#def_pw_rep = "2"
#Use a user supplied seed?
#def_pw_seed = "no"
#Print phonetics for passwords?
def_pw_phon = "no"

#Get user input
pw_len = raw_input("How long do you want your password to be? (Default: 8): ")
pw_num = raw_input("How many passwords would you like to generate? (Default: 10): ")
pw_case = raw_input("What case should letters be in? Choices are: lower, upper, both. (Default: both): ")
pw_spec = raw_input("Do you want to use special characters? (Default: no): ")
#pw_sim = raw_input("Do want to use similar characters? (Default: no): ")
#pw_rep = raw_input("What is the maximum you want any charachter to be repeated? (Default: 2): ")
#pw_seed = raw_input("Do you want to use a seed to generate your password? (Default: no): ")
#set_pw_seed = raw_input("Please enter your seed: ")
pw_phon = raw_input("Do you want to print password phonetics? (Default: no): ")

#Password resource lists
pw_lower_lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#Be efficient and generate pw_upper_lst from pw_lower_lst
pw_upper_lst = []
for each in pw_lower_lst:
    each = each.upper()
    pw_upper_lst.append(each)
#pw_upper_lst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
pw_num_lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pw_spec_lst = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "<", ">", ",", ".", "?"]

#Phonetics dictionary
#pw_lower_desc = {"a": "alpha", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo", "f": "foxtrot", "g": "golf", "h": "hotel", "i": "india", "j": "juliett", "k": "kilo", "l": "lima", "m": "mike", "n": "november", "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra", "t": "tango", "u": "uniform", "v": "victor", "w": "whiskey", "x": "x-ray", "y": "yankee", "z": "zulu"}

#Be lazy and generate pw_upper_desc from pw_lower_desc
#pw_upper_desc = []
#for each in pw_lower_desc:
#    each = each.upper()
#    pw_upper_desc.append(each)
#print pw_upper_desc
#pw_upper_desc = {"A": "ALPHA", "B": "BRAVO", "C": "CHARLIE", "D": "DELTA", "E": "ECHO", "F": "FOXTROT", "G": "GOLF", "H": "HOTEL", "I": "INDIA", "J": "JULIETT", "K": "KILO", "L": "LIMA", "M": "MIKE", "N": "NOVEMBER", "O": "OSCAR", "P": "PAPA", "Q": "QUEBEC", "R": "ROMEO", "S": "SIERRA", "T": "TANGO", "U": "UNIFORM", "V": "VICTOR", "W": "WHISKEY", "X": "X-RAY", "Y": "YANKEE", "Z": "ZULU"}
#pw_num_desc = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8":"Eight", "9": "Nine"}
#pw_spec_desc = {"`": "BackQuote", "~": "Tildy", "!": "ExclimationPoint", "@": "At", "#": "Hash", "$": "DollarSign", "%": "Percent", "^": "Carrot", "&": "Ampersand", "*": "Astrix", "(": "LeftPerentheses", ")": "RightPerentheses", "-": "Minus", "_": "Underscore", "=": "Equals", "+": "Plus", "<": "LessThan", ">": "MoreThan", ",": "Comma", ".": "Period", "?": "QuestionMark"}

pw_phon_desc = {"a": "alpha", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo", "f": "foxtrot", "g": "golf", "h": "hotel", "i": "india", "j": "juliett", "k": "kilo", "l": "lima", "m": "mike", "n": "november", "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra", "t": "tango", "u": "uniform", "v": "victor", "w": "whiskey", "x": "x-ray", "y": "yankee", "z": "zulu", "A": "ALPHA", "B": "BRAVO", "C": "CHARLIE", "D": "DELTA", "E": "ECHO", "F": "FOXTROT", "G": "GOLF", "H": "HOTEL", "I": "INDIA", "J": "JULIETT", "K": "KILO", "L": "LIMA", "M": "MIKE", "N": "NOVEMBER", "O": "OSCAR", "P": "PAPA", "Q": "QUEBEC", "R": "ROMEO", "S": "SIERRA", "T": "TANGO", "U": "UNIFORM", "V": "VICTOR", "W": "WHISKEY", "X": "X-RAY", "Y": "YANKEE", "Z": "ZULU", "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8":"Eight", "9": "Nine", "`": "BackQuote", "~": "Tildy", "!": "ExclimationPoint", "@": "At", "#": "Hash", "$": "DollarSign", "%": "Percent", "^": "Carrot", "&": "Ampersand", "*": "Astrix", "(": "LeftPerentheses", ")": "RightPerentheses", "-": "Minus", "_": "Underscore", "=": "Equals", "+": "Plus", "<": "LessThan", ">": "MoreThan", ",": "Comma", ".": "Period", "?": "QuestionMark"}

#Diag
#print pw_lower_lst
#print pw_upper_lst
#print pw_num_lst
#print pw_spec_lst
#print pw_lower_desc
#print pw_upper_desc
#print pw_num_desc
#print pw_spec_desc

# Check for user specified values, if none given use defaults, if given change to int where appropriate.
if pw_len == "":
    pw_len = def_pw_len
else:
    pw_len = int(pw_len)

if pw_num == "":
    pw_num = def_pw_num
else:
    pw_num = int(pw_num)

# Note, if the option is blank or "both" then nothing is done.
pw_case = pw_case.lower()
if pw_case == "upper":
    pw_lower_lst = []
elif pw_case == "lower":
    pw_upper_lst = []

#Note, if the option is "yes" then nothing is done.
pw_spec = pw_spec.lower()
if pw_spec == "" or pw_spec == "no":
    pw_spec_lst = []

#if pw_sim == "":
#    pw_sim = def_pw_sim
    
#if pw_rep == "":
#    pw_rep = def_pw_rep

#if pw_seed == "":
#    pw_seed = def_pw_seed

pw_phon == pw_phon.lower()

# Save some things for future reference here
pw_len_orig = pw_len


# Make a password
while pw_num >= 1:
    password_lst = []
    while pw_len >= 1:
        x = random.choice(pw_lower_lst + pw_upper_lst + pw_num_lst + pw_spec_lst)
        password_lst.append(x)
        pw_len -= 1
    password = string.join(password_lst)
    print "Password %s is: %s" %(pw_num, password.replace(" ", ""))
    if pw_phon == "yes":
        password_phon = []
        for each in password_lst:
            password_phon.append(pw_phon_desc[each])
        phonetics = string.join(password_phon)
        print "Password %s phonetics are: %s" %(pw_num, phonetics)
    pw_len = pw_len_orig
    pw_num -= 1



#Useful info:
#random.choice(string.ascii_letters + string.digits)

