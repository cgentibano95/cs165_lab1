from itertools import product
import hashlib
import binascii


class MD5Crypt:

    def to64(self, hash, n):
        ret = ""
        base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for i in range(n):
            ret += base64[hash&0x3f]
            hash >>= 6
        return ret

    def compute_alt(self, pw, salt):
        # computes alternate sum and returns as hex
        # compare with hex soln
        return hashlib.md5(pw.encode() + salt.encode() + pw.encode()).hexdigest()

    def compute_intermediate(self, pw, magic, salt):
        intermediate = (pw + magic + salt).encode('utf-8')
        alt = self.compute_alt(pw, salt)
        pw_len = len(pw)

        # need to convert alternate (hex string) to binary representation
        # if not converted, adding to intermediate will not work
        bin_alt = binascii.unhexlify(alt)
        while pw_len > 0:
            intermediate += bin_alt[0:min(16, pw_len)]
            pw_len -= 16

        pw_len = len(pw)
        while pw_len != 0:
            if pw_len & 1:
                # if bit is set, append NUL byte
                # will append character 0
                intermediate += chr(0).encode('utf-8')
            else:
                # if unset, append first byte of the pw
                intermediate += pw[0].encode('utf-8')
            pw_len >>= 1

        # intermediate calculate
        return hashlib.md5(intermediate).digest()

    # loop function will loop 1000 times to stretch algo
    def loop(self, intermediate, pw, salt):
        if isinstance(intermediate, str) == 1:
            intermediate += intermediate.encode('utf-8')

        for i in range(1000):
            new_inter = b''
            # if even/odd
            if i%2 == 0:
                new_inter += intermediate
            else:
                new_inter += pw.encode()
            if i%3 != 0:
                new_inter += salt.encode()
            if i%7 != 0:
                new_inter += pw.encode()
            # if even/odd
            if i%2 == 0:
                new_inter += pw.encode()
            else:
                new_inter += intermediate
            intermediate = hashlib.md5(new_inter).digest()
        # we now have new intermediate 1000, returns hex
        return intermediate

    def finalize(self, h):
        return self.to64((h[0] << 16) | (h[6] << 8) | (h[12]), 4) \
               + self.to64((h[1] << 16) | (h[7] << 8) | (h[13]), 4) \
               + self.to64((h[2] << 16) | (h[8] << 8) | (h[14]), 4) \
               + self.to64((h[3] << 16) | (h[9] << 8) | (h[15]), 4) \
               + self.to64((h[4] << 16) | (h[10] << 8) | (h[5]), 4) \
               + self.to64(h[11], 2)

    def calc_hash(self, pw, salt, magic):

        interm = self.compute_intermediate(pw, magic, salt)
        base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        loop_interm = self.loop(interm, pw, salt)
        b64_ret = self.finalize(loop_interm)

        final_hash = magic + salt + '$' + b64_ret
        return final_hash


if __name__ == '__main__':

    pw = "zhgnnd"
    salt = "hfT7jp2q"
    magic = "$1$"
    # above provided for testing from slides
    md5 = MD5Crypt()
    # test alt
    altsum = md5.compute_alt(pw,salt)
    test_alt = b'\x3f\xfc\x86\xe7\xc7\x8f\x47\xa8\x16\x4f\xe2\x85\xc0\xfa\x22\x55'
    print(altsum == test_alt.hex())
    #print(altsum)
    # testing alt works

    test_inter = b'\xed\x7a\x53\x07\x58\x8e\x49\xed\x3a\x27\x77\xd9\x26\xd6\x2f\x96'
    ret_interm = md5.compute_intermediate(pw, magic, salt)
    print(ret_interm)
    print(ret_interm == test_inter)

    test_loop = b'\xff\x20\x2f\x2e\x9b\x6a\xc6\xe4\x95\x57\x05\x36\xfc\x89\xfd\x2a'

    ret_loop = md5.loop(test_inter, pw, salt)
    print(test_loop.hex() == ret_loop.hex())

    test_soln = '$1$hfT7jp2q$wPwz7GC6xLt9eQZ9eJkaq.'
    print("wPwz7GC6xLt9eQZ9eJkaq")
    hash_val = md5.calc_hash(pw, salt, magic)
    print("test soln = " + test_soln)
    print(hash_val)
    print(test_soln == hash_val)






