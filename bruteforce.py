from itertools import product
from main import MD5Crypt
import multiprocessing as mp
import string
from timeit import default_timer as timer

# Team 41: pass = gzwbuh
# Processes used = 10
# CPU: AMD 2700x
# Candidates tested per second: ~8080-10000 per second


def try_onepass(arg_word):
    one_word = "".join(arg_word)
    md5 = MD5Crypt()
    magic = "$1$"
    salt = "4fTgjp6q" # team 41
    found_pw = ""

    #print(one_word)
    #print(md5.calc_hash(one_word, salt, magic))
    #test_soln = "4fTgjp6q$jnmk28IoEJtBYVb.kJYt.0"
    team_41_soln = "$1$4fTgjp6q$9jnkmpmGRVLiVbyM7ZRsh1"
    if md5.calc_hash(one_word, salt, magic) == team_41_soln:
        found_pw = one_word
        print(" found result! " + found_pw)
        return found_pw
    return found_pw


def generate_pws(chars_tested):
    pw_found = "" #storing pw here
    low_ascii = string.ascii_lowercase
    pw_counter = 0
    pw_time = 0
    p = mp.Pool(processes=10)
    start = timer()

    for x in p.imap(try_onepass, (product(low_ascii, repeat=chars_tested)), chunksize=10):
        pw_counter += 10 # pw counter increments by 10 since we're running 10 procs with chunksize of 10
        if x != "":
            end = timer()
            pw_time += pw_counter // (end - start)
            p.close()
            p.join()
            return x,pw_time

    # if here, we didn't find pass
    end = timer()
    print(pw_counter)
    pw_time += pw_counter // (end - start)
    p.close()
    p.join()
    return pw_found,pw_time


if __name__ == "__main__":
    chars_tested = 6 # change this int value if you want to test 1,2,3,4,5 or 6 characters.

    print("Trying to find passwords with " + str(chars_tested) + " characters")
    soln, pw_time = generate_pws(chars_tested)
    print("Candidates tested per second: " + str(pw_time))

    if soln == "":
        print("Didn't find the solution :( ")
    else:
        print("The solution is: " + soln)