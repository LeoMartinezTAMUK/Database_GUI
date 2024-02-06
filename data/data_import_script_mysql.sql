set @@global.local_infile = 1;

load data local infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.1\\Uploads\\CBM005.txt' into table cbm005_table
(@row)
set record_code = substr(@row,1,1),
inst_code = substr(@row,2,6),
subject = substr(@row,8,7),
course_num = substr(@row,15,7),
section_num = substr(@row,22,7),
unused = substr(@row,29,1),
building = substr(@row,30,6),
room = substr(@row,36,16),
days = substr(@row,52,7),
time = substr(@row,59,4),
duration = substr(@row,63,3),
semester = substr(@row,66,1),
year = substr(@row,67,4),
room_type = substr(@row,71,3),
item_15 = substr(@row,74,15),
item_16 = substr(@row,89,3),
item_17 = substr(@row,92,3),
item_18 = substr(@row,95,3),
item_19 = substr(@row,98,3);