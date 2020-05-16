/*
Navicat MySQL Data Transfer

Source Server         : A
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : equipment_manager

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2020-05-15 20:26:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for equipment_manager
-- ----------------------------
DROP TABLE IF EXISTS `equipment_manager`;
CREATE TABLE `equipment_manager` (
  `inside_id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `equipment_id` varchar(255) NOT NULL,
  `equipment_classid` varchar(255) NOT NULL,
  `equipment_infomation` mediumtext NOT NULL,
  PRIMARY KEY (`inside_id`,`equipment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=96 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of equipment_manager
-- ----------------------------

-- ----------------------------
-- Table structure for storehouse_manager
-- ----------------------------
DROP TABLE IF EXISTS `storehouse_manager`;
CREATE TABLE `storehouse_manager` (
  `storehouse_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `storehouse_name` varchar(255) NOT NULL,
  `storehouse_whois` varchar(255) DEFAULT NULL,
  `storehouse_create_s` varchar(255) DEFAULT NULL,
  `storehouse_is_del` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`storehouse_id`,`storehouse_name`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of storehouse_manager
-- ----------------------------
INSERT INTO `storehouse_manager` VALUES ('1', '科学校区', 'lingyunyi', '2020-05-13', '0');
INSERT INTO `storehouse_manager` VALUES ('2', '东风校区\r\n', 'lingyunyi', '2020-05-13', '0');
INSERT INTO `storehouse_manager` VALUES ('3', '实习基地', 'lingyunyi', '2020-05-13', '0');
