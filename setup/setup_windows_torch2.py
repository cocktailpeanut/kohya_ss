import setup_common
from .setup_windows import install_kohya_ss_torch2
if __name__ == '__main__':
    setup_common.ensure_base_requirements()
    setup_common.setup_logging()
    install_kohya_ss_torch2()
