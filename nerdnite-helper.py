#!/usr/bin/env python
import re
import base64

uuu="aHR0c;ovL2dvGy5nGC9mG3Jtcy95c;F;GEw4Tkx0Cg@@"

def nerdnite_helper_1(uuu):
    www=re.sub(r'@',r'=',re.sub(r';',r'D',re.sub(r'G',r'b',uuu)))
    return www

def nerdnite_helper_2(uuu):
    return base64.b64decode(uuu)

########
# MAIN #
########
def main():
    print "PLEASE VISIT THE FOLLOWING URL\n"
    print nerdnite_helper_2(nerdnite_helper_1(uuu))
    print "COPY AND PASTE THE URL INTO YOUR BROWSER. FOLLOW THE INSTRUCTIONS ONCE YOU GET THERE"
    exit( 0 )

# Execute
if __name__ == "__main__":
    main()
