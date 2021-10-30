
``` python
>>> from markupsafe import Markup

>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

>>> Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up \xbb HTML'
```

















