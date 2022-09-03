dic={

    "Rama Krishan":"father", 

    "Nani":"brother",

    "Anusha Gayathri":"sister",

    "Bujji":"mother"
}

def relation_to_chandu(name):

    name = dic.get(name)

    return("chandu, I am your {}".formate(name))

result = relation_to_chandu("Nani")
print(result)