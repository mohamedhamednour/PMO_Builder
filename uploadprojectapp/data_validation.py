from dataclasses import dataclass, asdict


@dataclass
class InitProjectData:
    projectid: str
    projectname: str

    def dict(self):
        return asdict(self)
