import json
file = open('sample-data.json', 'r')
data=json.loads(file.read())
print('''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
''')
for i in range(len(data["imdata"])):
    sp=72-len(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"])
    # print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"],data["imdata"][i]["l1PhysIf"]["attributes"]["descr"], data["imdata"][i]["l1PhysIf"]["attributes"]["speed"], data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]+(sp*" ")+data["imdata"][i]["l1PhysIf"]["attributes"]["descr"]+data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]+"   "+data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])