DROP TABLE IF EXISTS Contact;
DROP TABLE IF EXISTS Investment;
DROP TABLE IF EXISTS Trade;
DROP TABLE IF EXISTS Firm;

CREATE TABLE [Contact](
[Id] [nvarchar](50) NOT NULL PRIMARY KEY,
[FullName] [nvarchar] (50) NOT NULL,
[ContactType] [nvarchar] (50) NOT NULL
);

CREATE TABLE [Firm](
[Id] [nvarchar](50) NOT NULL PRIMARY KEY,
[FirmName] [nvarchar] (50) NOT NULL
);

CREATE TABLE [Investment](
[Id] varchar(3) NOT NULL PRIMARY KEY,
[InvestorId] [nvarchar] (50) NOT NULL,
[AdviserId] [nvarchar] (50) NOT NULL,
[FirmId] [nvarchar] (50) NOT NULL,
FOREIGN KEY(InvestorId) REFERENCES Contact(Id),
FOREIGN KEY(AdviserId) REFERENCES Contact(Id),
FOREIGN KEY(FirmId) REFERENCES Firm(Id)
);

CREATE TABLE [Trade](
[Id] [nvarchar](50) NOT NULL PRIMARY KEY,
[InvestmentId] [nvarchar] (50) NOT NULL,
[Shares] [integer] NOT NULL,
[Price] [integer] NOT NULL,
FOREIGN KEY(InvestmentId) REFERENCES Investment(Id)
);

INSERT INTO Investment
VALUES ('I00001','C00001','C00004', 'F00001'),
       ('I00002','C00001','C00004', 'F00001'),
       ('I00003','C00002','C00004', 'F00001'),
       ('I00004','C00002','C00005', 'F00002'),
       ('I00005','C00002','C00004', 'F00001'),
       ('I00006','C00003','C00005', 'F00002'),
       ('I00007','C00003','C00005', 'F00002'),
       ('I00008','C00003','C00005', 'F00002');

INSERT INTO Contact
VALUES ('C00001', 'Noella Brady', 'Investor'),
       ('C00002', 'Gavril Girard', 'Investor'),
       ('C00003', 'Jaako Bodilsen', 'Investor'),
       ('C00008', 'Azaria Heppenheimer', 'Investor'),
       ('C00004', 'Herbert Johanssen', 'Adviser'),
       ('C00005', 'Jovica Amelsvoort', 'Adviser');

INSERT INTO Firm
VALUES ('F00001', 'Much Money Management'),
       ('F00002', 'Big Bucks Benefits');

INSERT INTO Trade
VALUES ('T00001', 'I00001', 1000, 3.5),
       ('T00002', 'I00002', 12500, 4),
       ('T00003', 'I00002', 500, 5),
       ('T00004', 'I00003', 4500, 2),
       ('T00005', 'I00004', 1400, 0.5),
       ('T00006', 'I00005', 11000, 15),
       ('T00007', 'I00006', 15000, 1.5),
       ('T00008', 'I00006', 450, 6),
       ('T00009', 'I00007', 750, 9),
       ('T00010', 'I00007', 900, 10),
       ('T00011', 'I00007', 4000, 4),
       ('T00012', 'I00008', 6000, 2),
       ('T00013', 'I00008', 1200, 4.6),
       ('T00014', 'I00008', 150, 6.7),
       ('T00015', 'I00008', 400, 9),
       ('T00016', 'I00008', 800, 2);
