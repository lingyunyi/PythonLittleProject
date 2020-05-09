/*
Navicat MySQL Data Transfer

Source Server         : A
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : house_search

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2020-05-02 12:52:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for house_infomation
-- ----------------------------
DROP TABLE IF EXISTS `house_infomation`;
CREATE TABLE `house_infomation` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `house_title` varchar(255) DEFAULT NULL,
  `house_village` varchar(255) DEFAULT NULL,
  `house_address` varchar(255) DEFAULT NULL,
  `house_price` varchar(255) DEFAULT NULL,
  `house_describe` varchar(255) DEFAULT NULL,
  `house_status` varchar(255) DEFAULT NULL,
  `house_show_img` varchar(255) DEFAULT NULL,
  `houser` varchar(255) DEFAULT NULL,
  `users` varchar(255) DEFAULT NULL,
  `response` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_account
-- ----------------------------
DROP TABLE IF EXISTS `users_account`;
CREATE TABLE `users_account` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `users_account` varchar(255) NOT NULL,
  `users_password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`,`users_account`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_infomation_json
-- ----------------------------
DROP TABLE IF EXISTS `users_infomation_json`;
CREATE TABLE `users_infomation_json` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `users_name` varchar(60) NOT NULL,
  `users_infomation_json` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`users_name`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
