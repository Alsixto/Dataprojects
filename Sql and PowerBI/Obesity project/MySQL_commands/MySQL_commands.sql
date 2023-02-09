#Create a new column for every table so that I can then combine them all in just one file to export to PowerBI

ALTER TABLE daily_calories_intake
ADD COLUMN unique_id  CHAR(100)  AFTER Code
;
ALTER TABLE bmi_men
ADD COLUMN unique_id  CHAR(100)  AFTER Code
;
ALTER TABLE bmi_women
ADD COLUMN unique_id  CHAR(100)  AFTER Code
;
ALTER TABLE life_expectancy
ADD COLUMN unique_id  CHAR(100)  AFTER Code
;

#Add the info to the unique_id column in the tables

UPDATE daily_calories_intake
SET unique_id = concat(Entity,Year)
;
UPDATE bmi_men
SET unique_id = concat(Entity,Year)
;
UPDATE bmi_women
SET unique_id = concat(Entity,Year)
;
UPDATE life_expectancy
SET unique_id = concat(Entity,Year)
;

#Renaming some columns for clarity and to follow SQL syntaxis

ALTER TABLE life_expectancy
RENAME COLUMN `Life expectancy at birth (historical)` TO life_expectancy
;
ALTER TABLE bmi_men
RENAME COLUMN `Mean BMI (male)` TO bmi_male
;
ALTER TABLE bmi_women
RENAME COLUMN `Mean BMI (female)` TO bmi_female
;
ALTER TABLE daily_calories_intake
RENAME COLUMN `Daily caloric supply (OWID based on UN FAO & historical sources)` TO daily_caloric_supply
;

#Join all the tables in just 1. We also sort by Country and Year to make the table more clear.

SELECT l.Entity AS country, l.Code AS country_code, l.unique_id, l.Year AS year, l.life_expectancy, ROUND(m.bmi_male,2) AS bmi_male, ROUND(w.bmi_female,2) AS bmi_female, ROUND(((bmi_male+bmi_female)/2),2) AS bmi_total , d.daily_caloric_supply
FROM life_expectancy l
JOIN bmi_men m ON m.unique_id = l.unique_id
JOIN bmi_women w ON w.unique_id = l.unique_id
LEFT JOIN daily_calories_intake d ON d.unique_id = l.unique_id
ORDER BY 1,4
;

#We can now export this information into Powerbi to work with it.
;
