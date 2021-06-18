# jurassic3
## Problem Statement
This time, Jurassic Park's t-rex is secretly requesting that you free it from its cage. It tells you that the cage is protected by a flag, and gives you the source code.

Nothing bad can happen if you find the right flag, right?

## Solution
The flag is first converted to hex, then shifted by 10 characters. To reverse this, shift the flag back 10 characters, then convert it from hex back into text.

See `solution.py` for a full solution.

## Flag
`flag{t-rex_has_escaped}`
