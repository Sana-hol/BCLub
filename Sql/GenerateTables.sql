CREATE TABLE "Clubs" (
  "club_id" integer PRIMARY KEY,
  "club_name" varchar NOT NULL,
  "created_at" timestamp NOT NULL
);

CREATE TABLE "Members" (
  "member_id" integer PRIMARY KEY,
  "member_name" varchar NOT NULL,
  "member_phone" integer,
  "created_at" timestamp NOT NULL
);

CREATE TABLE "Books" (
  "book_id" integer PRIMARY KEY,
  "book_title" varchar NOT NULL,
  "book_author" varchar NOT NULL,
  "book_rating" integer,
  "total_size" integer
);

CREATE TABLE "Meetings" (
  "meeting_id" integer PRIMARY KEY,
  "club_id" integer NOT NULL,
  "title" varchar,
  "local" varchar NOT NULL,
  "data" varchar NOT NULL,
  "book_id" integer NOT NULL,
  "book_progress" integer NOT NULL,
  "created_at" timestamp NOT NULL
);

CREATE TABLE "BookStatus" (
  "book_id" integer NOT NULL,
  "member_id" integer NOT NULL,
  "book_rate" integer,
  "book_progress" integer NOT NULL,
  PRIMARY KEY ("book_id", "member_id")
);

CREATE TABLE "ClubStatus" (
  "club_id" integer NOT NULL,
  "member_id" integer NOT NULL,
  "club_status" integer NOT NULL,
  PRIMARY KEY ("club_id", "member_id")
);

CREATE TABLE "posts" (
  "id" integer PRIMARY KEY,
  "club_id" integer NOT NULL,
  "member_id" integer NOT NULL,
  "book_id" integer NOT NULL,
  "quote" text,
  "comment" text,
  "progress_wposted" integer NOT NULL,
  "created_at" timestamp NOT NULL
);

ALTER TABLE "Meetings" ADD FOREIGN KEY ("book_id") REFERENCES "Books" ("book_id");

ALTER TABLE "BookStatus" ADD FOREIGN KEY ("member_id") REFERENCES "Members" ("member_id");

ALTER TABLE "BookStatus" ADD FOREIGN KEY ("book_id") REFERENCES "Books" ("book_id");

ALTER TABLE "posts" ADD FOREIGN KEY ("member_id") REFERENCES "Members" ("member_id");

ALTER TABLE "posts" ADD FOREIGN KEY ("book_id") REFERENCES "Books" ("book_id");

ALTER TABLE "posts" ADD FOREIGN KEY ("club_id") REFERENCES "Clubs" ("club_id");

ALTER TABLE "Meetings" ADD FOREIGN KEY ("club_id") REFERENCES "Clubs" ("club_id");

ALTER TABLE "ClubStatus" ADD FOREIGN KEY ("club_id") REFERENCES "Clubs" ("club_id");

ALTER TABLE "ClubStatus" ADD FOREIGN KEY ("member_id") REFERENCES "Members" ("member_id");
