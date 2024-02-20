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
('Ines','Lorquet', 'Inessa', 'ines.lorquet@laplateforme.io', 'InessLorquet0609!', 1, 1),
('Lucas','Martinie', 'Lucassa', 'lucas.martinie@laplateforme.io', 'LucasMartinie2412!', 2, 1),
('Vanny','Lamorte', 'Vannyssa', 'vanny.lamorte@laplateforme.io', 'VannyLamorte2512!', 3, 2),
('Jacques','Dubois', 'Jack', 'jacques.dubois@laplateforme.io', 'JackesDubois0502!', 4, 2);

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

INSERT INTO message(name, time, message, id_channel) VALUES
('Inessa', '2024-02-05 13:37:12', 'Welcome to LaPlateforme School', 1),
('Inessa', '2024-02-05 13:37:12', 'Welcome to LaPlateforme School', 1);

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
('Artificial Intelligence 1', True, True, 2), 
('Artificial Intelligence 2', True, False, 2), 
('Dark Side', True, False, 3), 
('Light Side 1', True, True, 3), 
('Light Side 2', True, False, 3);