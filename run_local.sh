#script for running tests locally
rm -rf tests/allure_raw

cd tests

echo "Starting tests"

python -m pytest
#pytest --reruns 1 -n 5 --dist loadfile --alluredir=allure_raw test_element.py
pytest --reruns 1 -n 5 --dist loadfile --alluredir=allure_raw

allure serve allure_raw
