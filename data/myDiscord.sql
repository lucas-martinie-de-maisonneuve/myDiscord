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
('Vannyssa', '2024-03-06 18:10:01',"WELCOME ALL ! The Platform, the leading digital school for all ! Built on a partnership with employers and social actors in the region, the Platform, a digital and new technology school, has committed to enhancing the employability and professional integration of residents in the cities where it operates. It offers quality training in digital professions, open to all, regardless of resources or diplomas, and accessible throughout life. Present in Marseille, Toulon, Cannes and in Martigues, the school continues its development and holds a strong ambition for 2025/2026 with the opening of a brand-new campus capable of accommodating 3000 students. Unlock your potential by joining la plateforme !", 1);

# Rules
('Inessa', '2024-03-06 18:20:02',"OUR RULES | You must respect all members of the server | Your language must be appropriate for all members | Advertising is prohibited here, whether it be verbal, written, via private message, or even in custom statuses | Pornographic, religious, and political content, as well as discriminatory remarks, will result in a permanent ban | Inappropriate usernames and profile pictures (pornography, advertising, offensive material, etc.) are prohibited.", 2);

# News
('Lucassa', '2024-03-06 18:30:03',"OUR NEW | Open house day in Cannes: 20 march from 14:00 to 17:00 | Delayed start for Bachelor IT students on March 11th 2021 | Tech Tuesday: Every Tuesday, there is a conference on a topic in computer science. See you in the main hall of the school | The inclusive digital school, La Plateforme, will expand to achieve a goal of training 3,000 students per year by 2026. To this end, the creation of an urban campus spanning 25,000 square meters will take place within the designated Euromed 2 perimeter of the public development establishment Euroméditerranée.
", 3);

# AI
('Inessa', '2024-03-06 19:10:11',"Hey guys, have you heard about the different specialties offered at LaPlateforme school ?", 7),
('Vanny', '2024-03-06 19:10:12',"Yeah, I was checking out their website earlier. They've got quite a range: cybersecurity, AI, software, web development, immersive systems and digital imaging.", 3),
('Lucassa', '2024-03-06 19:10:13',"Exactly! It's pretty cool that they offer such diverse options. I'm particularly interested in software.", 7), 
('Vannyssa', '2024-03-06 19:10:14'," Oh, me too! Software development is such a versatile field. You can practically create anything from mobile apps to complex systems.", 7),
('Lucassa', '2024-03-06 19:10:15'," Totally! And it's not just about coding; there's also design, testing, and maintenance involved. It's like building digital ecosystems.", 7),
('Inessa', '2024-03-06 19:10:16',"I am not sure software development is for me. I like to play with data better. I will probably pick a different specialty than both of you.", 7);

# Logiciel
('Inessa', '2024-03-06 20:10:21',"Hey guys, I wanted to share something with you. I've decided to specialize in AI for my studies.", 5),
('Vannyssa', '2024-03-06 20:10:22',"Oh, that's awesome! What made you choose AI ?", 5),
('Inessa', '2024-03-06 20:10:23',"Well, I've always been fascinated by data analysis, and AI seems to be at the forefront of that. Plus, it's such a promising field for the future, you know?", 5),
('Lucassa','2024-03-06 20:10:24'," Absolutely! The potential of AI is incredible. It's reshaping so many industries and opening up new possibilities.", 5),
('Inessassa','2024-03-06 20:10:25',"Exactly! I feel like there's so much to explore and innovate within AI. It's both challenging and rewarding.", 5),
('Vannyssa', '2024-03-06 20:10:26',"I'm really glad you found your passion, Inessa. And you're right, AI is definitely a field that's only going to keep growing.", 5),
('Lucassa', '2024-03-06 20:10:27',"Totally! You've got our full support, Inessa. If you ever need help or want to bounce ideas off of us, we're here for you.", 5),
('Inessa', '2024-03-06 20:10:28',"Thanks, guys! I appreciate your encouragement. It means a lot to me. Together, I know we can accomplish great things in this field.", 5);

# Light Side
INSERT INTO message(name, time, message, id_channel) VALUES
('Inessa', '2024-02-06 21:00:01',"Hey everyone, ready to kick off our project?", 10),
('Lucassa', '2024-02-06 21:00:02',"Absolutely! So, our project revolves around LaPlatforme, the digital school in Marseille. Are you happy if we choose this thematique?", 10),
('Vannyssa', '2024-02-06 21:00:03',"Fine by me ! We could perhaps focus on the specialties that the members of our group have chosen for our second year in the IT Bachelor's program, namely artificial intelligence and software. ", 10),
('Inessa', '2024-02-06 21:00:04',"Great idea, both of you! I'm so happy to work on this project together !", 10); 

# Dark Side
INSERT INTO message(name, time, message, id_channel) VALUES
('Inessa', '2024-02-06 22:20:01',"Hey team, we need to discuss our approach to managing members on Discord. It seems like we have an influx of new members, but also some inactive ones.", 8),
('Lucassa', '2024-02-06 22:20:02',"Yeah, I've noticed that too. Some new members are active and engaging, while others join and then go silent.", 8),
('Vannyssa', '2024-02-06 22:20:03',"I agree. Maybe we should have some criteria for when to accept or remove members?", 8),
('Inessa', '2024-02-06 22:20:04',"Sounds fair to me. It gives members a chance to be active and participate while also keeping the community clean and focused.", 8),
('Lucassa', '2024-02-06 22:20:05'," Agreed. We'll implement that policy starting next week. In the meantime, let's encourage existing members to participate more and welcome new ones warmly.", 8),
('Inessa', '2024-02-06 22:20:06'," Great teamwork, everyone. Let's keep our Discord community thriving!", 8); 



















