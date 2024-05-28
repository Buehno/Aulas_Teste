Create database Exame_Candidates;
use Exame_Candidates;

create table users(
	id_user int primary key auto_increment not null,
    name_user varchar(50) not null,
    mail varchar(50) not null,
    passW  varchar(20) not null
);

use users;
select * from users;

insert into users(name_user, mail, passW) 
values ('Ronaldo Bueno', 'ronaldo.bueno@fecaf.com.br','Buh@1202');

create table Candidates(
	id_candidate int primary key auto_increment not null,
    candidateName varchar(50) not null,
    curseCandidate varchar (50) not null,
    testName varchar(100) not null,
    coordenatorCandidate varchar(50) not null
);

create table exame(
	id_exame int primary key auto_increment not null,
    note varchar(560),
    stats bool not null
);
ALTER TABLE exame
ADD COLUMN id_candidate INT;

ALTER TABLE exame
ADD CONSTRAINT fk_candidate
FOREIGN KEY (id_candidate) REFERENCES Candidates(id_candidate);

