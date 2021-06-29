# jurassic4
## Problem Statement
It's been a long day at the park. You are heading home, but before you can exit, you meet the legendary gatekeeper, dinosauce313. dinosauce313 asks you what the best dinosaur is (hint: contrary to what some may believe, it's not a T-Rex!), but he wants the answer given as a flag. 

Can you tell dinosauce313 what he wants to hear, and exit the park? 

## Solution
The flag is first shifted to the right by 5 characters, wrapping around the edge using the modulo operator. Then, each pair of characters in the flag is swapped (i.e. the first 2 characters are swapped, the 3rd and 4th characters are swapped, etc.). Finally, each character's ASCII value is shifted by 10 downwards. To reverse this, start by increasing each character's ASCII value by 10. Then, swap each pair of characters exactly how they were swapped originally. Finally, shift the flag to the left by 5 characters, and wrap this shift around the edges using the modulo operator.

See `solution.py` for a full solution.

## Flag
`flag{spinosaurus_b3st_d1n0}`

