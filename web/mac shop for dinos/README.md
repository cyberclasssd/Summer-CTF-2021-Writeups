# mac shop for dinos
## Problem Statement
Let's go buy some mac and cheese. https://mac-shop-for-dinos.cyberclass.repl.co/
## Solution
We can view the page source (Ctrl+U). We see a function called Verify() that checks if our password is correct.

```javascript
function Verify(){
        var checkpass = document.getElementById("pass").value;
        if (encodeURIComponent(checkpass) == "cctf%7Burlenc0d%25nGye3h%40w%7D") {
          alert("ya bro that is the flag");
        }
        else {
          alert("na bro no mac n cheese 4 u my man");
        }
      }
```
It seems that whatever password we enter will get URL encoded by `encodeURIComponent(encodeURIComponent(checkpass))`. If the result of the double URL encoding is equal to `flag%257Burlenc0d%2525nGye3h%2540w%257D` we get the alert "ya bro that is the flag." Otherwise (`else`), we get the alert "na bro no mac n cheese 4 u my man."

If we want the flag, we simply have to decode the given URL encoded string, `flag%257Burlenc0d%2525nGye3h%2540w%257D`. (Since the flag is synonymous to the password for logging in, if we enter the decoded string into the login box, the `encodeURIComponent(encodeURIComponent(checkpass))` will encode it to be the same as `cflag%257Burlenc0d%2525nGye3h%2540w%257D` which would log us in.)

We can use an online URL decoder.

# Flag
`flag{urlenc0d%nGye3h@w}`
