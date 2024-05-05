DROP DATABASE IF EXISTS CIDM_6350;
CREATE DATABASE CIDM_6350;
USE CIDM_6350;

CREATE TABLE employee(
employee_ID INT PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR(20),
username VARCHAR(50),
email VARCHAR(50),
employee_type VARCHAR(2),
supervisor_ID INT,
FOREIGN KEY (supervisor_ID) REFERENCES employee(employee_ID)
);

CREATE TABLE service_request(
request_ID INT PRIMARY KEY,
request_date DATETIME,
description TEXT,
status VARCHAR(20) CHECK (status IN ('fulfilled', 'in process', 'failed'))
);

CREATE TABLE technician(
technician_ID INT PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR(20)
);

CREATE TABLE technician_skill(
technician_ID INT,
skillset VARCHAR(40),
PRIMARY KEY (technician_ID, skillset),
FOREIGN KEY (technician_id) REFERENCES technician(technician_ID)
);

CREATE TABLE assignment(
assignment_ID INT PRIMARY KEY,
assignment_date DATETIME,
priority VARCHAR(20) CHECK (priority IN ('high','medium','low')),
employee_ID INT,
technician_ID INT,
request_ID INT,
FOREIGN KEY (employee_ID) REFERENCES employee(employee_ID),
FOREIGN KEY (technician_ID) REFERENCES technician(technician_ID),
FOREIGN KEY (request_ID) REFERENCES service_request(request_ID)
);

CREATE TABLE infotech(
I_employee_ID INT PRIMARY KEY,
FOREIGN KEY (I_employee_ID) REFERENCES employee(employee_ID)
);

CREATE TABLE certificate(
I_employee_ID INT,
Certificate VARCHAR(100),
PRIMARY KEY (I_employee_ID, certificate),
FOREIGN KEY (I_employee_ID) REFERENCES infotech(I_employee_ID)
);

CREATE TABLE human_resources(
H_employee_ID INT PRIMARY KEY,
number_contract INT,
FOREIGN KEY (H_employee_ID) REFERENCES employee(employee_ID)
);

CREATE TABLE customer_service(
C_employee_ID INT PRIMARY KEY,
FOREIGN KEY (C_employee_ID) REFERENCES employee(employee_ID)
);

CREATE TABLE languages(
C_employee_ID INT,
language_spoken VARCHAR(100),
PRIMARY KEY (C_employee_ID, language_spoken),
FOREIGN KEY (C_employee_ID) REFERENCES customer_service(C_employee_ID)
);

CREATE TABLE device(
device_ID INT PRIMARY KEY,
device_name VARCHAR(20),
warranty_date DATE
);

CREATE TABLE vendor(
vendor_ID INT PRIMARY KEY,
vendor_name VARCHAR(20),
contact VARCHAR(20)
);

CREATE TABLE login(
login_ID INT PRIMARY KEY,
date DATE,
location VARCHAR(20),
employee_ID INT,
device_ID INT,
FOREIGN KEY (employee_ID) REFERENCES employee(employee_ID),
FOREIGN KEY (device_ID) REFERENCES device(device_ID)
);

CREATE TABLE software(
software_ID INT PRIMARY KEY,
version_s VARCHAR(20),
license_key BIGINT,
warranty_date DATE,
vendor_id INT,
FOREIGN KEY (vendor_ID) REFERENCES vendor(vendor_ID)
);

CREATE TABLE device_software(
device_ID INT,
software_ID INT,
PRIMARY KEY (device_ID, software_ID),
FOREIGN KEY (device_ID) REFERENCES device(device_ID),
FOREIGN KEY (software_ID) REFERENCES software(software_ID)
);

CREATE TABLE order_placed(
order_ID INT PRIMARY KEY,
order_date DATE,
software_ID INT,
employee_ID INT,
FOREIGN KEY (software_ID) REFERENCES software(software_ID),
FOREIGN KEY (employee_ID) REFERENCES employee(employee_ID)
);


