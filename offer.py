class Offer:

    def __init__(self, index, position, company, fork, tech, loc, link):
        self.index = index
        self.position = position
        self.company = company
        self.fork = fork
        self.tech = tech
        self.loc = loc
        self.link = link

    def to_dict(self):
        return {"id": self.index, "position": self.position, "company": self.company, "fork": self.fork,
                "tech": self.tech, "loc": self.loc, "link": self.link}
