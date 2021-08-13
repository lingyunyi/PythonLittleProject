/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : infomana

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2021-08-13 14:12:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('1', 'admin', '21232f297a57a5a743894a0e4a801fc3');
INSERT INTO `account` VALUES ('2', '123456', 'e10adc3949ba59abbe56e057f20f883e');

-- ----------------------------
-- Table structure for infomana
-- ----------------------------
DROP TABLE IF EXISTS `infomana`;
CREATE TABLE `infomana` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `infoCol` mediumtext,
  `accountName` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of infomana
-- ----------------------------
INSERT INTO `infomana` VALUES ('30', '{\"title\": \"553378880\", \"CreateTime\": \"2021-08-13 14:10:38\", \"infoList\": [{\"content\": \"123\", \"insertTime\": \"2021-08-13 14:10:38\", \"uuid\": \"439f5720-cf69-4925-b38d-4e54a102649a\"}, {\"content\": \"456\", \"insertTime\": \"2021-08-13 14:10:38\", \"uuid\": \"df246286-6c4e-4fd4-a2d6-5f36193e55df\"}, {\"content\": \"789\", \"insertTime\": \"2021-08-13 14:11:16\", \"uuid\": \"6fad66c0-d7aa-4be4-9789-fb9543ffcd7b\"}]}', '21232f297a57a5a743894a0e4a801fc3');
