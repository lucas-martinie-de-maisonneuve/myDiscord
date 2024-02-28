-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: discord
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `intro` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'General','Welcome to La Plateforme School'),(2,'Bachelor IT','Coding Dreams, Bachelor Reality.'),(3,'Talk Talk','Code & Chat: Tech Friends Unite!');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `communication` tinyint(1) DEFAULT NULL,
  `id_category` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
INSERT INTO `channel` VALUES (1,'About Us',0,0,1),(2,'Rules',0,0,1),(3,'News',0,0,1),(4,'Logiciel',0,1,2),(5,'Logiciel',0,0,2),(6,'Artificial Intelligence',0,1,2),(7,'Artificial Intelligence',0,0,2),(8,'Dark Side',1,0,3),(9,'Light Side',0,1,3),(10,'Light Side',0,0,3);
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `message` text,
  `id_channel` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,'Vannyssa','2024-03-06 18:10:01','WELCOME EVERYONE ! La Plateforme, the leading digital school for all ! Built on a partnership with employers and social actors in the region, La Platforme, a digital and new technology school, has committed to enhancing the employability and professional integration of residents in the cities where it operates. It offers quality training in digital professions, open to all, regardless of resources or diplomas, and accessible throughout life. Present in Marseille, Toulon, Cannes and in Martigues, the school continues its development and holds a strong ambition for 2025/2026 with the opening of a brand-new campus capable of accommodating 3000 students. Unlock your potential by joining La Plateforme !',1),(2,'Inessa','2024-03-06 18:20:02','OUR RULES | You must respect all members of the server | Your language must be appropriate for all members | Advertising is prohibited here, whether it be verbal, written, via private message, or even in any other ways | Pornographic, religious, and political content, as well as discriminatory remarks, will result in a permanent ban | Inappropriate usernames and profile pictures (pornography, advertising, offensive material, etc.) are prohibited.',2),(3,'Vannyssa','2024-01-25 18:30:03','Tech Tuesday: Every Tuesday in Marseille, there is a conference on a topic in computer science. See you in the main hall of the school',3),(4,'Inessa','2024-02-06 18:30:03','Delayed start for Bachelor IT students on March 11th 2021',3),(5,'Lucassa','2024-03-05 18:30:03','If you live by Cannes, there will be an open day on March 20th. Don\'t hesitate to drop by !',3),(6,'Lucassa','2024-03-20 18:30:03','The inclusive digital school, La Plateforme, will expand to achieve a goal of training 3,000 students per year by 2026. To this end, the creation of an urban campus spanning 25,000 square meters will take place within the designated Euromed 2 perimeter of the public development establishment Euroméditerranée.',3),(7,'Inessa','2024-03-06 19:10:11','Hey guys, have you heard about the different specialties offered at LaPlateforme school ?',7),(8,'Vanny','2024-03-06 19:10:12','Yeah, I was checking out their website earlier. They\'ve got quite a range: cybersecurity, AI, software, web development, immersive systems and digital imaging.',7),(9,'Lucassa','2024-03-06 19:10:13','Exactly! It\'s pretty cool that they offer such diverse options. I\'m particularly interested in software.',7),(10,'Vannyssa','2024-03-06 19:10:14',' Oh, me too! Software development is such a versatile field. You can practically create anything from mobile apps to complex systems.',7),(11,'Lucassa','2024-03-06 19:10:15',' Totally! And it\'s not just about coding; there\'s also design, testing, and maintenance involved. It\'s like building digital ecosystems.',7),(12,'Inessa','2024-03-06 19:10:16','I am not sure software development is for me. I like to play with data better. I will probably pick a different specialty than both of you.',7),(13,'Inessa','2024-03-06 20:11:21','Hey guys, I wanted to share something with you. I\'ve decided to specialize in AI for my studies.',5),(14,'Vannyssa','2024-03-06 20:12:22','Oh, that\'s awesome! What made you choose AI ?',5),(15,'Inessa','2024-03-06 20:13:23','Well, I\'ve always been fascinated by data analysis, and AI seems to be at the forefront of that. Plus, it\'s such a promising field for the future, you know?',5),(16,'Lucassa','2024-03-06 20:14:24',' Absolutely! The potential of AI is incredible. It\'s reshaping so many industries and opening up new possibilities.',5),(17,'Inessassa','2024-03-06 20:15:25','Exactly! I feel like there\'s so much to explore and innovate within AI. It\'s both challenging and rewarding.',5),(18,'Vannyssa','2024-03-06 20:16:26','I\'m really glad you found your passion, Inessa. And you\'re right, AI is definitely a field that\'s only going to keep growing.',5),(19,'Lucassa','2024-03-06 20:17:27','Totally! You\'ve got our full support, Inessa. If you ever need help or want to bounce ideas off of us, we\'re here for you.',5),(20,'Inessa','2024-03-06 20:18:28','Thanks, guys! I appreciate your encouragement. It means a lot to me. Together, I know we can accomplish great things in this field.',5),(21,'Inessa','2024-02-06 21:05:01','Hey everyone, ready to kick off our project?',10),(22,'Lucassa','2024-02-06 21:06:02','Absolutely! So, our project revolves around LaPlatforme, the digital school in Marseille. Are you happy if we choose this thematique?',10),(23,'Vannyssa','2024-02-06 21:07:03','Fine by me ! We could perhaps focus on the specialties that the members of our group have chosen for our second year in the IT Bachelor\'s program, namely artificial intelligence and software. ',10),(24,'Inessa','2024-02-06 21:08:04','Great idea, both of you! I\'m so happy to work on this project together !',10),(25,'Inessa','2024-02-06 22:20:01','Hey team, we need to discuss our approach to managing members on Discord. It seems like we have an influx of new members, but also some inactive ones.',8),(26,'Lucassa','2024-02-06 22:21:02','Yeah, I\'ve noticed that too. Some new members are active and engaging, while others join and then go silent.',8),(27,'Vannyssa','2024-02-06 22:22:03','I agree. Maybe we should have some criteria for when to accept or remove members?',8),(28,'Inessa','2024-02-06 22:20:04','Sounds fair to me. It gives members a chance to be active and participate while also keeping the community clean and focused.',8),(29,'Lucassa','2024-02-06 22:23:05',' Agreed. We\'ll implement that policy starting next week. In the meantime, let\'s encourage existing members to participate more and welcome new ones warmly.',8),(30,'Inessa','2024-02-06 22:24:06',' Great teamwork, everyone. Let\'s keep our Discord community thriving!',8);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password`
--

DROP TABLE IF EXISTS `password`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `password` (
  `password` varchar(255) DEFAULT NULL,
  `id_user` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password`
