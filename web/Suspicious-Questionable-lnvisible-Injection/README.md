# Suspicious-Questionable-lnvisible-Injection
## Problem Statement
Donkey has stumbled across a suspicious [website](http://134.195.42.198:25567) with nothing on it... 

## Solution
Inspect element, and remove the visibility hidden attribute from the form element (click the small gray arrow to expand down, then double click to edit).

![image](https://user-images.githubusercontent.com/72477484/123558515-85aa9480-d74b-11eb-97a0-6cbafe60e830.png)

Now we can see that there is a place to login, with two input boxes and a login button! However, we can't seem to input anything or use the button. To fix this, remove the disabled attribute from the login button and input boxes. (Again, click the small gray arrow to expand down, then double click to edit.)

![image](https://user-images.githubusercontent.com/72477484/123558557-b8ed2380-d74b-11eb-9bda-77bb942950c4.png)

Now we can do a basic injection using `'OR 1=1--`, and put that into one of the input boxes, which brings us to a page containing the flag.

## Flag
`flag{h3ll0_th3r3_1nv151bl3_man}`
