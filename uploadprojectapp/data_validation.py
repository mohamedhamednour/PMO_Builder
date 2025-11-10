from dataclasses import dataclass, asdict


@dataclass
class InitProjectData:
    projectid: str
    projectname: str

    def dict(self):
        return asdict(self)


@dataclass
class GenrateDomainData:
    projectName: str
    stageName: list
    projectId: str

    def dict(self):
        return asdict(self)