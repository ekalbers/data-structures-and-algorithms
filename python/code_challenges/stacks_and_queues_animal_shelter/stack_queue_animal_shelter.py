from code_challenges.stacks_and_queues.queue import Queue


class AnimalShelter(Queue):
    def __init__(self):
        super().__init__()

    def dequeue(self, pref=None):
        temp_stack = Queue()
        return_value = None
        if not pref or self.front.value.species == pref:
            return super().dequeue()
        temp_stack.enqueue(super().dequeue())
        while self.front:
            current = self.front.value.species
            if current == pref:
                return_value = super().dequeue()
            else:
                temp_stack.enqueue(super().dequeue())
        while temp_stack.front:
            self.enqueue(temp_stack.dequeue())
        return return_value


class Cat:
    def __init__(self, name=None):
        self.species = 'cat'
        self.name = name


class Dog:
    def __init__(self, name=None):
        self.species = 'dog'
        self.name = name



