from msilib.schema import Environment
from venv import create
import fire
from solarnet.run import RunTask


if __name__ == '__main__':
    fire.Fire(RunTask)

conda venv create -f Environment.ubuntu.cpu.yml
conda activate <environment_name>
