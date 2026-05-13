Feature: Verify BrowserStack Local

  Scenario: Navigate to a page served on localhost through the BrowserStack Local tunnel
    Given I visit local app website
    Then the page title should contain "BrowserStack Local"
