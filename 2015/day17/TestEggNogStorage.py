import unittest


class TestEggnogStorage(unittest.TestCase):
    def setUp(self):
        self.storage = EggnogStorage([20, 15, 10, 5, 5], 25)

    def test_


class EggnogStorage:
    def __init__(self, containers, volumeToStore):
        self.containers = containers
        self.volumeToStore = volumeToStore
