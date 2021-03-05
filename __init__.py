import os

def make_user(username,password,email,aboutme):
    x = input("THIS WILL CREATE A NEW USER, ARE YOU SURE?(y/n)")
    if x == "y" or x == "Y":
        string = 'http POST http://www.amazeryogo.in/api/users username={} password={} email={} "about_me={}"'.format(username,password,email,aboutme)
        os.system(string)
        print("done!")
    else:
        pass

def get_token(username,password):
    pass
