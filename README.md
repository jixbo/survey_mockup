There are 5 questions defined in the database with 2 dependencies.
Api returns next question of the survey fulfilling the dependency. It will return question 4 after recieving answer from question 2 because dependency answer for question 3 is not fulfilled, but it is for question 4.

curl http://localhost:5000/api/question/ -d '{"id":2,"answer":"no"}' -X POST -H "Content-Type: application/json"

curl http://localhost:5000/api/question/ -d '{"id":3,"answer":"yes"}' -X POST -H "Content-Type: application/json"

curl http://localhost:5000/api/question/ -d '{"id":4,"answer":"yes"}' -X POST -H "Content-Type: application/json"

