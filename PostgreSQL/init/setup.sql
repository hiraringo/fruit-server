CREATE TABLE public.fruits 
(
   id smallserial NOT NULL,
   name varchar(10) NOT NULL,
   country varchar(10) NOT NULL,
   PRIMARY KEY (id)
)
WITH (
   OIDS = FALSE
);

INSERT INTO fruits (name, country) VALUES
    ('りんご', '日本'),
    ('オレンジ', 'アメリカ'),
    ('バナナ', '中国');