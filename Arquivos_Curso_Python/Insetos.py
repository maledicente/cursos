#Classe mãe
class Inseto:
	class_name = ""
	desc = ""
	objects = {}

	def __init__(self,name):
		self.name = name
		Inseto.objects[self.class_name] = self

	def get_desc(self):
			return self.class_name + "\n" + self.desc

#Classe filha
class Aranha(Inseto):
	def __init__(self, name):
			self.class_name = "aranha"
			self.pernas = 8
			self._desc = "Uma aranha"
			super().__init__(name)

#Classe filha
class Barata(Inseto):
		def __init__(self, name):
					self.class_name = "barata"
					self.pernas = 6
					self._desc = "Um animal resistente"
					super().__init__(name)

Armadeira = Aranha("Armadeira")
Barata = Barata("Baratinha")

def hit(noun):
    if noun in Inseto.objects:
        thing = Inseto.objects[noun]
        if type(thing) == Aranha:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the insect!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

def examine(noun):
    if noun in Inseto.objects:
        return Inseto.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)

verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit
}

while True:
    get_input()