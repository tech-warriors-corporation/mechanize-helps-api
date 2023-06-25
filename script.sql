DROP TYPE status CASCADE;

CREATE TYPE status AS ENUM ('unsolved', 'solved', 'cancelled');

DROP TABLE tickets CASCADE;

CREATE TABLE tickets (
  id SERIAL PRIMARY KEY,
  driver_id INT NOT NULL,
  vehicle VARCHAR(100) NOT NULL,
  location VARCHAR(200) NOT NULL,
  description VARCHAR(400) NOT NULL,
  mechanic_id INT,
  rating INT CHECK (rating >= 1 AND rating <= 5),
  created_date TIMESTAMP DEFAULT current_timestamp,
  status status NOT NULL DEFAULT 'unsolved'
);

COMMIT;
