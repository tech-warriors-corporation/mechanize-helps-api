DROP TYPE status CASCADE;

CREATE TYPE status AS ENUM ('unsolved', 'solved');

DROP TABLE tickets CASCADE;

CREATE TABLE tickets (
  id SERIAL PRIMARY KEY,
  driver_id INT NOT NULL,
  vehicle VARCHAR(100) NOT NULL,
  location VARCHAR(200) NOT NULL,
  description VARCHAR(400) NOT NULL,
  mechanic_id INT,
  created_date DATE DEFAULT current_date,
  status status NOT NULL DEFAULT 'unsolved'
);

COMMIT;
