create schema test;

create table user
(
    id   int         null comment '学号',
    name varchar(50) null comment '姓名',
    age  int         null comment '年龄'
)
    comment '学生花名册';

show databases;

show tables ;

desc user;

insert into user(id,name,age) values(1,'Zack',18);
insert into user(id,name,age) values(2,'Anya',18);
insert into user(id, name, age) values (3,'Jack',19);

select * from user;

图片大致对应代码顺序，有点急请见谅（使用了datagrip）
