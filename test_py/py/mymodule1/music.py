class MusicAlbum:

    #constructor or initilizer
    def __init__(self, album, name, music):
        self.album = album
        self.name = name
        self.music = music
    #method
    def info(self):
        return "Album name: "+self.album+'\n'+ "Artist name: "+self.name+'\n'+"Music title: "+self.music  

album1 = MusicAlbum("Kalkidan", "Abebe Teka", "Wofitu");

print(MusicAlbum.info(album1));
print(album1.album);
print(album1.music);
print(album1.name);

album1.name = 'Neway Debebe'
album1.music = 'Jemma'
album1.album = 'New'

print(MusicAlbum.info(album1));
print(album1.album);
print(album1.music);
print(album1.name);

album2 = MusicAlbum("Hagerie", "Efrim Tameru", "Demo Jemeregne");

print(MusicAlbum.info(album2));
print(album2.album);
print(album2.music);
print(album2.name);

print(MusicAlbum.info(album1));
print(MusicAlbum.info(album2));

