import json
import behave2cucumber
from behave.__main__ import main as behave_main

code = behave_main()
cucumber_json = behave2cucumber.convert(json.load(open("reports/cucumber/behave.json")))
with open('reports/cucumber/cucumber.json', 'w') as report:
    report.write(json.dumps(cucumber_json))
    report.flush()
exit(code)
