# an old rusty map bot
## Problem Statement
Hey, this person has a broken bot they need you to fix. Care to take a look? https://im-the-map.cyberclass.repl.co/
## Solution
Based on the problem statement, we should take a look at the `robots.txt` file:
```
User-Agent: *
Disallow: /

Sitemap: https://im-the-map.cyberclass.repl.co/sitemap.xml
```
Visiting the sitemap, we see:
```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<!--  This thing might be a bit outdated?  -->
<url>
<loc>https://im-the-map.cyberclass.repl.co/</loc>
<priority>1.00</priority>
</url>
<url>
<loc>https://im-the-map.cyberclass.repl.co/cables.html</loc>
<priority>0.80</priority>
</url>
<url>
<loc>https://im-the-map.cyberclass.repl.co/gpu.html</loc>
<priority>0.80</priority>
</url>
<url>
<loc>https://im-the-map.cyberclass.repl.co/stopppp.html</loc>
<priority>0.80</priority>
</url>
</urlset>
```

One page in particular looks interesting: `https://im-the-map.cyberclass.repl.co/stopppp.html`.

Visiting this page gives us the flag.

## Flag
`flag{imthemapimthemapxml}`
