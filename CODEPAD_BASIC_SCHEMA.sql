/*******                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
To replica the CODEPAD environment in SQL
*******/ 
####TABLE EMPLOYEEES
DROP TABLE IF EXISTS `leet_facebook`.`employees`;
CREATE TABLE `leet_facebook`.`employees` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `salary` INT NULL,
  `department_id` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

INSERT INTO `leet_facebook`.`employees`
(`id`,`first_name`,`last_name`,`salary`,`department_id`)
VALUES(1,'John','Smith',20000,1);

INSERT INTO `leet_facebook`.`employees`
(`id`,`first_name`,`last_name`,`salary`,`department_id`)
VALUES(2,'Ava','Muffinson',10000,5);

INSERT INTO `leet_facebook`.`employees`
(`id`,`first_name`,`last_name`,`salary`,`department_id`)
VALUES(3,'Cailin','Ninson',30000,2);

INSERT INTO `leet_facebook`.`employees`
(`id`,`first_name`,`last_name`,`salary`,`department_id`)
VALUES(4,'Mike','Peterson',20000,2);

INSERT INTO `leet_facebook`.`employees`
(`id`,`first_name`,`last_name`,`salary`,`department_id`)
VALUES(5,'Ian','Peterson',80000,2);

INSERT INTO `leet_facebook`.`employees`
(`id`,`first_name`,`last_name`,`salary`,`department_id`)
VALUES(6,'John','Mills',50000,3);



####TABLE DEPARTMENTS
DROP TABLE IF EXISTS `leet_facebook`.`departments`;
CREATE TABLE `leet_facebook`.`departments` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

INSERT INTO `leet_facebook`.`departments`
(`id`,`name`)
VALUES(1,'Reporting');

INSERT INTO `leet_facebook`.`departments`
(`id`,`name`)
VALUES(2,'Engineering');

INSERT INTO `leet_facebook`.`departments`
(`id`,`name`)
VALUES(3,'Marketing');

INSERT INTO `leet_facebook`.`departments`
(`id`,`name`)
VALUES(4,'Biz Dev');
INSERT INTO `leet_facebook`.`departments`
(`id`,`name`)
VALUES(5,'Silly Walks');

