Create table If Not Exists Person (PersonId int, FirstName varchar(255), LastName varchar(255));
Create table If Not Exists Address (AddressId int, PersonId int, City varchar(255), State varchar(255));
Delete from Person;
Vacuum;
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen');
Delete from Address;
Vacuum;
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York');