# Test-Framework-for-web
Example of test framework for web

For run tests in a docker container:
docker build . -t pythest_runner
docker run --rm --mount type=bind,src=D:\Test-Framework-for-web,target=/web_tests/ pythest_runner

For run allure server
allure serve test_result
