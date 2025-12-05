from py.xml import html
from datetime import datetime

import pytest


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1", help="my option: test or demo")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope="session", autouse=True)
def default_function():
    print("\n default_function,每个模块只运行一次,根据conftest的目录来看")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Time', class_='sortable', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
