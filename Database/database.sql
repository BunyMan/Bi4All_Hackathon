BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Room_Reservations" (
	"ID_Reservation"	INTEGER,
	"Start"	DATETIME NOT NULL,
	"End"	DATETIME NOT NULL,
	"ID_ROOM"	INTEGER NOT NULL,
	PRIMARY KEY("ID_Reservation"),
	FOREIGN KEY("End") REFERENCES "Room"("ID")
);
CREATE TABLE IF NOT EXISTS "Room" (
	"ID"	INTEGER,
	"Capacity"	INTEGER NOT NULL,
	PRIMARY KEY("Capacity","ID")
);
INSERT INTO "Room_Reservations" VALUES (1,'2022-03-23 10:10','2022-03-23 10:10',4);
INSERT INTO "Room_Reservations" VALUES (2,'','',20);
INSERT INTO "Room" VALUES (1,4);
INSERT INTO "Room" VALUES (2,4);
INSERT INTO "Room" VALUES (3,8);
INSERT INTO "Room" VALUES (4,6);
COMMIT;
