/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : nmapdb

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2021-05-26 12:19:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for nampscan
-- ----------------------------
DROP TABLE IF EXISTS `nampscan`;
CREATE TABLE `nampscan` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nmapRow` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of nampscan
-- ----------------------------
INSERT INTO `nampscan` VALUES ('1', '[\"192.168.31.1\", \"XiaoQiang\", {\"53\": \"open\", \"80\": \"open\", \"784\": \"open\"}, \"2021-05-24 22:40:13\"]');
INSERT INTO `nampscan` VALUES ('2', '[\"192.168.31.158\", \"Null\", {}, \"2021-05-24 22:40:13\"]');
INSERT INTO `nampscan` VALUES ('3', '[\"192.168.31.222\", \"PC-202104191109\", {\"135\": \"open\", \"139\": \"open\", \"443\": \"open\", \"445\": \"open\", \"902\": \"open\", \"912\": \"open\"}, \"2021-05-24 22:40:13\"]');
INSERT INTO `nampscan` VALUES ('4', '[\"192.168.31.1\", \"XiaoQiang\", {\"53\": \"open\", \"80\": \"open\", \"784\": \"open\"}, \"2021-05-25 13:54:06\"]');
INSERT INTO `nampscan` VALUES ('5', '[\"192.168.31.158\", \"Null\", {}, \"2021-05-25 13:54:06\"]');
INSERT INTO `nampscan` VALUES ('6', '[\"192.168.31.173\", \"M2003J15SC-248136482\", {}, \"2021-05-25 13:54:06\"]');
INSERT INTO `nampscan` VALUES ('7', '[\"192.168.31.19\", \"nova_8-ee5fdda7839cac92\", {}, \"2021-05-25 13:54:06\"]');
INSERT INTO `nampscan` VALUES ('8', '[\"192.168.31.222\", \"PC-202104191109\", {\"135\": \"open\", \"139\": \"open\", \"443\": \"open\", \"445\": \"open\", \"902\": \"open\", \"912\": \"open\"}, \"2021-05-25 13:54:06\"]');
INSERT INTO `nampscan` VALUES ('9', '[\"192.168.31.88\", \"rockchip\", {\"53\": \"open\"}, \"2021-05-25 13:54:06\"]');
INSERT INTO `nampscan` VALUES ('10', '[\"192.168.1.1\", \"Null\", {\"21\": \"open\", \"80\": \"open\", \"943\": \"open\"}, \"2021-05-25 14:08:09\"]');
INSERT INTO `nampscan` VALUES ('11', '[\"192.168.1.1\", \"Null\", {}, \"2021-05-25 14:12:29\"]');
INSERT INTO `nampscan` VALUES ('12', '[\"192.168.1.2\", \"Null\", {}, \"2021-05-25 14:12:29\"]');
INSERT INTO `nampscan` VALUES ('13', '[\"192.168.1.3\", \"Null\", {\"53\": \"open\", \"80\": \"open\", \"784\": \"open\"}, \"2021-05-25 14:12:29\"]');
INSERT INTO `nampscan` VALUES ('14', '[\"192.168.1.4\", \"Null\", {}, \"2021-05-25 14:12:29\"]');
INSERT INTO `nampscan` VALUES ('15', '[\"192.168.1.5\", \"Null\", {}, \"2021-05-25 14:12:29\"]');
