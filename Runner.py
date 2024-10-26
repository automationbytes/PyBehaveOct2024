import os

from behave import __main__ as runner
import sys

if __name__ == '__main__':
    sys.stdout.flush()

    FeaturesFilesPath = "FeaturesFiles"
    ReportPath = " -f allure_behave.formatter:AllureFormatter -o Reports"
    JsonReport = " -f json.pretty -o JsonReports/json_report.json"
    BehaveOptions = " --summary --color --verbose --junit"
    Tagged = " --tags=Demo --tags=Smoke"
    run = FeaturesFilesPath+ReportPath+JsonReport+BehaveOptions+Tagged
    runner.main(run)

  #  reportdir = os.getcwd() + "/Reports"
   # os.system('cmd /c "allure serve "'+reportdir)

    '''
    --tags = Sanity #only sanity will be executed
    --tags = ~Sanity #except sanity will be executed
    
    --tags = Sanity,Demo # OR ---  Sanity or Demo will be executed
    --tags = Sanity --tags = Demo #and -- only if the scenario with both tag wil be executed    
    
    
    '''