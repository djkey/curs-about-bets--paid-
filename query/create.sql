-- Таблица "Жокеї"
CREATE TABLE Jockeys (
    jockey_id       INTEGER  PRIMARY KEY,
    name            TEXT     (100),
    gender          TEXT     (10),
    age             INTEGER,
    description     TEXT
);

-- Таблица "Коні"
CREATE TABLE Horses (
    horse_id        INTEGER    PRIMARY KEY,
    name            TEXT     (100),
    gender          TEXT     (10),
    age             INTEGER,
    photo           TEXT     (255),
    description     TEXT
);

-- Таблица "Забіги"
CREATE TABLE Races (
    race_id         INTEGER     PRIMARY KEY,
    date            DATE
);

-- Таблица "Користувачі"
CREATE TABLE Users (
    user_id         INTEGER     PRIMARY KEY,
    name            TEXT        (255),
    gender          TEXT        (10),
    age             INTEGER     CHECK (age > 10 & age < 100),
    email           TEXT        (20),
    phone_number    TEXT        (20),
    wallet          INTEGER     CHECK (wallet <= 0),
    password        TEXT        (10),
    photo           TEXT        (255),
    root            INTEGER     DEFAULT (0) 
);

-- Таблица "Ставки"
CREATE TABLE Bets (
    bet_id    INTEGER PRIMARY KEY,
    race_id   INTEGER,
    jockey_id INTEGER,
    horse_id  INTEGER,
    user_id   INTEGER,
    bet_size  INTEGER,
    FOREIGN KEY (race_id)   REFERENCES Races    (race_id),
    FOREIGN KEY (jockey_id) REFERENCES Jockeys  (jockey_id),
    FOREIGN KEY (horse_id)  REFERENCES Horses   (horse_id),
    FOREIGN KEY (user_id)   REFERENCES Users    (user_id) 
);

-- Таблица "Учасники забігу"
CREATE TABLE RaceParticipants (
    race_id   INTEGER,
    jockey_id INTEGER,
    horse_id  INTEGER,
    winner    INTEGER       DEFAULT (0),
    FOREIGN KEY (race_id)   REFERENCES Races    (race_id),
    FOREIGN KEY (jockey_id) REFERENCES Jockeys  (jockey_id),
    FOREIGN KEY (horse_id)  REFERENCES Horses   (horse_id) 
);

