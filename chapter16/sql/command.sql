CREATE SCHEMA `python_free_course` ;

CREATE TABLE `python_free_course`.`movie` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `description` VARCHAR(255) NULL,
  `year` INT NULL,
  PRIMARY KEY (`id`));

INSERT INTO `python_free_course`.`movie` (`title`, `description`, `year`) 
VALUES ('John Wick', 'Action Movie', 2020);

INSERT INTO actor (name,gender)
VALUES ('Keanu Reeves','M')

UPDATE `python_free_course`.`actor` SET `gender` = 'F' 
WHERE (`id` = '6');

SELECT * FROM python_free_course.actor_in_movie
WHERE movie_id=1;

SELECT * FROM actor_in_movie,movie,actor
WHERE actor_in_movie.movie_id = movie.id
AND actor_in_movie.actor_id = actor.id;

WHERE actor_in_movie.movie_id = movie.id
AND actor_in_movie.actor_id = actor.id
ORDER By movie.id;

SELECT movie.id,count(actor_in_movie.actor_id) 
FROM actor_in_movie,movie,actor
WHERE actor_in_movie.movie_id = movie.id
AND actor_in_movie.actor_id = actor.id
GROUP by movie.id
ORDER By movie.id;

SELECT movie.id,count(actor_in_movie.actor_id) 
FROM actor_in_movie,movie,actor
WHERE actor_in_movie.movie_id = movie.id
AND actor_in_movie.actor_id = actor.id
GROUP by movie.id
HAVING count(actor_in_movie.actor_id) > 2
ORDER By movie.id;