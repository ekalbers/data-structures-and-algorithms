from code_challenges.stacks_and_queues.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, obj):
        self.queue.enqueue(obj)

    def dequeue(self, pref):
        current = self.queue.back
        animal = None
        while current:
            if current.value.species == pref:
                animal = current.value
            current = current.next
        return animal


class Cat:
    def __init__(self, name=None):
        self.species = 'cat'
        self.name = name


class Dog:
    def __init__(self, name=None):
        self.species = 'dog'
        self.name = name



