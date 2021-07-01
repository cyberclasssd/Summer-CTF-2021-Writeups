# Really Smart Alligator
## Problem Statement
You've just met a Really Smart Alligator. What does it tell you?
```
p = 292338524084442490086181008854015675609
q = 185247202893447754330736379123444704803
e = 65537
d = 48913511277713132682013283111754848943415678659992063997085103947173699280865
c = 13847978666453840158748056455349059844242394304908673280323862836913105079345
```

## Solution
This is a straightforward implementation of RSA. Determine `n` by multiplying `p` and `q`, then use the pow function to calculate `m` using `c`, `d`, and `n`. See `solution.py` for the full implementation.

## Flag
`flag{i_wish_i_was_that_smart}`
