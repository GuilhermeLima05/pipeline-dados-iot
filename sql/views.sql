-- View 1: Média de temperatura
CREATE VIEW IF NOT EXISTS avg_temp_por_dispositivo AS
SELECT out_in AS device_id, AVG(temp) as avg_temp
FROM temperature_readings
GROUP BY out_in;

-- View 2: Leituras por hora
CREATE VIEW IF NOT EXISTS leituras_por_hora AS
SELECT strftime('%H', noted_date) AS hora, COUNT(*) AS contagem
FROM temperature_readings
WHERE noted_date IS NOT NULL
GROUP BY hora
ORDER BY hora;

-- View 3: Máxima e mínima
CREATE VIEW IF NOT EXISTS temp_max_min_por_dia AS
SELECT DATE(noted_date) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min
FROM temperature_readings
WHERE noted_date IS NOT NULL
GROUP BY data
ORDER BY data;