/*
Navicat MySQL Data Transfer

Source Server         : william
Source Server Version : 50022
Source Host           : localhost:3306
Source Database       : william

Target Server Type    : MYSQL
Target Server Version : 50022
File Encoding         : 65001

Date: 2018-07-17 16:44:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question` (
  `question_id` int(11) NOT NULL,
  `question_text` varchar(200) default NULL,
  `option_one` varchar(100) default NULL,
  `option_twe` varchar(100) default NULL,
  `option_three` varchar(100) default NULL,
  `option_four` varchar(200) default NULL,
  `answer` varchar(2) default NULL,
  PRIMARY KEY  (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of question
-- ----------------------------
INSERT INTO `question` VALUES ('1', '明朝的科举制度发生了某些变化，主要表现为', '开始采用分科考试的方法选拔官员', '首创了武举和殿试', '考试科目开始增加进士科', '考试范围仅限于四书五经', 'D');
INSERT INTO `question` VALUES ('2', '加入要拍一部有关康熙的电视剧，下列道具中可能会用得上的是', '”白酒释兵权“中的酒杯', '”军机处“的官署牌', '雅克萨之战的地图', '锦衣卫的印章', 'C');
INSERT INTO `question` VALUES ('3', '史前人类元谋人距今（）年前', '204万', '170万', '50万', '105万', 'B');
INSERT INTO `question` VALUES ('4', '在”二十四“节气中“立冬”之前和之后的两个节气分别是（）', '霜降、小雪', '寒露、小雪', '大雪、冬至', '寒露、霜降', 'A');
INSERT INTO `question` VALUES ('5', '新石器时代仰韶文化的（）是我国现存最早的绘画作品', '人面兽纹图', '花山原始岩图', '鹤鱼石斧图', '女史箴图', 'C');
INSERT INTO `question` VALUES ('6', '“贡士”是由（）考出来的考生', '院试', '乡试', '会试', '殿试', 'C');
INSERT INTO `question` VALUES ('7', '生肖发端于（），东汉时期已有明确记载。', '夏朝', '商', '春秋', '战国', 'D');
INSERT INTO `question` VALUES ('8', '“皇帝”的称呼是从（）开始的', '汉武帝', '周文王', '秦始皇', '唐太宗', 'C');
INSERT INTO `question` VALUES ('9', '五代时期的（）是山水画大师，代表作是《匡庐图》', '黄筌', '吴道子', '荆浩', '顾恺之', 'C');
INSERT INTO `question` VALUES ('10', '佛教创立于（）', '公元1世纪', '公元前6世纪', '公元6世纪', '7世纪初', 'B');

-- ----------------------------
-- Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS `result`;
CREATE TABLE `result` (
  `user` varchar(200) default NULL,
  `score` int(11) default NULL,
  `time` varchar(20) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of result
-- ----------------------------
INSERT INTO `result` VALUES ('15001', '75', '2017-1-17');
INSERT INTO `result` VALUES ('15504', '75', '2018-7-14');
INSERT INTO `result` VALUES ('15504', '75', '2018-6-14-15');
INSERT INTO `result` VALUES ('15504', '75', '2018-7-14-15');
INSERT INTO `result` VALUES ('15504', '100', '2018-7-14-15-14');
INSERT INTO `result` VALUES ('15504', '75', '2018-7-14-15-16');
INSERT INTO `result` VALUES ('15504', '0', '2018-7-15-15-58');
INSERT INTO `result` VALUES ('15504', '0', '2018-7-15-15-59');
INSERT INTO `result` VALUES ('15504', '25', '2018-7-15-16-28');
INSERT INTO `result` VALUES ('15504', '0', '2018-7-15-16-33');
INSERT INTO `result` VALUES ('15504', '25', '2018-7-15-16-33');
INSERT INTO `result` VALUES ('15504', '25', '2018-7-15-16-33');
INSERT INTO `result` VALUES ('15504', '25', '2018-7-15-16-33');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` varchar(20) NOT NULL,
  `name` varchar(50) default NULL,
  `age` int(3) default NULL,
  `dept` varchar(50) default NULL,
  `address` varchar(100) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1500', 'leon', '20', '网络工程', '雨花区');
INSERT INTO `student` VALUES ('1501', 'william', '21', '软件工程', '雨湖区');

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `id` int(11) default NULL,
  `name` varchar(10) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test
-- ----------------------------
INSERT INTO `test` VALUES ('1', 'leon');
INSERT INTO `test` VALUES ('2', 'william');
