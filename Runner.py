import os

from behave import __main__ as runner
import sys

if __name__ == '__main__':
    sys.stdout.flush()

    FeaturesFilesPath = "FeaturesFiles"
    ReportPath = " -f allure_behave.formatter:AllureFormatter -o Reports"
    BehaveOptions = " --summary --color --verbose --junit"
    run = FeaturesFilesPath+ReportPath+BehaveOptions
    runner.main(run)

    reportdir = os.getcwd() + "/Reports"
    os.system('cmd /c "allure serve "'+reportdir)