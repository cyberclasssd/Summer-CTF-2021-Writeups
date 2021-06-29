# jurassic4
## Problem Statement
With a t-rex on the loose, you need to stop it! Luckily, you remember a trap that you previously set to stop any dinosaur in their tracks. You run to the trap, and you realize that it needs a passphrase to use.

Quick, get the passphrase before it's too late!

## Solution
The flag is first encoded with BASE64 (to do this, the flag is encoded to ASCII bytes, encoded with base 64, and then decoded from ASCII bytes), then shifted by 13 characters. To reverse this, shift the flag back 13 characters, then decode the flag using BASE64.

See `solution.py` for a full solution.

## Flag
`flag{y0u'v3_act1vat3d_my_trap_card!}`
