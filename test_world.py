import logging
from pathlib import Path

import world


def test_configure_logger_first_call_configures_logger():
    # 确保日志文件不存在
    log_file = Path('logs/world.caca.log')
    if log_file.exists():
        log_file.unlink()

    world.configure_logger()

    logger = logging.getLogger('WorldLogger')
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.FileHandler)
    assert logger.handlers[0].level == logging.INFO
    assert logger.handlers[0].formatter._fmt == '%(asctime)s - %(levelname)s - %(message)s'
    assert log_file.exists()


def test_configure_logger_second_call_does_not_reconfigure_logger():
    world.configure_logger()

    # 保存原始配置
    original_logger = logging.getLogger('WorldLogger')
    original_handler = original_logger.handlers[0]

    world.configure_logger()

    logger = logging.getLogger('WorldLogger')
    assert logger is original_logger
    assert logger.handlers[0] is original_handler
