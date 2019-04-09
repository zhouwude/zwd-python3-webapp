drop database if exists zhouwudeblog;

create database zhouwudeblog;

use zhouwudeblog;

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`), -- 唯一索引 相当于 (unique index) 不能重复 不能为null 命名为 idx_email 可以通过 alter table users drop index idx_email删除
    key `idx_created_at` (`created_at`), -- 纯索引(普通的索引 ) 可以为null 可以重复 命名为 idx_created_at alter table users drop index index_name 删除该索引
    primary key (`id`)
) engine=innodb default charset=utf8;


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
) engine=innodb default charset=utf8;

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
) engine=innodb default charset=utf8;