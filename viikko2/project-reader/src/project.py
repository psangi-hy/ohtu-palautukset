class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _combine_strings(self, strings):
        return "".join(f"\n- {s}" for s in strings)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._combine_strings(self.authors)}"
            f"\n\nDependencies: {self._combine_strings(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._combine_strings(self.dev_dependencies)}"
        )
