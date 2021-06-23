T# warlockquest1
## Problem Statement
This is an OSINT challenge! You are a warlock on a quest. You come across a riddling sphinx. "What's my favorite dino?" asks the sphinx.

Hint: you may not have to transcribe this manually.

## Solution
Use an online text extractor tool such as [brandfolder](https://brandfolder.com/workbench/extract-text-from-image) for the gibberish text on the given image, so you don't have to transcribe it by hand.
> 	Oaxux gux tgdc pgdogiohm whdbigfui qab aglx
oubwwxd oahi xguoa. Gtbdy to tbio qxrr rhkxw gux
oax Ixhitbigfu, oax Jfwhmxugobzi, gdw oax Aczihnxtg
thiibfuhxdihi. Whdbigfui gux rx mbbrxio mbbr.
Xizxmhgrrc hdprgognix whdbigfui. Bdmx, 400 thrrhbd
cxgui gyb, H wuxiixw fz hd gd hdprgognrx whdbigfu
mbioftx pbu Gdfnhi'i Nhuoawgc zguoc. Oax mbioftx
qgi zhdk. Oax whdbigfu hi zhdk. Whw cbf kdbq Gdfnhi
agoxi zhdk? Gdfnhi agoxi whdbigfui obb. Gmofgrrc
H oahdk ax fixw ob agox oaxt nfo dbq ax rhkxi oaxt
nxmgfix oaxc'ux wxgw. Gdcqgc, tc pglbuhox whdbigfu
hi oax ioxyb-igfufi.

Decrypt using an automatic substitution cipher solver such as [decode.fr](https://www.dcode.fr/monoalphabetic-substitution)
> 	THERE ARE MANY FANTASTIC DINOSAURS WHO HAVE TRODDEN THIS EARTH. AMONG MT MOST WELL LIKED ARE THE SEISMOSAUR, THE JUDICERATOPS, AND THE HYPSIBEMA MISSOURIENSIS. DINOSAURS ARE LE COOLEST COOL. ESPECIALLY INFLATABSE DINOSAURS. ONCE, 400 MILLION YEARS AGO, I DRESSED UP IN AN INFLATABLE DINOSAUR COSTUME FOR ANUBIS'S BIRTHDAY PARTY. THE COSTUME WAS PINK. THE DINOSAUR IS PINK. DID YOU KNOW ANUBIS HATES PINK? ANUBIS HATES DINOSAURS TOO. ACTUALLY I THINK HE USED TO HATE THEM BUT NOW HE LIKES THEM BECAUSE THEY'RE DEAD. ANYWAY, MY FAVORITE DINOSAUR IS THE STEGO-SAURUS.

Hmmm...the last word "stego-saurus" is written weirdly. Aha! We should try some steganography, aka stego! Use the online steganography decoder [pelock](
https://www.pelock.com/products/steganography-online-codec) to find the hidden message in the image. What's this? We need a key? Try using "stego-saurus" as the key. We get:
> 	An aarakocra sends his aid! https://www.instagram.com/irrkqlukkirr/

Oho, link to an Instagram profile! Let's follow it. Our flag for this part of the challenge can be found in the bio of this Instagram account.

## Flag
`flag{wh4t_typ3_of_b1rd_am_i?}`
