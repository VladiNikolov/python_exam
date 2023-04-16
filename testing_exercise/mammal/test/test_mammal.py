from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):

    def test_correct_init(self):
        mammal = Mammal("Lily", "Fox", "exa")

        self.assertEqual("Lily", mammal.name)
        self.assertEqual("Fox", mammal.type)
        self.assertEqual("exa", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal("Lily", "Fox", "exa")

        result = mammal.make_sound()
        self.assertEqual("Lily makes exa", result)

    def test_get_kingdom(self):
        mammal = Mammal("Lily", "Fox", "exa")
        self.assertEqual("animals", mammal._Mammal__kingdom)

        result = mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        mammal = Mammal("Lily", "Fox", "exa")

        result = mammal.info()
        self.assertEqual("Lily is of type Fox", result)


if __name__ == "__main__":
    main()