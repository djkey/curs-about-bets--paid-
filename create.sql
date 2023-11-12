-- Таблица "Жокеї"
CREATE TABLE Jockeys (
    jockey_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    history TEXT
);

-- Таблица "Коні"
CREATE TABLE Horses (
    horse_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    color VARCHAR(15),
    photo VARCHAR(255),
    history TEXT
);

-- Таблица "Забіги"
CREATE TABLE Races (
    race_id INT PRIMARY KEY,
    date DATE,
    winner_id INT,
    winner_horse_id INT,
    FOREIGN KEY (winner_id) REFERENCES Jockeys(jockey_id),
    FOREIGN KEY (winner_horse_id) REFERENCES Horses(horse_id)
);

-- Таблица "Користувачі"
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    gender VARCHAR(255),
    age INT,
    email VARCHAR(255),
    phone_number VARCHAR(20),
    root BOOLEAN
);

-- Таблица "Ставки"
CREATE TABLE Bets (
    bet_id INT PRIMARY KEY,
    race_id INT,
    jockey_id INT,
    horse_id INT,
    user_id INT,
    FOREIGN KEY (race_id) REFERENCES Races(race_id),
    FOREIGN KEY (jockey_id) REFERENCES Jockeys(jockey_id),
    FOREIGN KEY (horse_id) REFERENCES Horses(horse_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Таблица "Учасники забігу"
CREATE TABLE RaceParticipants (
    race_id INT,
    jockey_id INT,
    horse_id INT,
    FOREIGN KEY (race_id) REFERENCES Races(race_id),
    FOREIGN KEY (jockey_id) REFERENCES Jockeys(jockey_id),
    FOREIGN KEY (horse_id) REFERENCES Horses(horse_id)
);

-- Таблица "Переможці"
CREATE TABLE Winners (
    race_id INT UNIQUE,
    jockey_id INT,
    horse_id INT,
    FOREIGN KEY (race_id) REFERENCES Races(race_id),
    FOREIGN KEY (jockey_id) REFERENCES Jockeys(jockey_id),
    FOREIGN KEY (horse_id) REFERENCES Horses(horse_id)
);
