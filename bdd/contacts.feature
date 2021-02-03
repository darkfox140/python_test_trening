Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <last_name>, <first_name> and <address1>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | last_name  | first_name  | address1 |
  | Last name1 | First name1 | Address1 |
  | Last name1 | First name2 | Address2 |


Scenario Outline: Delete a contact
  Given a non empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact