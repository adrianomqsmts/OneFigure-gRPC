import sqlite3

conn = sqlite3.connect('oneFigure.db')
cursor = conn.cursor()

# inserindo dados na tabela

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Monkey D. Luffy', 'RARA', 'Monkey D Luffy.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Vismoke Sanji', 'RARA', 'Sanji.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Roronoa Zoro', 'RARA', 'Zoro.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Corazon', 'COMUM', 'Corazon.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Monkey D. Garp', 'RARA', 'Monkey D Garp.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Charlotte Katakuri', 'RARA', 'Charlotte Katakuri.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Edward Newgate', 'ÉPICA', 'Edward Newgate.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Sabo', 'COMUM', 'Sabo.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Shanks', 'ÉPICA', 'Shanks.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Gol D. Roger', 'ÉPICA', 'Gol D Roger.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Portgas D. Ace', 'COMUM', 'Portgas D Ace.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Silvers Rayleigh', 'RARA', 'Silvers Rayleigh.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Brook', 'COMUM', 'Brook.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Tony Tony Chopper', 'COMUM', 'Tony Tony Chopper.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Aokiji', 'RARA', 'Aokij.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Eustass Kid', 'COMUM', 'Eustass Kid.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Bartolomeo', 'COMUM', 'Bartolomeo.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Affe D. Drache', 'COMUM', 'Affe D. Drache.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Franky', 'COMUM', 'Franky.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Donquixote Doflamingo', 'RARA', 'Donquixote Doflamingo.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Boa Hancock', 'RARA', 'Boa Hancock.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Vinsmoke Reiju', 'COMUM', 'Vinsmoke Reiju.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Marco the Phoenix', 'COMUM', 'Marco the Phoenix.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Usopp', 'COMUM', 'Usopp.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Nico Robin', 'COMUM', 'Nico Robin.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Zeff', 'COMUM', 'Zeff.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Crocodile', 'COMUM', 'Crocodile.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Smoker', 'COMUM', 'Smoker.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Bentham', 'COMUM', 'Bentham.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Emporio Ivankov', 'COMUM', 'Emporio Ivankov.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Nekomamushi', 'COMUM', 'Nekomamushi.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Bartholomew Kuma', 'COMUM', 'Bartholomew Kuma.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Kizaru', 'RARA', 'Kizaru.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Rob Lucci', 'COMUM', 'Rob Lucci.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Juracule Mihawk', 'COMUM', 'Juracule Mihawk.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Cavendish', 'COMUM', 'Cavendish.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Perona', 'COMUM', 'Perona.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Benn Beckman', 'RARA', 'Benn Beckman.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Viola', 'COMUM', 'Viola.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Bepo', 'COMUM', 'Bepo.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Foxfire Kin''emon', 'COMUM', 'Foxfire Kin''emon.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Nefertari Vivi', 'COMUM', 'Nefertari Vivi.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Caesar Clown', 'COMUM', 'Caesar Clown.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Basil Hawkins', 'COMUM', 'Basil Hawkins.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Kaido', 'COMUM', 'Kaido.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Eneru', 'COMUM', 'Eneru.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Sengoku', 'COMUM', 'Sengoku.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Nami', 'COMUM', 'Nami.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Buggy', 'RARA', 'Buggy.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Carrot', 'COMUM', 'Carrot.png');
""")

cursor.execute("""
INSERT INTO `figure` (`name`, `rarity`, `path`) VALUES ('Monkey D Dragon', 'ESPECIAL', 'Dragon.png');
""")


cursor.execute("""
INSERT INTO `usuario` (`name`, `password`, `balance`) VALUES ('teste', 'teste', 10000);
""")

cursor.execute("""
INSERT INTO `usuario` (`name`, `password`, `balance`) VALUES ('user', 'user', 10000);
""")

cursor.execute("""
INSERT INTO `usuario` (`name`, `password`, `balance`) VALUES ('fulano', 'fulano', 10000);
""")



# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
