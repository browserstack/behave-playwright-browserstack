Feature: Local sample

  Scenario: Can reach a localhost page through the BrowserStack Local tunnel
    Given I visit the local sample page
    Then I should see the local sample heading
