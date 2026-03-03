Feature: Movie booking via web interface

  Scenario: Visitor views list of movies
    Given the database has a movie titled "BDD Movie"
    When I go to the movies page
    Then I should see "BDD Movie" on the page

  Scenario: Visitor books an available seat
    Given the database has a movie titled "BDD Movie"
    And that movie has at least one unbooked seat
    When I book the first available seat for "BDD Movie"
    Then the seat should be marked as booked
