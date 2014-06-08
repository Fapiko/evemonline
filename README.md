# EVEMonline #

## Description ##

This project is intended as a browser based alternative to the popular EVEMon program. The
short term goals only include viewing character skills and perhaps a training queue, but if
you'd like to add more please feel free to fork the project and submit a pull request!

I've chosen to write this application because while I love EVEMon it is a Windows-only
program (though I've read it works well with wine, though I've never tried it) and I'm mainly
a Linux guy. I also tend to have multiple PCs which I find it annoying to constantly have
to add my API key to every time I install it somewhere new. Finally, I think it would be
neat to view a lot of this information "on the go" rather than having to install a desktop
application. I think it makes sense to build a web application loosely based on the great
work the guys over at BattleClinic have done.

## Developer Guide (API) ##

### Getting Started ###

For the easiest setup it's recommended to use Virtualenv. To get the API up and running run
the following commands:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
./manage.py syncdb
./manage.py startapp
```

## License ##

The MIT License (MIT)

Copyright (c) 2014 Lucas Jandrew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
