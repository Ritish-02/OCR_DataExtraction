create database if not exists ocr_db;
use ocr_db;
create table if not exists patients(id int auto_increment primary key,name varchar(255) not null,dob date not null);
create table if not exists forms_data(id int auto_increment primary key,patient_id int not null,form_json JSON not null,created_at timestamp default current_timestamp,foreign key (patient_id) references patients(id) on delete cascade);