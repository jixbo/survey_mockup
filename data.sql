INSERT INTO "main"."question" ("id", "text", "answers") VALUES ('1', 'Where do you live?', '');
INSERT INTO "main"."question" ("id", "text", "answers") VALUES ('2', 'Are you currently using any cream?', 'yes,no');
INSERT INTO "main"."question" ("id", "text", "answers") VALUES ('3', 'How much do you currently spend on creams each month?', '');
INSERT INTO "main"."question" ("id", "text", "answers") VALUES ('4', 'How much are you willing to spend on creams each month?', '');
INSERT INTO "main"."question" ("id", "text", "answers") VALUES ('5', 'Please describe your current skin issues', '');

INSERT INTO "main"."dependency" ("id", "answer", "question_id_dependant", "question_id_answer") VALUES ('1', 'yes', '3', '2');
INSERT INTO "main"."dependency" ("id", "answer", "question_id_dependant", "question_id_answer") VALUES ('2', 'no', '4', '2');