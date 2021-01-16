from itertools import product
from main import MD5Crypt
import string


def try_pass(pass_list):
    magic = "$1$"
    salt = "4fTgjp6q" # team 41
    found_pw = ""
    print("Checking pw's, please wait..")
    for pw in pass_list:
        md5 = MD5Crypt()
        '''
        print(md5.calc_hash(pw, salt, magic))
        print("$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1")
        print("magic")
        '''
        #print(md5.calc_hash(pw, salt, magic))
        if md5.calc_hash(pw, salt, magic) == "$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1":
            found_pw = pw
            print("found result! " + found_pw)
            return found_pw
    if found_pw == "":
        print("not found in length: " + str(len(pass_list[0])))
    print("done checking pw's..... ")
    return found_pw

def try_onepass(one_word):
    md5 = MD5Crypt()
    magic = "$1$"
    salt = "4fTgjp6q" # team 41
    found_pw = ""

    print("\n\nChecking one pw, please wait..")
    '''
        print(md5.calc_hash(pw, salt, magic))
        print("$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1")
        print("magic")
    '''
    #print(md5.calc_hash(one_word, salt, magic))
    if md5.calc_hash(one_word, salt, magic) == "$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1":
        found_pw = one_word
        print("found result! " + found_pw)
        return found_pw
    if found_pw == "":
        print("not found in your string: " + one_word)
    print("done checking pw's..... ")
    return found_pw

def generate_pws():
        pw_found = "" #storing pw here

        low_ascii = string.ascii_lowercase
        '''
        pw_list = []
        # trying all single char
        for x in product(low_ascii, repeat=1):
            pw_list.append(x[0])
        pw_found = try_pass(pw_list)
        if pw_found != "":
            return pw_found
        pw_list = []
        # empty then try 2 chars
        for x in product(low_ascii, repeat=2):
            pw_list.append(x[0] + x[1])
        pw_found = try_pass(pw_list)
        if pw_found != "":
            return pw_found
        pw_list = []
        # empty then try 3 chars
        for x in product(low_ascii, repeat=3):
            pw_list.append(x[0] + x[1] + x[2])
        pw_found = try_pass(pw_list)
        if pw_found != "":
            return pw_found
        pw_list = []
        # empty then try 4 chars
        for x in product(low_ascii, repeat=4):
            pw_list.append(x[0] + x[1] + x[2] + x[3])
        pw_found = try_pass(pw_list)
        if pw_found != "":
            return pw_found
        '''
        '''
        pw_list = []
        # empty then try 5 chars
        for x in product(low_ascii, repeat=5):
            pw_list.append(x[0] + x[1] + x[2] + x[3] + x[4])
        pw_found = try_pass(pw_list)
        #print(pw_list)
        if pw_found != "":
            return pw_found
        '''

        pw_list = []
        print("Checking 6 char  ")
        # empty then try 6 chars

        loop_pw = ""
        success = ""
        for x in product(low_ascii, repeat=6):
            loop_pw = ''.join(x)
            success = try_onepass(loop_pw)
            if success:
                print("password is: " + success)
                return success

        if pw_found != "":
            return pw_found

        return pw_found


if __name__ == "__main__":
    print("found: " + generate_pws())