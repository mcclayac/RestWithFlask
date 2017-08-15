-- Tony McClay Postgrsql
-- Table views

-- Table: items

-- DROP TABLE items;

CREATE TABLE items
(
  id serial NOT NULL, -- Primary Key
  name text, -- The Name of the item
  price numeric(4,2) -- The Price of an item
)
WITH (
  OIDS=FALSE
);
ALTER TABLE items
  OWNER TO restfulapi;
GRANT ALL ON TABLE items TO public;
GRANT ALL ON TABLE items TO restfulapi;
COMMENT ON COLUMN items.id IS 'Primary Key';
COMMENT ON COLUMN items.name IS 'The Name of the item';
COMMENT ON COLUMN items.price IS 'The Price of an item';

-- Table: users

-- DROP TABLE users;

CREATE TABLE users
(
  id serial NOT NULL,
  username text NOT NULL,
  password text NOT NULL,
  CONSTRAINT user_id PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE users
  OWNER TO restfulapi;


