CREATE TABLE Doctor (
    doctor_id SERIAL PRIMARY KEY,          -- Уникальный идентификатор врача
    last_name VARCHAR(50) NOT NULL,        -- Фамилия врача
    first_name VARCHAR(50) NOT NULL,       -- Имя врача
    middle_name VARCHAR(50),               -- Отчество врача
    specialty VARCHAR(100) NOT NULL,       -- Специальность врача
    hire_date DATE NOT NULL                -- Дата устройства на работу
);

-- Создание таблицы Visitor (Посетитель)
CREATE TABLE Visitor (
    visitor_id SERIAL PRIMARY KEY,         -- Уникальный идентификатор посетителя
    last_name VARCHAR(50) NOT NULL,        -- Фамилия посетителя
    first_name VARCHAR(50) NOT NULL,       -- Имя посетителя
    middle_name VARCHAR(50),               -- Отчество посетителя
    home_address VARCHAR(200) NOT NULL     -- Домашний адрес посетителя
);
-- Создание таблицы ProcedureRoom (Процедурный кабинет)
CREATE TABLE ProcedureRoom (
    room_id SERIAL PRIMARY KEY,            -- Уникальный идентификатор кабинета
    room_number INT NOT NULL,              -- Номер кабинета
    start_time TIME NOT NULL,              -- Время начала работы
    end_time TIME NOT NULL,                -- Время окончания работы
    day_of_week SMALLINT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7), -- Номер дня недели
    lab_name VARCHAR(100) NOT NULL         -- Название лаборатории
);
-- Создание таблицы Appointment (Приём)
CREATE TABLE Appointment (
    appointment_id SERIAL PRIMARY KEY,     -- Уникальный идентификатор приёма
    doctor_id INT NOT NULL,                -- Внешний ключ на врача
    visitor_id INT NOT NULL,               -- Внешний ключ на посетителя
    start_time TIME NOT NULL,              -- Время начала приёма
    end_time TIME NOT NULL,                -- Время окончания приёма
    day_of_week SMALLINT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7), -- Номер дня недели
    room_number INT NOT NULL, 
	FOREIGN KEY (room_number) REFERENCES ProcedureRoom(room_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),   -- Связь с таблицей Doctor
    FOREIGN KEY (visitor_id) REFERENCES Visitor(visitor_id) -- Связь с таблицей Visitor
);

