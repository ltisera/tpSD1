-- MySQL Script generated by MySQL Workbench
-- Tue Sep  5 01:26:46 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bdRecetas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bdRecetas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bdRecetas` DEFAULT CHARACTER SET utf8 ;
USE `bdRecetas` ;

-- -----------------------------------------------------
-- Table `bdRecetas`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Usuario` (
  `usuario` VARCHAR(25) NOT NULL,
  `email` VARCHAR(45) NULL,
  `nombre` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `tipo` VARCHAR(45) NULL,
  PRIMARY KEY (`usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdRecetas`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Categoria` (
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`nombre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdRecetas`.`Receta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Receta` (
  `idReceta` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `descripcion` VARCHAR(256) NULL,
  `foto1` VARCHAR(1600) NULL,
  `foto2` VARCHAR(1600) NULL,
  `foto3` VARCHAR(1600) NULL,
  `foto4` VARCHAR(1600) NULL,
  `foto5` VARCHAR(1600) NULL,
  `pasos` VARCHAR(1600) NULL,
  `tiempoEnMinutos` INT NULL,
  `categoria` VARCHAR(45) NOT NULL,
  `creador` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`idReceta`),
  INDEX `fk_Receta_Categoria1_idx` (`categoria` ASC) VISIBLE,
  INDEX `fk_Receta_Usuario1_idx` (`creador` ASC) VISIBLE,
  CONSTRAINT `fk_Receta_Categoria1`
    FOREIGN KEY (`categoria`)
    REFERENCES `bdRecetas`.`Categoria` (`nombre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Receta_Usuario1`
    FOREIGN KEY (`creador`)
    REFERENCES `bdRecetas`.`Usuario` (`usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdRecetas`.`Ingrediente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Ingrediente` (
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`nombre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdRecetas`.`Receta_has_Ingrediente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Receta_has_Ingrediente` (
  `idReceta` INT NOT NULL,
  `ingrediente` VARCHAR(45) NOT NULL,
  `cantidad` INT NULL,
  `tipoDeMedida` VARCHAR(45) NULL,
  PRIMARY KEY (`idReceta`, `ingrediente`),
  INDEX `fk_Receta_has_Ingrediente_Ingrediente1_idx` (`ingrediente` ASC) VISIBLE,
  INDEX `fk_Receta_has_Ingrediente_Receta_idx` (`idReceta` ASC) VISIBLE,
  CONSTRAINT `fk_Receta_has_Ingrediente_Receta`
    FOREIGN KEY (`idReceta`)
    REFERENCES `bdRecetas`.`Receta` (`idReceta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Receta_has_Ingrediente_Ingrediente1`
    FOREIGN KEY (`ingrediente`)
    REFERENCES `bdRecetas`.`Ingrediente` (`nombre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdRecetas`.`Siguiendo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Siguiendo` (
  `Usuario_Seguidor` VARCHAR(25) NOT NULL,
  `Usuario_Seguido` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`Usuario_Seguidor`, `Usuario_Seguido`),
  INDEX `fk_Usuario_has_Usuario_Usuario2_idx` (`Usuario_Seguido` ASC) VISIBLE,
  INDEX `fk_Usuario_has_Usuario_Usuario1_idx` (`Usuario_Seguidor` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_has_Usuario_Usuario1`
    FOREIGN KEY (`Usuario_Seguidor`)
    REFERENCES `bdRecetas`.`Usuario` (`usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Usuario_Usuario2`
    FOREIGN KEY (`Usuario_Seguido`)
    REFERENCES `bdRecetas`.`Usuario` (`usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdRecetas`.`Receta_Favorita`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdRecetas`.`Receta_Favorita` (
  `usuario` VARCHAR(25) NOT NULL,
  `idReceta` INT NOT NULL,
  PRIMARY KEY (`usuario`, `idReceta`),
  INDEX `fk_Usuario_has_Receta_Receta1_idx` (`idReceta` ASC) VISIBLE,
  INDEX `fk_Usuario_has_Receta_Usuario1_idx` (`usuario` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_has_Receta_Usuario1`
    FOREIGN KEY (`usuario`)
    REFERENCES `bdRecetas`.`Usuario` (`usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Receta_Receta1`
    FOREIGN KEY (`idReceta`)
    REFERENCES `bdRecetas`.`Receta` (`idReceta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO `bdRecetas`.`Usuario` (`usuario`, `email`, `nombre`, `password`, `tipo`) VALUES ('admin', 'admin@admin.com', 'admin', 'admin', 'admin');
INSERT INTO `bdRecetas`.`Usuario` (`usuario`, `email`, `nombre`, `password`, `tipo`) VALUES ('roberto', 'roberto@roberto.com', 'roberto', 'roberto', 'roberto');

INSERT INTO `bdRecetas`.`Categoria` (`nombre`) VALUES ('Desayuno');
INSERT INTO `bdRecetas`.`Categoria` (`nombre`) VALUES ('Almuerzo');
INSERT INTO `bdRecetas`.`Categoria` (`nombre`) VALUES ('Cena');

INSERT INTO `bdRecetas`.`Receta` (`titulo`, `descripcion`, `foto1`, `foto2`, `foto3`, `foto4`, `foto5`, `pasos`, `tiempoEnMinutos`, `categoria`, `creador`) VALUES ('Huevos con jamon', 'Huevos con jamon', 'https://cdn0.recetasgratis.net/es/posts/2/9/7/huevos_con_jamon_y_frijoles_76792_orig.jpg', NULL, NULL, NULL, NULL, '1. Cocinar los huevos en una sarten\n2. Cocinar el jamon en otra sarten\n3. Servir en un plato', '10', 'Desayuno', 'admin');

INSERT INTO `bdRecetas`.`Receta` (`titulo`, `descripcion`, `foto1`, `foto2`, `foto3`, `foto4`, `foto5`, `pasos`, `tiempoEnMinutos`, `categoria`, `creador`) VALUES ('Frijoles', 'Frijoles muy ricos con salsa especial', 'https://www.goya.com/media/4156/colombian-beans.jpg?quality=80', NULL, NULL, NULL, NULL, '1. Servir 2. Poner salsa', '10', 'Almuerzo', 'roberto');