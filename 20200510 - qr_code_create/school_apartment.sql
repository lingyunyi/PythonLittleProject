/*
Navicat MySQL Data Transfer

Source Server         : A
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2020-05-17 12:01:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for school_apartment
-- ----------------------------
DROP TABLE IF EXISTS `school_apartment`;
CREATE TABLE `school_apartment` (
  `id` int(11) unsigned zerofill NOT NULL,
  `name_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `sex_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `school_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `class_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `iphone_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `apartment_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `qrcode_img` varchar(255) DEFAULT NULL,
  `is_del` int(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
