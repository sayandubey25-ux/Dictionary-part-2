royaltree= {
    "King":{
        "Name": "Mickey",
        "Race": "Mouse",
        "Occupation": "King"
    },
    "Queen":{
        "Name": "Minnie",
        "Race": "Mouse",
        "Occupation": "Queen"
    },
    "Knight": {
        "Name": "Goofy",
        "Race": "Dog",
        "Occupation": "Knight"
    }
}

print(royaltree)

royaltree.update({"Mage":{"Name": "Doland", "Race": "Duck", "Occupation": "Mage"}})
print(royaltree)

#royaltree.popitem()
#print(royaltree)
for x in royaltree.values():
    print(x)
royaltree['Mage']['Name']='Donald'
print(royaltree)