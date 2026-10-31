#!/usr/bin/env python3
# run before every push: writes the current UTC time into index.html (the page shows it in GMT+2)
import re,datetime
t=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
s=open("index.html").read()
open("index.html","w").write(re.sub(r'const BUILD="[^"]*"','const BUILD="%s"'%t,s,1));print("stamped",t)
