from itertools import product
from main import MD5Crypt
import multiprocessing as mp
import string

# Team 41: pass= gzwbuh


def try_onepass(arg_word):
    one_word = "".join(arg_word)
    md5 = MD5Crypt()
    magic = "$1$"
    salt = "4fTgjp6q" # team 41
    found_pw = ""
    #print(one_word)
    #print(md5.calc_hash(one_word, salt, magic))
    test_soln = "4fTgjp6q$jnmk28IoEJtBYVb.kJYt.0"
    team_41_soln = "$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1"
    if md5.calc_hash(one_word, salt, magic) == "$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1":
        found_pw = one_word
        print(" found result! " + found_pw)
        return found_pw
    return found_pw


def generate_pws():

    pw_found = "" #storing pw here
    low_ascii = string.ascii_lowercase

    p = mp.Pool(processes=10)
    for x in p.imap(try_onepass, product(low_ascii, repeat=6), chunksize=10):
        if x != "":
            p.join()
            p.close()
            return x
    p.join()
    p.close()
    return pw_found


if __name__ == "__main__":


    print("\n\n\n\n\n Found result!!! Done! \n\n\n\n\n\n" + generate_pws())