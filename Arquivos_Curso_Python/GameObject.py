#Classes
"""
Nivel: 01
Ataque: 1
Defesa:
Agilidade:
Magia 

Resistencia:
Habilidade especial:
"""
class GameObject:
	class_name = ""
	desc = ""
	objects = {}

	def __init__(self,name):
		self.name = name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
			return self.class_name + "\n" + self.desc

class Man(GameObject):
    def __init__(self, name):
        self.class_name = "man"
        self.health = 100
        self._desc = "A injured creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 100:
            return self._desc
        elif self.health == 75:
            health_line = "It has a wound on its knee."
        elif self.health == 50:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

Luiz = Man("Luiz")

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Man:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the man!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
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