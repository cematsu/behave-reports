Feature: Test report generation

Background:
  Given I generate a test report

Scenario: generate a test report
  Given I generate another test report
  When I wait 0 sec
  Then I fail the test