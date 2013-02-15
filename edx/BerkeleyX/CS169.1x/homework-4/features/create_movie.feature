Feature: search for movies by director

  As a moviefiler
  I want to include a movie
  So that I can display to my friends or so on

  Scenario: add a movie
    Given I am on the RottenPotatoes home page
    When  I follow "Add new movie"
    Then  I am on the new movie page
    And   I fill in "movie[title]" with "Elite Squad"
    And   I press "Save Changes"
    Then  I should be on the RottenPotatoes home page
    And   I should see "Elite Squad was successfully created"