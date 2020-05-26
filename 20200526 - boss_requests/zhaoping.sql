/*
Navicat MySQL Data Transfer

Source Server         : A
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2020-05-26 13:02:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for zhaoping
-- ----------------------------
DROP TABLE IF EXISTS `zhaoping`;
CREATE TABLE `zhaoping` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `zwmc` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `gsmc` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `gzdd` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `xz_low` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `xz_height` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `ptime` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `href` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of zhaoping
-- ----------------------------
