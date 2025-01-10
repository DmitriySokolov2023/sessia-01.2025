CREATE TABLE CarSeries (
    car_series VARCHAR(50) PRIMARY KEY,    -- Серия автомобиля
    manufacturer VARCHAR(100) NOT NULL     -- Завод-изготовитель
);

-- Таблица ServiceCenters (Сервисные центры)
CREATE TABLE ServiceCenters (
    service_center_id SERIAL PRIMARY KEY,   -- Уникальный идентификатор сервисного центра
    service_center_name VARCHAR(100) NOT NULL,  -- Наименование сервисного центра
    company_name VARCHAR(100) NOT NULL,         -- Наименование фирмы
    repair_slots INT NOT NULL,                  -- Число мест для ремонта
    service_center_address VARCHAR(200) NOT NULL -- Адрес центра
);

-- Таблица Cars (Автомобили)
CREATE TABLE Cars (
    car_id SERIAL PRIMARY KEY,              -- Уникальный идентификатор автомобиля
    car_series VARCHAR(50) NOT NULL,        -- Серия автомобиля
    engine_power INT NOT NULL,              -- Мощность двигателя
    passenger_count INT NOT NULL,           -- Число пассажиров
    weight INT NOT NULL,                    -- Вес автомобиля
    color VARCHAR(50) NOT NULL,             -- Цвет автомобиля
    body_type VARCHAR(50) NOT NULL,         -- Тип кузова
    air_conditioning BOOLEAN NOT NULL,      -- Наличие кондиционера
    service_center_id INT NOT NULL,         -- Идентификатор сервисного центра
    FOREIGN KEY (car_series) REFERENCES CarSeries(car_series), -- Связь с таблицей CarSeries
    FOREIGN KEY (service_center_id) REFERENCES ServiceCenters(service_center_id) -- Связь с таблицей ServiceCenters
);