--

LOCK TABLES `password` WRITE;
/*!40000 ALTER TABLE `password` DISABLE KEYS */;
INSERT INTO `password` VALUES ('a',1),('InesLorquet',2),('LucasMartinie2415!',3),('VannyLamorte2512!',4),('GerardLamorte1234!',5),('LucyMadec1234!',6),('CamilleMartinie1234!',7),('ClaireLamorte1234!',8),('EliseMartinie01234!',9),('JulienBeaurain01234!',10),('AlexPhilipot01234!',11);
/*!40000 ALTER TABLE `password` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Admin'),(2,'Normal');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `surname` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `pseudo` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `photo` int DEFAULT NULL,
  `id_role` int DEFAULT NULL,
  `last_message` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'ILV','LLM','Super User','a','ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb',3,2,'2024-02-28 14:20:10'),(2,'Ines','Lorquet','Inessa','ines.lorquet@laplateforme.io','586447cae9b58ff7e2c0a2b3980caf7f2ac5984bfe92cbb99eb0a5f0a702914d',1,1,'2024-02-28 14:20:10'),(3,'Lucas','Martinie','Lucassa','lucas.martinie@laplateforme.io','fc96020f4fc3fbbe01b03f6c1ef101a57110b6844511567e2cca087e02c0d4bb',2,1,'2024-02-28 14:20:10'),(4,'Vanny','Lamorte','Vannyssa','vanny.lamorte@laplateforme.io','5c5bdc4a2ad0deadbd40affb8fe0e359ff6fb3402a38b2a8addbdee2b802d1b5',3,2,'2024-02-28 14:20:10'),(5,'Gerard','Lamorte','GegeDeMars','gerard.lamorte@laplateforme.io','f8e2f219f007cc3d627bd6841ae18c0e3f8e502bb9d3004877d92522924c4f6f',3,2,'2024-02-28 14:20:10'),(6,'Lucy','Madec','Lucyleony','lucy.madec@laplateforme.io','bb3841631aa4975e6a2458f7def3a3030e17ecd27c0f2aa443fa94de4342a24b',4,1,'2024-02-28 14:20:10'),(7,'Camille','Martinie','CamCamCam','camille.martinie@laplateforme.io','2674f3c9cee0ecaa024b4cbc53ed34e18fc2dd288e56d9b2f5a6f57d29115119',2,1,'2024-02-28 14:20:10'),(8,'Claire','Lamorte','Cla Loup','claire.lamorte@laplateforme.io','2fea5bafc5c03e90ffa05ae77fcd7c369f15f041f9da2cbb359b760583f10b86',3,2,'2024-02-28 14:20:10'),(9,'Elise','Martinie','Hey lee02','elise.martinie@laplateforme.io','877dec59269bf577868d0043a673249d3bb544047fdd6bd166ec585b6b67fe7d',2,2,'2024-02-28 14:20:10'),(10,'Julien','Beaurain','Ju Bond','julien.beaurain@laplateforme.io','b69990c682ef8acb1574ab57b656eb997818b0361a4e644b12780bcd09c67839',1,2,'2024-02-28 14:20:10'),(11,'Alex','Philipot','Poupinou','alexandre.philipot@laplateforme.io','ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb',4,2,'2024-02-28 14:20:10');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-28 14:29:38
