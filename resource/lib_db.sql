/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50730 (5.7.30-0ubuntu0.18.04.1)
 Source Host           : localhost:3306
 Source Schema         : lib_db

 Target Server Type    : MySQL
 Target Server Version : 50730 (5.7.30-0ubuntu0.18.04.1)
 File Encoding         : 65001

 Date: 18/01/2024 22:11:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for lib_admin
-- ----------------------------
DROP TABLE IF EXISTS `lib_admin`;
CREATE TABLE `lib_admin` (
  `admin_user` varchar(40) DEFAULT NULL,
  `admin_id` bigint(20) NOT NULL,
  `admin_password` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of lib_admin
-- ----------------------------
BEGIN;
INSERT INTO `lib_admin` (`admin_user`, `admin_id`, `admin_password`) VALUES ('admin', 1, '1');
INSERT INTO `lib_admin` (`admin_user`, `admin_id`, `admin_password`) VALUES ('BetaCat', 123, '123');
COMMIT;

-- ----------------------------
-- Table structure for lib_book
-- ----------------------------
DROP TABLE IF EXISTS `lib_book`;
CREATE TABLE `lib_book` (
  `name` varchar(40) DEFAULT NULL,
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `author` varchar(40) DEFAULT NULL,
  `pubdate` date DEFAULT NULL,
  `rent_stu_id` bigint(20) DEFAULT '-1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of lib_book
-- ----------------------------
BEGIN;
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('星光', 1, '西城男孩', '2018-10-03', 123);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('残夏', 2, '泰勒·斯威夫特', '1313-01-30', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('1984', 3, 'George Orwell', '1949-06-08', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('The Great Gatsby', 4, 'F. Scott Fitzgerald', '1925-04-10', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('Pride and Prejudice', 5, 'Jane Austen', '1813-01-28', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('围城', 6, '钱钟书', '1947-01-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('活着', 7, '余华', '1993-01-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('The Catcher in the Rye', 8, 'J.D. Salinger', '1951-07-16', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('白夜行', 9, '东野圭吾', '2006-03-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('小王子', 10, '安托万·德·圣埃克苏佩里', '1943-04-06', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('To Kill a Mockingbird', 11, 'Harper Lee', '1960-07-11', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('哈利波特与魔法石', 12, 'J.K.罗琳', '1997-06-26', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('活法', 13, '安妮宝贝', '2000-01-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('百年孤独', 14, '加西亚·马尔克斯', '1967-05-30', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('解忧杂货店', 15, '东野圭吾', '2012-08-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('挪威的森林', 16, '村上春树', '1987-08-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('梦里花落知多少', 17, '三毛', '1976-01-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('人类简史', 18, '尤瓦尔·赫拉利', '2011-02-10', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('月亮与六便士', 19, '毛姆', '1919-01-01', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('囚鸟', 20, '冯内古特', '1961-05-05', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('飘', 21, '玛格丽特·米切尔', '1936-04-30', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('To Kill a Mockingbird', 22, 'Harper Lee', '1960-07-11', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('1984', 23, 'George Orwell', '1949-06-08', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('The Great Gatsby', 24, 'F. Scott Fitzgerald', '1925-04-10', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('Pride and Prejudice', 25, 'Jane Austen', '1813-01-28', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('The Catcher in the Rye', 26, 'J.D. Salinger', '1951-07-16', -1);
INSERT INTO `lib_book` (`name`, `id`, `author`, `pubdate`, `rent_stu_id`) VALUES ('The Lord of the Rings', 27, 'J.R.R. Tolkien', '1954-07-29', -1);
COMMIT;

-- ----------------------------
-- Table structure for lib_reader
-- ----------------------------
DROP TABLE IF EXISTS `lib_reader`;
CREATE TABLE `lib_reader` (
  `stu_name` varchar(40) DEFAULT NULL,
  `stu_id` bigint(20) NOT NULL,
  `stu_user` varchar(40) DEFAULT NULL,
  `stu_password` varchar(40) DEFAULT NULL,
  `stu_dep` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of lib_reader
-- ----------------------------
BEGIN;
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('reader', 1, '1', '1', '1');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('邵子异', 2, 'Shao Ziyi', 'Au3tP8Mtvy', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('邹云熙', 3, 'Zou Yunxi', 'gm71ZbcsqF', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('雷詩涵', 4, 'Lei Shihan', 'S7NkVhxWRw', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('严璐', 5, 'Yan Lu', 'i0xrjPGSyw', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('林云熙', 6, 'Lin Yunxi', 'V7XJNZAuYB', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('金詩涵', 7, 'Jin Shihan', 'B4VKdbEfNv', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('萧子韬', 8, 'Xiao Zitao', '4wkpnFtwBl', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('于子异', 9, 'Yu Ziyi', 'B49z0h6E0p', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('薛云熙', 10, 'Xue Yunxi', '7qhfIh0aau', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('尹璐', 11, 'Yin Lu', 'BjmDicXm5s', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('贺詩涵', 12, 'He Shihan', 'aWtFTZLUU4', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('沈晓明', 13, 'Shen Xiaoming', 'emwJei3R3G', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('向云熙', 14, 'Xiang Yunxi', 'EQRAQrbpg3', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('姚秀英', 15, 'Yao Xiuying', 'NjlM7aqzXV', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('卢璐', 16, 'Lu Lu', 'OXGxNwO4Dq', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('江子韬', 17, 'Jiang Zitao', 'E6SVJC6gbW', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('唐岚', 18, 'Tang Lan', 'xs5ENNZ50z', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('陶安琪', 19, 'Tao Anqi', 'UHAbNign2n', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('曹晓明', 20, 'Cao Xiaoming', 'QWlhm6T8cM', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('戴岚', 21, 'Dai Lan', 'x4OD3O5mId', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('郝詩涵', 22, 'Hao Shihan', 'w15K1OEV14', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('孙宇宁', 23, 'Sun Yuning', 'IzphPp7Tug', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('胡詩涵', 24, 'Hu Shihan', 'PFmyZnQQ75', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('江子韬', 25, 'Jiang Zitao', 'Cc7WugcsyM', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('曾安琪', 26, 'Zeng Anqi', 'W4MvXIrqLD', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('曹子异', 27, 'Cao Ziyi', 'oU6l9y3YOv', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('方宇宁', 28, 'Fang Yuning', 'gF4cfdnAj0', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('孔子韬', 29, 'Kong Zitao', 'KyTSMbQDJ6', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('宋杰宏', 30, 'Song Jiehong', 'Z8oThgkqXK', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('郑睿', 31, 'Zheng Rui', 'viP2bXKKyS', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('郝杰宏', 32, 'Hao Jiehong', 'TdJpWxV7ye', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('沈秀英', 33, 'Shen Xiuying', '6GOjFFHKqP', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('侯杰宏', 34, 'Hou Jiehong', '5mdS7hqnCT', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('苏致远', 35, 'Su Zhiyuan', 'e89P2c0FXb', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('熊震南', 36, 'Xiong Zhennan', '5XBCR7J5Uz', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('魏詩涵', 37, 'Wei Shihan', 'MGGSaJ8vjd', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('高睿', 38, 'Gao Rui', 'eY33NJoo94', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('杜云熙', 39, 'Du Yunxi', 'wTeExEBosC', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('邹子异', 40, 'Zou Ziyi', 'y9hQ3szqRj', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('陈震南', 41, 'Chen Zhennan', 'ttFVoMGfhH', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('韩震南', 42, 'Han Zhennan', 'NM8LxylcMk', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('侯致远', 43, 'Hou Zhiyuan', 'FpeuvfhcIs', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('郭秀英', 44, 'Guo Xiuying', '9mdt0LsH8J', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('林宇宁', 45, 'Lin Yuning', '1f218GJ5rs', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('范宇宁', 46, 'Fan Yuning', 'fcmGHZOrmE', '21计师1班');
INSERT INTO `lib_reader` (`stu_name`, `stu_id`, `stu_user`, `stu_password`, `stu_dep`) VALUES ('BetaCat_stu', 123, 'BetaCat_stu', '123', '123');
COMMIT;

-- ----------------------------
-- Table structure for lib_rent
-- ----------------------------
DROP TABLE IF EXISTS `lib_rent`;
CREATE TABLE `lib_rent` (
  `stu_id` bigint(20) DEFAULT NULL,
  `book_id` bigint(20) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of lib_rent
-- ----------------------------
BEGIN;
INSERT INTO `lib_rent` (`stu_id`, `book_id`) VALUES (123, 1);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
