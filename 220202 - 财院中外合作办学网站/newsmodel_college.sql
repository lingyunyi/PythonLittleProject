/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : newsmodel_college

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2022-02-10 20:48:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for account_tb
-- ----------------------------
DROP TABLE IF EXISTS `account_tb`;
CREATE TABLE `account_tb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_iphone` varchar(11) NOT NULL,
  `user_passwd` varchar(255) NOT NULL,
  `user_type` varchar(255) NOT NULL,
  `uesr_loginTime` varchar(255) NOT NULL,
  `is_del` int(1) unsigned NOT NULL DEFAULT '0',
  `user_info_dict` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`,`user_iphone`),
  UNIQUE KEY `user_iphone_Un` (`user_iphone`,`user_type`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account_tb
-- ----------------------------
INSERT INTO `account_tb` VALUES ('11', '18172041272', '202cb962ac59075b964b07152d234b70', 'Ad', '2022-02-09 15:10:43', '0', '{\"i_name\": \"\\u7ba1\\u7406\\u5458\", \"i_cardID\": \"AD200604292351\", \"i_institute\": \"AD\\u4fe1\\u606f\\u4e0e\\u7edf\\u8ba1\\u5b66\\u9662\", \"i_class\": \"\", \"is_null\": \"False\"}');
INSERT INTO `account_tb` VALUES ('12', '18172041272', '202cb962ac59075b964b07152d234b70', 'Te', '2022-02-09 17:29:44', '0', '{\"i_name\": \"Te\\u6559\\u5ba4\", \"i_cardID\": \"Te20060421213\", \"i_institute\": \"Te\\u4fe1\\u606f\\u4e0e\\u7edf\\u8ba1\\u5b66\\u9662\", \"i_class\": \"Te\\u8ba1\\u79d12023\", \"is_null\": \"False\"}');
INSERT INTO `account_tb` VALUES ('13', '18172041272', '202cb962ac59075b964b07152d234b70', 'St', '2022-02-09 17:49:18', '0', '{\"i_name\": \"St\\u5b66\\u751f\", \"i_cardID\": \"St10123033\", \"i_institute\": \"St\\u4fe1\\u606f\\u4e0e\\u7edf\\u8ba1\\u5b66\\u9662\", \"i_class\": \"St\\u8ba1\\u79d12023\", \"is_null\": \"False\"}');
INSERT INTO `account_tb` VALUES ('14', '123', '202cb962ac59075b964b07152d234b70', 'Ad', '2022-02-10 18:09:45', '0', null);

-- ----------------------------
-- Table structure for download_tb
-- ----------------------------
DROP TABLE IF EXISTS `download_tb`;
CREATE TABLE `download_tb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_iphone` varchar(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `content_title` varchar(1024) NOT NULL,
  `wx_url` varchar(255) NOT NULL,
  `create_time` varchar(255) NOT NULL,
  `is_delete` int(1) unsigned zerofill NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`user_iphone`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of download_tb
-- ----------------------------
INSERT INTO `download_tb` VALUES ('7', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('8', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('9', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('0', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('11', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('12', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('13', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('14', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('15', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('16', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('17', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('18', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('19', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('20', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('21', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('22', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('23', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('24', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('25', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('26', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('27', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('28', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('29', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');
INSERT INTO `download_tb` VALUES ('30', '18172041272', '管理员', '【测试下载】私募基金经理高杉夜跑时失踪，警方确认其已经离世，有哪些信息值得关注？', 'https://www.zhihu.com/question/515363030', '2022-02-09 15:22:55', '0');

-- ----------------------------
-- Table structure for law_tb
-- ----------------------------
DROP TABLE IF EXISTS `law_tb`;
CREATE TABLE `law_tb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_iphone` varchar(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `content_title` varchar(1024) NOT NULL,
  `wx_url` varchar(255) NOT NULL,
  `create_time` varchar(255) NOT NULL,
  `is_delete` int(1) unsigned zerofill NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`user_iphone`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of law_tb
-- ----------------------------
INSERT INTO `law_tb` VALUES ('0', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('3', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('4', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('5', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('6', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('7', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('8', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('9', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('10', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('11', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('12', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('13', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '1');
INSERT INTO `law_tb` VALUES ('14', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('15', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('16', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('17', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('18', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('19', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('20', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('21', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('22', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('23', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('24', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('25', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('26', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('27', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('28', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('29', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');
INSERT INTO `law_tb` VALUES ('30', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '1');
INSERT INTO `law_tb` VALUES ('31', '18172041272', '管理员', '【测试法规】北京冬奥会短道速滑2月7日比赛，韩国选手全军覆没后拒绝采访黑脸离场，如何评价他们比赛后的态度？', 'https://www.zhihu.com/question/515332319', '2022-02-09 15:24:01', '0');

-- ----------------------------
-- Table structure for news_tb
-- ----------------------------
DROP TABLE IF EXISTS `news_tb`;
CREATE TABLE `news_tb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_iphone` varchar(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `content_title` varchar(1024) NOT NULL,
  `wx_url` varchar(255) NOT NULL,
  `create_time` varchar(255) NOT NULL,
  `is_delete` int(1) unsigned zerofill NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`user_iphone`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news_tb
-- ----------------------------
INSERT INTO `news_tb` VALUES ('0', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('3', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('4', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('5', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('6', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('7', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('8', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('9', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('10', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('11', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('12', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('13', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('14', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('15', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('16', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('17', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('18', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('19', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('20', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('21', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('22', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('23', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('24', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('25', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('26', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('27', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('28', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '1');
INSERT INTO `news_tb` VALUES ('29', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('30', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('31', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('32', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('33', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');
INSERT INTO `news_tb` VALUES ('34', '18172041272', '管理员', '【测试动态】如何看待「小红花测评」指认「老爸评测」部分产品虚假宣传？真实的情况如何？', 'https://www.zhihu.com/question/515022444', '2022-02-09 15:22:00', '0');

-- ----------------------------
-- Table structure for notice_tb
-- ----------------------------
DROP TABLE IF EXISTS `notice_tb`;
CREATE TABLE `notice_tb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_iphone` varchar(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `content_title` varchar(1024) NOT NULL,
  `wx_url` varchar(255) NOT NULL,
  `create_time` varchar(255) DEFAULT NULL,
  `is_delete` int(1) unsigned zerofill NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`user_iphone`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of notice_tb
-- ----------------------------
INSERT INTO `notice_tb` VALUES ('0', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('5', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('6', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('7', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('8', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('9', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('13', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('16', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('17', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('18', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('19', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('20', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('21', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('22', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('23', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('24', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('25', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('26', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('27', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('29', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('30', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('31', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('32', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('33', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('34', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('35', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('36', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('38', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('39', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('40', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');
INSERT INTO `notice_tb` VALUES ('41', '18172041272', '管理员', '【测试内容】B站为员工猝死一事发长文致歉，称将扩招审核人员1000人降低工作压力，审核岗工作强', 'https://www.zhihu.com/question/515463666', '2022-02-09 15:12:29', '0');

-- ----------------------------
-- Table structure for te_st_wall_tb
-- ----------------------------
DROP TABLE IF EXISTS `te_st_wall_tb`;
CREATE TABLE `te_st_wall_tb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_iphone` varchar(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `content_txt` varchar(255) NOT NULL,
  `img_url` varchar(255) NOT NULL,
  `create_time` varchar(255) NOT NULL,
  `te_a_st` varchar(255) NOT NULL,
  `is_delete` int(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of te_st_wall_tb
-- ----------------------------
INSERT INTO `te_st_wall_tb` VALUES ('5', '18172041272', 'Te教室', '【教室留言】完啦BBQ了。欧耶。', 'static/back_static/s_public/imgs_files/7b890265-505d-42ce-bcb6-17cdf664e973.png', '2022-02-09 17:41:37', 'Te', '0');
INSERT INTO `te_st_wall_tb` VALUES ('0', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('8', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('7', '18172041272', 'Te教室', '【测试留言】啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦', '', '2022-02-09 18:04:55', 'Te', '1');
INSERT INTO `te_st_wall_tb` VALUES ('9', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('10', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('11', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('12', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('13', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('14', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('15', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('16', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('17', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('18', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('19', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('20', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('21', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('22', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('23', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('24', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('25', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('26', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('27', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('28', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('29', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('30', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('31', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('32', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('33', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('34', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('35', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('36', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('37', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('38', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('39', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('40', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('41', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('42', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('43', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('44', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('45', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('46', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('47', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('48', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('49', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('50', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('51', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('52', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('53', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('54', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('55', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('56', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('57', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('58', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('59', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('60', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('61', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('62', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('63', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('64', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('65', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('66', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('67', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('68', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('69', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('70', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('71', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('72', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('73', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('74', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('75', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('76', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('77', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('78', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('79', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('80', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('81', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('82', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('83', '18172041272', 'St学生', '【学生留言】你是打死不说的风景上课来得及看来发大水士大夫。', 'static/back_static/s_public/imgs_files/bb8f4e0c-17cb-4924-a28b-de07583dbfe0.png', '2022-02-09 17:50:15', 'St', '0');
INSERT INTO `te_st_wall_tb` VALUES ('85', '18172041272', 'Te教室', '谁是大傻逼？', '', '2022-02-10 18:11:40', 'Te', '0');
INSERT INTO `te_st_wall_tb` VALUES ('86', '18172041272', 'Te教室', '你才是大傻逼', 'static/back_static/s_public/imgs_files/4c1d2fda-7235-4b45-b499-158272f2647c.jpg', '2022-02-10 18:12:35', 'Te', '0');
INSERT INTO `te_st_wall_tb` VALUES ('87', '18172041272', 'Te教室', '冬梅我喜欢你', 'static/back_static/s_public/imgs_files/6b15b3d5-3669-4e28-8b32-088b30a19e19.jpg', '2022-02-10 18:13:24', 'Te', '0');
INSERT INTO `te_st_wall_tb` VALUES ('88', '18172041272', 'Te教室', '我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦我在做梦', '', '2022-02-10 18:22:07', 'Te', '0');
