class Movie():    
    def __init__(self, title, gener):
        self.title = title
        self.gener = gener
    def gettitle(self):
        return self.gettitle
    def getgener(self):
        return self.getgener
    def setgener(self, gener):
        self.gener = gener
class ethio(Movie):
    def __init__(self,title, gener, year):
        super().__init__(title, gener)
        self.__year = year
    def getyear(self):
        return self.__year
    def getDescription(self):
        return self.gettitle() + self.getgener() + self.getyear()
e = ethio("Amharic", "Movie", "1993")
print(e.gettitle()); print(e.getgener()); print(e.getyear()); print(e.getDescription());




    