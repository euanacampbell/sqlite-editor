
DROP TABLE Trade;
DROP TABLE Customer;
CREATE TABLE [Trade](
                    [TradeId] varchar(3) NOT NULL,
                    [CustCode] [nvarchar](50) NOT NULL,
                    [Qty] [int] NULL);

CREATE TABLE [Customer](
                    [CustCode] [nvarchar](50) NOT NULL,
                    [CustName] [nvarchar] (50) NOT NULL);

insert into Trade values ('001', 'A',3), ('002', 'C',5), ('003', 'C',20), ('004', 'D',7), ('005', 'B',4), ('006', 'A',10), ('007', 'B',5), ('008', 'E',15);

insert into Customer values ('A','CustA'), ('B','CustB'), ('D','CustD'), ('E','CustE');