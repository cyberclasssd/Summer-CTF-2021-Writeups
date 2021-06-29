# not-rsa-but-easy
## Problem Statement
The text file contains the output generated when the code is ran on the flag.
Wrap the flag in flag format (flag{XXXXXXXX}).

## Solution
The randomly generated RSA key would not be factorable in reasonable time. However, the cipher is still insecure because each letter is encoded individually, meaning that you could bash the cipher by encoding every ascii character using the same key and comparing them to each number in the output.

## Flag 
`flag{h3y!_why_d0_1_ke3p_3471ng_my_fri3nd5?}`
