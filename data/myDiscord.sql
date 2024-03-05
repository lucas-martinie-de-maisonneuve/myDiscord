-- Active: 1706527539532@@127.0.0.1@3306@discord
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
    id_role INT,
    change_role BOOLEAN,
    last_message DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user(surname, name, pseudo, email, password, photo, id_role, change_role) VALUES
('ILV','LLM', 'Super User', 'a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 3, 1, False),
('ILVbis','LLMbis', 'Super Userbis', 'b', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 3, 2, False ),
('Ines','Lorquet', 'Inessa', 'ines.lorquet@laplateforme.io', '586447cae9b58ff7e2c0a2b3980caf7f2ac5984bfe92cbb99eb0a5f0a702914d', 1, 1, False),
('Lucas','Martinie', 'Lucassa', 'lucas.martinie@laplateforme.io', 'fc96020f4fc3fbbe01b03f6c1ef101a57110b6844511567e2cca087e02c0d4bb', 2, 1, False),
('Vanny','Lamorte', 'Vannyssa', 'vanny.lamorte@laplateforme.io', '5c5bdc4a2ad0deadbd40affb8fe0e359ff6fb3402a38b2a8addbdee2b802d1b5', 3, 1, False),
('Gerard','Lamorte', 'GegeDeMars', 'gerard.lamorte@laplateforme.io', 'f8e2f219f007cc3d627bd6841ae18c0e3f8e502bb9d3004877d92522924c4f6f', 3, 2, False),
('Lucy','Madec', 'Lucyleony', 'lucy.madec@laplateforme.io', 'bb3841631aa4975e6a2458f7def3a3030e17ecd27c0f2aa443fa94de4342a24b', 4, 1, True),
('Camille','Martinie', 'CamCamCam', 'camille.martinie@laplateforme.io', '2674f3c9cee0ecaa024b4cbc53ed34e18fc2dd288e56d9b2f5a6f57d29115119', 2, 2, False),
('Claire','Lamorte', 'Cla Loup', 'claire.lamorte@laplateforme.io', '2fea5bafc5c03e90ffa05ae77fcd7c369f15f041f9da2cbb359b760583f10b86', 3, 2, False),
('Elise','Martinie', 'Hey lee02', 'elise.martinie@laplateforme.io', '877dec59269bf577868d0043a673249d3bb544047fdd6bd166ec585b6b67fe7d', 2, 2, False),
('Julien','Beaurain', 'Ju Bond', 'julien.beaurain@laplateforme.io', 'b69990c682ef8acb1574ab57b656eb997818b0361a4e644b12780bcd09c67839', 2, 2, False),
('Alex','Philipot', 'Poupinou', 'alexandre.philipot@laplateforme.io', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 4, 2, False)
;

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
('About Us', False, False, 1),
('Rules', False, False, 1),
('News', False, False, 1),
('Logiciel', False, True, 2),
('Logiciel', False, False, 2),
('Artificial Intelligence', False, True, 2),
('Artificial Intelligence', False, False, 2),
('Dark Side', True, False, 3),
('Light Side', False, True, 3),
('Light Side', False, False, 3);

CREATE TABLE message (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    time DATETIME,
    message TEXT,
    id_channel INT,
    react int DEFAULT NULL
);

INSERT INTO message(name, time, message, id_channel) VALUES
#--- About Us ---#
('Vannyssa', '2024-02-06 18:10:01',"WELCOME EVERYONE ! La Plateforme, the leading digital school for all ! Built on a partnership with employers and social actors in the region, La Platforme, a digital and new technology school, has committed to enhancing the employability and professional integration of residents in the cities where it operates. It offers quality training in digital professions, open to all, regardless of resources or diplomas, and accessible throughout life. Present in Marseille, Toulon, Cannes and in Martigues, the school continues its development and holds a strong ambition for 2025/2026 with the opening of a brand-new campus capable of accommodating 3000 students. Unlock your potential by joining La Plateforme !", 1),
#--- Rules ---#
('Inessa', '2024-02-06 18:20:02',"OUR RULES | You must respect all members of the server | Your language must be appropriate for all members | Advertising is prohibited here, whether it be verbal, written, via private message, or even in any other ways | Pornographic, religious, and political content, as well as discriminatory remarks, will result in a permanent ban | Inappropriate usernames and profile pictures (pornography, advertising, offensive material, etc.) are prohibited.", 2),
#--- News ---#
('Vannyssa', '2024-01-25 18:30:03',"Tech Tuesday: Every Tuesday in Marseille, there is a conference on a topic in computer science. See you in the main hall of the school", 3),
('Inessa', '2024-02-01 18:30:03',"Delayed start for Bachelor IT students on March 11th 2021", 3), 
('Lucassa', '2024-03-02 18:30:03',"If you live by Cannes, there will be an open day on March 20th. Don't hesitate to drop by !", 3), 
('Lucassa', '2024-03-03 18:30:03',"The inclusive digital school, La Plateforme, will expand to achieve a goal of training 3,000 students per year by 2026. To this end, the creation of an urban campus spanning 25,000 square meters will take place within the designated Euromed 2 perimeter of the public development establishment Euroméditerranée.", 3),
#--- AI ---#
('Inessa', '2024-02-06 19:10:11',"Hey guys, have you heard about the different specialties offered at LaPlateforme school ?", 7),
('Vanny', '2024-02-06 19:10:12',"Yeah, I was checking out their website earlier. They've got quite a range: cybersecurity, AI, software, web development, immersive systems and digital imaging.", 7),
('Lucassa', '2024-02-06 19:10:13',"Exactly! It's pretty cool that they offer such diverse options. I'm particularly interested in software.", 7), 
('Vannyssa', '2024-02-06 19:10:14'," Oh, me too! Software development is such a versatile field. You can practically create anything from mobile apps to complex systems.", 7),
('Lucassa', '2024-02-06 19:10:15'," Totally! And it's not just about coding; there's also design, testing, and maintenance involved. It's like building digital ecosystems.", 7),
('Inessa', '2024-02-06 19:10:16',"I am not sure software development is for me. I like to play with data better. I will probably pick a different specialty than both of you.", 7),
#--- Logiciel ---#
('Inessa', '2024-02-06 20:11:21',"Hey guys, I wanted to share something with you. I've decided to specialize in AI for my studies.", 5),
('Vannyssa', '2024-02-06 20:12:22',"Oh, that's awesome! What made you choose AI ?", 5),
('Inessa', '2024-02-06 20:13:23',"Well, I've always been fascinated by data analysis, and AI seems to be at the forefront of that. Plus, it's such a promising field for the future, you know?", 5),
('Lucassa','2024-02-06 20:14:24'," Absolutely! The potential of AI is incredible. It's reshaping so many industries and opening up new possibilities.", 5),
('Inessassa','2024-02-06 20:15:25',"Exactly! I feel like there's so much to explore and innovate within AI. It's both challenging and rewarding.", 5),
('Vannyssa', '2024-02-06 20:16:26',"I'm really glad you found your passion, Inessa. And you're right, AI is definitely a field that's only going to keep growing.", 5),
('Lucassa', '2024-02-06 20:17:27',"Totally! You've got our full support, Inessa. If you ever need help or want to bounce ideas off of us, we're here for you.", 5),
('Inessa', '2024-02-06 20:18:28',"Thanks, guys! I appreciate your encouragement. It means a lot to me. Together, I know we can accomplish great things in this field.", 5),
#--- Light Side ---#
('Inessa', '2024-02-06 21:05:01',"Hey everyone, ready to kick off our project?", 10),
('Lucassa', '2024-02-06 21:06:02',"Absolutely! So, our project revolves around LaPlatforme, the digital school in Marseille. Are you happy if we choose this thematique?", 10),
('Vannyssa', '2024-02-06 21:07:03',"Fine by me ! We could perhaps focus on the specialties that the members of our group have chosen for our second year in the IT Bachelor's program, namely artificial intelligence and software. ", 10),
('Inessa', '2024-02-06 21:08:04',"Great idea, both of you! I'm so happy to work on this project together !", 10),
#--- Dark Side ---#
('Inessa', '2024-02-06 22:20:01',"Hey team, we need to discuss our approach to managing members on Discord. It seems like we have an influx of new members, but also some inactive ones.", 8),
('Lucassa', '2024-02-06 22:21:02',"Yeah, I've noticed that too. Some new members are active and engaging, while others join and then go silent.", 8),
('Vannyssa', '2024-02-06 22:22:03',"I agree. Maybe we should have some criteria for when to accept or remove members?", 8),
('Inessa', '2024-02-06 22:20:04',"Sounds fair to me. It gives members a chance to be active and participate while also keeping the community clean and focused.", 8),
('Lucassa', '2024-02-06 22:23:05'," Agreed. We'll implement that policy starting next week. In the meantime, let's encourage existing members to participate more and welcome new ones warmly.", 8),
('Inessa', '2024-02-06 22:24:06'," Great teamwork, everyone. Let's keep our Discord community thriving!", 8);


CREATE TABLE password (
    password VARCHAR(255),
    id_user INT
);

INSERT INTO password(password, id_user) VALUES
("a", 1),
("b", 2),
("InesLorquet", 3),
("LucasMartinie2415!",4),
("VannyLamorte2512!",5),
("GerardLamorte1234!",6),
("LucyMadec1234!",7),
("CamilleMartinie1234!",8),
("ClaireLamorte1234!",9),
("EliseMartinie01234!",10),
("JulienBeaurain01234!",11),
("AlexPhilipot01234!", 12);