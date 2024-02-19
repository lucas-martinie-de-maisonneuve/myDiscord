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


# A modifier dans la DATABASE


    # Rennomer les channels
USE discord;

UPDATE channel
SET name = "Logiciel"
WHERE id = 4;

UPDATE channel
SET name = "Artificial Intelligence"
WHERE id = 6;

UPDATE channel
SET name = "Artificial Intelligence"
WHERE id = 7;

UPDATE channel
SET name = "Light Side"
WHERE id = 9;

UPDATE channel
SET name = "Light Side"
WHERE id = 10;

SELECT * FROM channel;


# About Us 
('Lucassa', '2024-03-06 18:10:01',"The Platform, the leading digital school for all ! Built on a partnership with employers and social actors in the region, the Platform, a digital and new technology school, has committed to enhancing the employability and professional integration of residents in the cities where it operates. It offers quality training in digital professions, open to all, regardless of resources or diplomas, and accessible throughout life. Present in Marseille, Toulon, Cannes and in Martigues, the school continues its development and holds a strong ambition for 2025/2026 with the opening of a brand-new campus capable of accommodating 3000 students. Unlock your potential by joining la plateforme !", 1);

# Rules
('Inessa', '2024-03-06 18:20:02',"OUR RULES | You must respect all members of the server | Your language must be appropriate for all members | Advertising is prohibited here, whether it be verbal, written, via private message, or even in custom statuses | Pornographic, religious, and political content, as well as discriminatory remarks, will result in a permanent ban | Inappropriate usernames and profile pictures (pornography, advertising, offensive material, etc.) are prohibited.", 2);

# News
('Lucassa', '2024-03-06 18:30:03',"OUR NEW | Open house day in Cannes: 20 march from 14:00 to 17:00 | Delayed start for Bachelor IT students on March 11th 2021 | Tech Tuesday: Every Tuesday, there is a conference on a topic in computer science. See you in the main hall of the school | The inclusive digital school, La Plateforme, will expand to achieve a goal of training 3,000 students per year by 2026. To this end, the creation of an urban campus spanning 25,000 square meters will take place within the designated Euromed 2 perimeter of the public development establishment Euroméditerranée.
", 3);


# Light Side
INSERT INTO message(name, time, message, id_channel) VALUES
('Inessa', '2024-02-06 17:00:01',"Hey everyone, ready to kick off our project?", 1),
('Lucassa', '2024-02-06 17:00:02',"Absolutely! So, our project revolves around LaPlatforme, the digital school in Marseille. Are you happy if we choose this thematique?", 1);
('Vannyssa', '2024-02-06 17:00:03',"Fine by me ! We could perhaps focus on the specialties that the members of our group have chosen for our second year in the IT Bachelor's program, namely artificial intelligence and software. ", 1);
('Inessa', '2024-02-06 17:00:04',"Great idea, both of you! I'm so happy to work on this project together !", 1); 
















