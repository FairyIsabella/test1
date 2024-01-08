import pytest

from common.yaml_util import clear_extract_file

# 作用域session,每次执行前清空exstract文件变量
@pytest.fixture(scope='session',autouse=True)
def clear_exstract():
    clear_extract_file()