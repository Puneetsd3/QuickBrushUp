-- All posts
SELECT * FROM posts;

-- Posts by username
SELECT p.*
  FROM posts p
  JOIN users u ON u.id = p.user_id
 WHERE u.username = 'alice';

-- Count likes per post
SELECT post_id, COUNT(*) AS total_likes
  FROM likes
 GROUP BY post_id;
