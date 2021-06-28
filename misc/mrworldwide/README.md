# mrworldwide
## Problem Statement
Mr. Worldwide is planning a trip around the globe! He needs to make a website, and is uploading an image to it. However, he suspects that the image file holds a secret message. What is the message? Make sure that the flag is in the format `flag{}`, and all the characters of the flag will be lowercase.

## Solution
Put the image in an online stegonography decoder, [here](https://stylesuxx.github.io/steganography/). You will now find the text: `[(39.927362, 32.860246),(-8.058765, -34.882457),(59.912664, 10.750807),(40.711806, -73.988744),(39.727727, -104.978255),(14.059467, -87.171896),(17.375177, 78.487209),(55.948121, -3.205113),(49.893631, -97.132239),(34.687753, 135.504505),(24.725890, 46.694707),(-15.424178, 28.307403),(-12.463530, 130.845014)]`

This text corresponds to coordinates of several cities across the world. You can manually enter each set of coordinates into google maps, zoom out, and then determine the cities. The cities are, in order:
- Ankara, Turkey
- Recife, Brazil
- Oslo, Norway
- Ulaanbaatar, Mongolia
- New York, USA
- Denver, USA
- Tegucigalpa, Honduras
- Hyderabad, India
- Edinburgh, Scotland
- Winnipeg, Canada
- Osaka, Japan
- Riyadh, Saudi Arabia
- Lusaka, Zambia
- Darwin, Australia

Using the first letter of each city, we get `aroundtheworld`. Put this in the correct flag format to get `flag{aroundtheworld}`.


## Flag
`flag{aroundtheworld}`
