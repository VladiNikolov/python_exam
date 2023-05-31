from project.jockey import Jockey


class JockeyFactory:

    def create_jockey(self, jockey_name: str, age: int):
        return Jockey(jockey_name, age)