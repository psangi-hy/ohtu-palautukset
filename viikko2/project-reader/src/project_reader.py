from urllib import request
from project import Project
from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # tiedoston sisältö
        parsed = loads(content)
        try:
            poetry = parsed["tool"]["poetry"]
            name = poetry["name"]
            description = poetry["description"]
            dependencies = list(poetry["dependencies"])
            dev_dependencies = list(poetry["group"]["dev"]["dependencies"])
        except KeyError:
            return None

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
