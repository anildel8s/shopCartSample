Feature: Add product to cart from wishlist
  Scenario: Adding the lowest price product from wishlist
    Given I add four different products to my wish list
    When I view my wishlist table
    Then I find total four selected item in the wishlist
    When I search for the lowest price product
    And I am able to add the lowest price item to my cart
    Then I am able to verify the item in my cart