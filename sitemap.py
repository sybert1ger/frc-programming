import sys
sys.stdout = open('_config.yml', 'w')

print "name: \"FRC West Curriculum\"\n\
description: \"FRC West's Robotics Curriculum\"\n\n\
url: http://www.frc-west.github.io\n\n\
permalink: pretty\n\
markdown: rdiscount\n\n\
# Site Navigation\n\
"

def getyaml(file, key):
    import yaml
    data = None
    with open (file, "r") as myfile:
        data=myfile.read()
    data = data[:data[3:].index("---")+6]
    
    y = yaml.load_all(data)
    for doc in y:
        if doc != None:
            for k,v in doc.items():
                if k == key:
                    return v
def unCamel(s):
    r = re.compile("([a-zA-Z][a-z]*)")
    name = ""
    if r.search(s) == None:
        name = s
    else:
        for g in r.findall(s):
            name += g
            if len(g) > 1:
                name += " "
        if name[len(name) - 1] == " ":
            name = name[:len(name) - 1]
    return name

import glob, re
print("courses:"),
for x in sorted(glob.glob("courses/*")):
    print "\n-\n    course:", getyaml(x + "/home.md", "title")
    print "    base: /" + x
    print "    url: /" + x + "/home"
    desc = getyaml(x + "/home.md", "description")
    if desc != None:
        print "    desc:", desc
    
    groups = []
    for i in sorted(glob.glob(x + "/*")):
        if re.compile(x.replace("/", "\\/") + "\/\d").search(i) != None:
            name = unCamel(i[i.index("-") + 1:])
            groups.append([
              int(re.compile(x.replace("/", "\\/") + "\/([\d])").search(i).groups()[0]),
              name,
              i
            ])
    if len(groups) > 0:
        print "    groups:\n"
    for a in range(1, len(groups) + 1):
        for g in groups:
            if g[0] == a:
                print "    -\n        group:", g[1]
                units = []
                for c in sorted(glob.glob(g[2] + "/*")):
                    if re.compile(g[2].replace("/", "\\/") + "\/\d").search(c) != None:
                        title = getyaml(c, "title")

                        units.append([
                            int(re.compile(g[2].replace("/", "\\/") + "\/([\d])").search(c).groups()[0]),
                            title,
                            "/" + c[:c.rfind(".")]
                        ])
                
                if len(units) > 0:
                    print "        units:"
                for t in range(1, len(units) + 1):
                    for u in units:
                        if u[0] == t:
                            print "        -\n            unit:", u[1]
                            print "            url:", u[2], "\n"

    tests = []
    for i in sorted(glob.glob(x + "/Tests/*")):
        if re.compile(x.replace("/", "\\/") + "\/Tests\/\d").search(i) != None:
            name = getyaml(i, "title")
            tests.append([name, "/" + i[:i.rfind(".")]])
    if len(tests) > 0:
        print "    tests:\n"
        for test in tests:
            print "    -\n        test:", test[0]
            print "        url:", test[1]
