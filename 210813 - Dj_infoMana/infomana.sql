/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : infomana

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2022-01-26 10:26:37
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
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('1', 'admin', '21232f297a57a5a743894a0e4a801fc3');
INSERT INTO `account` VALUES ('2', '123456', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `account` VALUES ('3', 'dm', '608e7dc116de7157306012b4f0be82ac');

-- ----------------------------
-- Table structure for infomana
-- ----------------------------
DROP TABLE IF EXISTS `infomana`;
CREATE TABLE `infomana` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `infoCol` mediumtext,
  `accountName` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of infomana
-- ----------------------------
