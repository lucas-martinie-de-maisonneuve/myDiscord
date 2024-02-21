-- Active: 1706528666952@@127.0.0.1@3306@discord
CREATE DATABASE discord;
USE discord;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    surname VARCHAR(255),
    name VARCHAR(255),
    pseudo VARCHAR(255), 
    email VARCHAR(255),
    password VARCHAR(255),
    photo INT, 
    id_role INT
);

INSERT INTO user(surname, name, pseudo, email, password, photo, id_role) VALUES
('Ines','Lorquet', 'Inessa', 'ines.lorquet@laplateforme.io', '586447cae9b58ff7e2c0a2b3980caf7f2ac5984bfe92cbb99eb0a5f0a702914d', 1, 1),
('Lucas','Martinie', 'Lucassa', 'lucas.martinie@laplateforme.io', 'fc96020f4fc3fbbe01b03f6c1ef101a57110b6844511567e2cca087e02c0d4bb', 2, 1),
('Vanny','Lamorte', 'Vannyssa', 'vanny.lamorte@laplateforme.io', '5c5bdc4a2ad0deadbd40affb8fe0e359ff6fb3402a38b2a8addbdee2b802d1b5', 3, 2),
('Jacques','Dubois', 'Jack', 'jacques.dubois@laplateforme.io', '2f5cede731389f72b1c679168da2258bb21420e12f547c89ab6cd769ba5e8087', 4, 2);

CREATE TABLE role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
); 

INSERT INTO role(name) VALUES
('Admin'),
('Normal');

CREATE TABLE message (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    time DATETIME,
    message TEXT, 
    id_channel INT
);

CREATE TABLE category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    intro TEXT
);

INSERT INTO category(name, intro) VALUES
('General','Welcome to La Plateforme School'), 
('Bachelor IT','Coding Dreams, Bachelor Reality.'),
('Talk Talk','Code & Chat: Tech Friends Unite!');

CREATE TABLE channel (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255), 
    status BOOLEAN,
    communication BOOLEAN,
    id_category INT
);

INSERT INTO channel(name, status, communication, id_category) VALUES
('About Us', True, False, 1), 
('Rules', True, False, 1),
('News', True, False, 1),
('Logiciel', True, True, 2), 
('Logiciel', True, False, 2), 
('Artificial Intelligence', True, True, 2), 
('Artificial Intelligence', True, False, 2), 
('Dark Side', True, False, 3), 
('Light Side 1', True, True, 3), 
('Light Side 2', True, False, 3);