INSERT INTO employee (employee_ID, first_name, last_name, username, email, employee_type, supervisor_ID)
VALUES
    (001, 'Ansu', 'Fati', 'Ansu_Fati', 'ansu.fati@example.com', 'IT', NULL),
    (002, 'Alice', 'smith','alice_smith', 'alice.smith@example.com', 'IT', 001),
    (003, 'Bob', 'Jones','bob_jones', 'bob.jones@example.com', 'HR', 001),
    (004, 'Emma', 'Wilson','emma_wilson', 'emma.wilson@example.com', 'HR', 002),
    (005, 'Max', 'Miller', 'max_miller', 'max.miller@example.com', 'CS', 002);
    
INSERT INTO service_request (request_ID, request_date, description, status)
VALUES
    (0023, '2023-11-19 10:00:00', 'Software Installation', 'fulfilled'),
    (0045, '2023-11-19 11:30:00', 'Hardware Repair', 'in process'),
    (0044, '2023-11-19 13:45:00', 'Network Configuration', 'failed'),
    (0056, '2023-11-19 15:20:00', 'Database Optimization', 'fulfilled'),
    (0093, '2023-11-19 17:00:00', 'Security Audit', 'in process');
    
INSERT INTO technician (technician_ID, first_name, last_name)
VALUES
    (0091, 'Kyle', 'Smith'),
    (0029, 'Mbappe', 'Johnson'),
    (0093, 'Benzema', 'Williams'),
    (0084, 'Messi', 'Jones'),
    (0055, 'Ronaldo', 'Brown');

INSERT INTO technician_skill (technician_ID, skillset)
VALUES
    (0091, 'Programming'),
    (0029, 'Network Administration'),
    (0093, 'Database Management'),
    (0084, 'Hardware Troubleshooting'),
    (0055, 'Security Analysis');
    
INSERT INTO assignment (assignment_ID, assignment_date, priority, employee_ID, technician_ID, request_ID)
VALUES
    (100, '2023-11-19 10:30:00', 'high', 001, 0029, 0023),
    (287, '2023-11-19 12:00:00', 'medium', 002, 0055, 0045),
    (367, '2023-11-19 14:15:00', 'low', 001, 0084, 0056),
    (455, '2023-11-19 16:30:00', 'high', 005, 0093, 0044),
    (558, '2023-11-19 18:00:00', 'medium', 005, 0091, 0093);
    
INSERT INTO infotech (I_employee_ID)
VALUES
    (001);
    
INSERT INTO certificate (I_employee_ID, Certificate)
VALUES
    (001, 'CISSP'),
    (001, 'Oracle Database Administrator Certified Associate (OCA)');

INSERT INTO human_resources (H_employee_ID, number_contract)
VALUES
    (002, 24),
    (003, 10);

INSERT INTO customer_service (C_employee_ID)
VALUES
    (4),
    (5);
    
INSERT INTO languages (C_employee_ID, language_spoken)
VALUES
    (4, 'German'),
    (4, 'English'),
    (5, 'English'),
    (5, 'Mandarin');
    
INSERT INTO device (device_ID, device_name, warranty_date)
VALUES
    (024, 'Laptop1', '2023-12-31'),
    (003, 'Desktop2', '2024-01-15'),
    (018, 'Tablet3', '2023-11-25'),
    (015, 'Phone4', '2023-12-10'),
    (008, 'Printer5', '2024-02-01');
    
INSERT INTO vendor (vendor_ID, vendor_name, contact)
VALUES
    (001, 'Marshal Tech', '509-958-777'),
    (045, 'Caprisun', '234-334-5342'),
    (003, 'Ballon doree', '134-545-355'),
    (015, 'Abidjan', '355-657-234'),
    (016, 'Startend', '324-657-865');

INSERT INTO login (login_ID, date, location, employee_ID, device_ID)
VALUES
    (0023, '2023-05-19', 'Office1', 001, 003),
    (0984, '2023-11-30', 'Home2', 002, 024),
    (0894, '2023-11-14', 'Office3', 003, 008),
    (0418, '2023-07-19', 'Home4', 004, 018),
    (0415, '2023-07-19', 'Office5', 005, 015);

