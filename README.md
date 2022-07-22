# Test-Framework-for-web
Example of test framework for web


To run tests in a docker container:
docker build . -t pythest_runner
docker run --rm --mount type=bind,src=D:\Test-Framework-for-web,target=/web_tests/ pythest_runner


To run allure server:
allure serve test_result


Also, you can run tests using docker-compose.yml

To run tests use:
docker-compose up --build 

To stop and remove all containers after tests running
docker-compose down
