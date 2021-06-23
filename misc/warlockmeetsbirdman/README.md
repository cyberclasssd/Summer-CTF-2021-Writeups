# warlockmeetsbirdman
## Problem Statement

There is a part 2??

Hint: Yeah, there is.

## Solution

This is the second part of the OSINT challenge. We can start right where we left off, on part 1. We were at [this](https://www.instagram.com/irrkqlukkirr/) instagram profile when we found the flag of part 1 in the instagram bio `flag{wh4t_typ3_of_b1rd_am_i?}`.
There was also a pastebin link: pastebin.com/piEHyt6j(pastebin.com/piEHyt6j).

Following the link, we find a password protected pastebin. How can we find the password?!

Let's go back to our instagram profile. There doesn't seem to be any more useful info...but the flag of the previous challenge did pose us a question: "what type of bird am i?"

Maybe the profile picture could help us here. Let's use an online tool like [this](https://www.instadp.com/article/5/how-to-download-instagram-profile-picture-in-its-original-quality.html)
to get the profile picture in its full sized glory. Then, we can try reverse image searching.

According to Google, this bird is a harpy! Plugging this in as the password works! The pastebin contains the following:

> 	Your bookish pet crow is mad! You must bring it a Pacific Rose as appeasement. Where could you find such a fruit? Maybe check out the list of cyberclass past workshops.

We can check the list of past CyberClass events by simply googling for the CyberClass website, then looking in Past Events>[Past Workshops](https://sites.google.com/view/cyberclassroom/past-events/past-workshops).
What did the pastebin say again? We needed a Pacific Rose, which is a type of *apple*?

If we try to search for the word "apple" on the CyberClass Past Workshops page, we find a strange insert in the website: "appleappleapple". It's also a link! Clicking on the first "apple" word will lead us to yet another pastebin: https://pastebin.com/p4WyuxPy.
It's not password protected this time.

> 	7FsKpRgomIWvkxafLvkg/DDrB5cS2NyCmb9DN9mzMJc=
Hint: All lowercase; include spaces.
"With dust over chaos we both hurry down streets"
-the narrator, whose friend's younger brother, E.B.W., holds your key. A.E.S is the effectuator.



## Flag
`FLAG{CHICKEN_SALAD_4_LYFE}`
