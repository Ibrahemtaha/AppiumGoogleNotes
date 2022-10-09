import pytest
from base.DriverClass import Driver
import time


@pytest.fixture(scope="class")
def beforeClass(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    print("Before Class")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After Calss")

@pytest.fixture()
def beforeMethod():
    print("Beofre Method")
    yield
    print("After Method")