import glob, re, yaml
print("courses:"),
for x in sorted(glob.glob("courses/*")):
    print "\n-\n    course:", re.compile("\/(.+)").search(x).group(1)
    print "    base: /" + x
    print "    url: /" + x + "/home"
    
    data = None
    with open (x + "/home.md", "r") as myfile:
        data=myfile.read()
    data = data[:data[3:].index("---")+6]
    
    y = yaml.load_all(data)
    for doc in y:
        if doc != None:
            for k,v in doc.items():
                if k == "description":
                    print "    desc:", v
    
    groups = []
    for i in sorted(glob.glob(x + "/*")):
        if re.compile(x.replace("/", "\\/") + "\/\d").search(i) != None:
            groups.append([
              int(re.compile(x.replace("/", "\\/") + "\/([\d])").search(i).groups()[0]),
              i[i.index(" - ") + 3:],
              i
            ])
    if len(groups) > 0:
        print "    groups:\n    -"
    for a in range(1, len(groups) + 1):
        for g in groups:
            if g[0] == a:
                print "        group:", g[1]
                print "        units:"
                units = []
                for c in sorted(glob.glob(g[2] + "/*")):
                    if re.compile(g[2].replace("/", "\\/") + "\/\d").search(c) != None:
                        after = c[len(g[2]) + 1:]
                        after = after[after.index(" - ") + 3:]
                        after = after[:after.rfind(".")]
                        units.append([
                            int(re.compile(g[2].replace("/", "\\/") + "\/([\d])").search(c).groups()[0]),
                            after,
                            c[:c.rfind(".")]
                        ])
                
                for t in range(1, len(units) + 1):
                    for u in units:
                        if u[0] == t:
                            print "        -\n            unit:", u[1]
                            print "            url:", u[2]
