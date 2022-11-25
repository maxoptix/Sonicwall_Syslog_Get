# Sonicwall_Syslog_Get

Creating a Databese Table
Use mysql database 8.0 server.

![This is an image]([https://myoctocat.com/assets/images/base-octocat.svg](https://github.com/maxoptix/Sonicwall_Syslog_Get/releases/download/untagged-066623e0df2d4f4c1d36/s1.jpg))
![This is an image]([https://myoctocat.com/assets/images/base-octocat.svg](https://github.com/maxoptix/Sonicwall_Syslog_Get/releases/download/untagged-066623e0df2d4f4c1d36/s2.jpg))
![This is an image]([https://myoctocat.com/assets/images/base-octocat.svg](https://github.com/maxoptix/Sonicwall_Syslog_Get/releases/download/untagged-066623e0df2d4f4c1d36/s3.jpg))


CREATE TABLE `log_any` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `app` varchar(5) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `src` varchar(35) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `dst` varchar(35) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `srcmac` varchar(20) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `dstmac` varchar(20) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `proto` varchar(15) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `category` varchar(150) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `rule` varchar(35) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `note` varchar(150) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `action` varchar(10) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `country_code` varchar(10) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `country_name` varchar(50) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `city` varchar(50) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin5 COLLATE latin5_turkish_ci DEFAULT NULL,
  `dstname` varchar(50) DEFAULT NULL,
  `usr` varchar(10) DEFAULT NULL,
  `arg` varchar(255) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=160729 DEFAULT CHARSET=latin5;
