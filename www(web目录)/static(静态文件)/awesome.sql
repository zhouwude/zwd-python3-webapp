
-- 每一行sql语句 必须以分号结尾 解释器才会认为 语句完毕。
drop database if exists awesome; -- 表存在先删除

create database awesome; -- 创建awesome 数据库

use awesome; -- 使用awesome

-- grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`), -- 主要是用来防止数据插入的时候重复的
    key `idx_created_at` (`created_at`), -- 索引
    primary key (`id`) -- 主键、另外，在MySQL中，对于一个Primary Key的列，MySQL已经自动对其建立了Unique Index，无需重复再在上面建立索引了。
);

create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
); -- engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
);

-- desc table_name;  要查看一个表的结构

-- show create table table_name  查看创建表的SQL语句：

-- change column 是更改 column 的名字。


-- 1. 如果Key是空的, 那么该列值的可以重复, 表示该列没有索引, 或者是一个非唯一的复合索引的非前导列
-- 2. 如果Key是PRI,  那么该列是主键的组成部分
-- 3. 如果Key是UNI,  那么该列是一个唯一值索引的第一列(前导列),并别不能含有空值(NULL)
-- 4. 如果Key是MUL,  那么该列的值可以重复, 该列是一个非唯一索引的前导列(第一列)或者是一个唯一性索引的组成部分但是可以含有空值NULL
