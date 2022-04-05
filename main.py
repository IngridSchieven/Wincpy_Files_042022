__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#makedirs = multiple directories
#mkdir = single one

#1. def clean_cache
#   creating empty folder named cache
from gettext import find
import os
import shutil
#from distutils.command.clean import clean > deze kwam voorbij na error!!??

#versie 1
def clean_cache():
    cwd = os.getcwd()                               #cwd = Winc
    #new_path_files = os.path.join(cwd, 'files')     #new_path_files = Winc/files
    print(cwd)                                      #check = Winc, better use pwd?
    #print(new_path_files)                           #check = Winc/files
    os.chdir(cwd)
    if os.path.exists('cache'):
       shutil.rmtree('cache')
    os.mkdir('cache')

clean_cache()

#2 cache_zip
#import zipfile #nb. extractall gebruiken, zie studytonight how-to-unzip

def cache_zip(zip_file_path, cache_dir_path):               #two arguments
    clean_cache()
    shutil.unpack_archive(zip_file_path, cache_dir_path)

#    unzipped_files = zipfile.ZipFile(zip_file_path, 'r')    #r = read
#    unzipped_files.extractall(cache_dir_path)               #zie studytonight web

cache_zip('./data.zip', './cache')                          #two arguments


#3 cached_files
def cached_files(): #no arguments
                    #returns a list of all files in the cache in ABSOLUTE terms
                    #absolute path = full path to some place on your computer
                    #relative path = path to some file
                    #cwd + relative path = abs
    list_of_all_files_in_cache = []                     #bron stackoverflow 9816816
    for folder, subs, files in os.walk('./cache'):
        for filename in files:
            list_of_all_files_in_cache.append(os.path.abspath(os.path.join(folder, filename)))
    return list_of_all_files_in_cache
    #print(list_of_all_files_in_cache)
cached_files()            

#aantekeningen bij opdracht #3  
    #file_list = os.listdir('.')
    #abs = os.path.abs.path('.')
    #from pathlib import Path 

#4 find_password
#function should read text IN each one to see if password is in there
#return #password in str

def find_password(list_of_all_files_in_cache): 
    for file in list_of_all_files_in_cache:
        with open(file, 'r') as f:            #bron StackOverflow 44694869 
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    #password = line.split(' ', 1)[1] 
                    #password = line.split('_')[1:]
                    #\n verwijderen str.strip() 
                    password = line.partition(' ')[2]  #regel splitten
                    #password = re.sub('/w', ' ', password)
                    #print(password)#.replace('_', ' '))  #realpython documentatie
                    return password.strip()  #deze  \n had ik zelf nooit kunnen bedenken, mbv Jelmer opgelost                            
print(find_password(cached_files())) 

