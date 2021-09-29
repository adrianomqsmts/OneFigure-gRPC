# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('oneFigure.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS `Usuario` (
  `idUser` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(45) NOT NULL UNIQUE,
  `balance` DOUBLE NOT NULL DEFAULT 100,
  `password` VARCHAR(45) NOT NULL,
  `login` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
  );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS `Figure` (
  `idFigure` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `rarity` VARCHAR(10) NOT NULL,
  `path` VARCHAR(45) NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS `Album` (
  `idUser` INTEGER NOT NULL,
  `idFigure` INTEGER NOT NULL,
  `quantity` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idFigure`, `idUser`),
  CONSTRAINT `fk_Usuario_has_Figura_Usuario`
    FOREIGN KEY (`idUser`)
    REFERENCES `Usuario` (`idUser`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Usuario_has_Figura_Figura1`
    FOREIGN KEY (`idFigure`)
    REFERENCES `Figure` (`idFigure`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS `Trade` (
  `idTrade` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `idUser` INT NOT NULL,
  `offer` INT NOT NULL,
  `taking` INT NOT NULL,
  CONSTRAINT `fk_Trade_Usuario1`
    FOREIGN KEY (`idUser`)
    REFERENCES `Usuario` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Trade_Figure1`
    FOREIGN KEY (`offer`)
    REFERENCES `Figure` (`idFigure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Trade_Figure2`
    FOREIGN KEY (`taking`)
    REFERENCES `Figure` (`idFigure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
""")


print('Tabelas criadas com sucesso.')
# desconectando...
conn.close()
