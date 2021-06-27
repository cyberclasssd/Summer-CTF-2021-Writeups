# Suspicious-Questionable-lnvisible-Injection
## Problem Statement
Donkey has stumbled across a suspicious [website](http://134.195.42.198:25567) with nothing on it... 

## Solution
Inspect element, and remove the visibility hidden attribute from the form element.

Then remove the disabled attribute from the login button and input boxes.

We can do a basic injection using `OR 1=1--`, and put that into one of the input boxes, which brings us to a page containing the flag.

## Flag
`flag{h3ll0_th3r3_1nv151bl3_man}`
