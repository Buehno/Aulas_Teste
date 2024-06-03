Create database exame_candidates;
use Exame_Candidates;

create table users(
	id_user int primary key auto_increment not null,
    name_user varchar(50) not null,
    mail varchar(50) not null,
    passW  varchar(20) not null
);
insert into users(name_user, mail, passW)
values('Ronaldo Bueno', 'Buenozim_', 'admin');

CREATE TABLE Candidates (
    id_candidate INT AUTO_INCREMENT PRIMARY KEY,
    candidateName VARCHAR(50) NOT NULL,
    curseCandidate VARCHAR(50) NOT NULL,
    testName VARCHAR(50) NOT NULL,
    coordenatorCandidate VARCHAR(50) NOT NULL
);

select * from Candidates;

insert into users(name_user, mail, passW)
values('Convidado', 'convidado', '12345',
		"Esther Cosso", "esther.cosso@pro.fecaf.com.br","Esther.cosso01","Simone Viana","simone.vianna@fecaf.com.br","simone.Vianna01"); 