INSERT INTO software (software_ID, version_s, license_key, warranty_date, vendor_id)
VALUES
    (012, 'Bien', 123456, '2024-01-01', 001),
    (015, 'Starline', 789012, '2023-12-31', 045),
    (022, 'Trackone', 345678, '2024-02-15', 003),
    (027, 'Tumblero', 901234, '2023-11-30', 015),
    (001, 'TheSoftware', 567890, '2024-03-10', 016);
    
INSERT INTO device_software (device_ID, software_ID)
VALUES
    (008, 015),
    (018, 027),
    (003, 001),
    (015, 022),
    (024, 012);
    
INSERT INTO order_placed (order_ID, order_date, software_ID, employee_ID)
VALUES
    (009, '2023-04-01', 012, 001),
    (026, '2023-08-06', 022, 001),
    (027, '2023-08-06', 001, 002),
    (034, '2023-11-19', 027, 002),
    (041, '2023-11-06', 015, 001);
    
/* Section 6*/

 -- Assignment Table
DESC assignment;
SELECT * FROM assignment;

-- Employee Table
DESC employee;
SELECT * FROM employee;

-- Infotech Table
DESC infotech;
SELECT * FROM infotech;

-- Certificate Table
DESC certificate;
SELECT * FROM certificate;

-- Human Resources Table
DESC human_resources;
SELECT * FROM human_resources;

-- Customer Service Table
DESC customer_service;
SELECT * FROM customer_service;

-- Languages Table
DESC languages;
SELECT * FROM languages;

-- Device Table
DESC device;
SELECT * FROM device;

-- Vendor Table
DESC vendor;
SELECT * FROM vendor;

-- service request Table
DESC service_request;
SELECT * FROM service_request;

-- Login Table
DESC login;
SELECT * FROM login;

-- Software Table
DESC software;
SELECT * FROM software;

-- Device Software Table
DESC device_software;
SELECT * FROM device_software;

-- Technician Table
DESC technician;
SELECT * FROM technician;

-- technician skill Table
DESC technician_skill;
SELECT * FROM technician_skill;

-- Order Placed Table
DESC order_placed;
SELECT * FROM order_placed;


/* Section 7*/
-- Retrieve the Names and Status of Service Requests with Their Assignments:
SELECT sr.request_ID, sr.description, sr.status, a.assignment_date, a.priority
FROM service_request sr
LEFT JOIN assignment a ON sr.request_ID = a.request_ID;

-- Find the Number of Technicians with Their Skills:
SELECT t.technician_ID, t.first_name, t.last_name, COUNT(ts.skillset) AS num_skills
FROM technician t
LEFT JOIN technician_skill ts ON t.technician_ID = ts.technician_ID
GROUP BY t.technician_ID, t.first_name, t.last_name;

-- Calculate the Average Number of Certificates per Infotech Employee:
SELECT i.I_employee_ID, COUNT(c.Certificate) AS num_certificates
FROM infotech i
LEFT JOIN certificate c ON i.I_employee_ID = c.I_employee_ID
GROUP BY i.I_employee_ID;

-- Retrieve Employee Assignments with Assigned Technicians and Service Request Details:
SELECT e.employee_ID, e.username, a.assignment_ID, a.assignment_date, a.priority,
       t.technician_ID, t.first_name AS technician_first_name, t.last_name AS technician_last_name,
       sr.request_ID, sr.request_date, sr.description, sr.status
FROM employee e
LEFT JOIN assignment a ON e.employee_ID = a.employee_ID
LEFT JOIN technician t ON a.technician_ID = t.technician_ID
LEFT JOIN service_request sr ON a.request_ID = sr.request_ID;

-- Find the Total Number of Devices and the Average Warranty Period:
SELECT COUNT(device_ID) AS total_devices, AVG(DATEDIFF(warranty_date, CURDATE())) AS avg_warranty_days
FROM device;

-- List Employees, employee types and the Total number of software they ordered:
SELECT e.employee_ID, e.username, e.employee_type, op.software_ID, COUNT(op.order_ID) AS total_orders
FROM employee e
LEFT JOIN order_placed op ON e.employee_ID = op.employee_ID
GROUP BY e.employee_ID, e.username, e.employee_type, op.software_ID;