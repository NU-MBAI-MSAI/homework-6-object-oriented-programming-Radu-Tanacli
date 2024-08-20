## Homework Instructions
MSAI 305 Intensive Program Design<br> 
Test Instructions
---
- This homework uses the unittest testing framework instead of the pytest testing framework. 
- However, it behaves very similarly. At any point, you can run individual tests by clicking 
  on the green play button next to the tests. 
- You can also run all the tests by right-clicking on the runner.py and choosing Run. This will run all 
  the tests for all the problems and provide useful information.
  
Homework Instructions
---

1. In the `city_data` package, create a file named `city.py`.
2. In that file, create a class named `City` with the following:
    - An `init` method that takes the following parameters: `name`, `infected`, `recovered`, and `deaths`. The 
      last three should have default values of `0`. The `init` method should set attributes of the same 
      name, but "private" (i.e. mangled). 
         - Uncomment the first import statement at the top of the `test_city.py` file. 
         - Uncomment and run the first test and the setup method in the class. Remove the pass keyword from each.
    - A property for the `name` attribute. Uncomment and run the `test_name` test. Remove the pass keyword.
    - A property and attribute for the `infected` attribute. For the setter, you should raise a `TypeError` if the 
      parameter is `None` or not an instance of an int. Give a useful error message. Uncomment and run the 
      `test_infected_init`, `test_infected_setter`, and `test_infected_setter_fail` tests. Remove the pass keyword.
    - A property and attribute for the `recovered` attribute. For the setter, you should raise a `TypeError` if the 
      parameter is `None` or not an instance of an int. Give a useful error message. Uncomment and run the 
      `test_recovered_init`, `test_recovered_setter`, and `test_recovered_fail` tests. Remove the pass keyword.
    - A property and attribute for the `deaths` attribute. For the setter, you should raise a `TypeError` if the 
      parameter is `None` or not an instance of an int. Give a useful error message. Uncomment and run the 
      `test_deaths_init`, `test_deaths_setter`, and `test_deaths_fail` tests. Remove the pass keyword.
    - Override the `__eq__` method to return True if `self` and the parameter have the same values for the name 
      attribute. Return False if the parameter is `None` or not an instance of a `City`. Uncomment and run the 
      `test_equals`, `test_equals_none` and `test_equals_diff_objs` tests. Remove the pass keyword.
    - Override the `__str__` method to return the values of the attributes in the following string format 
      (you may find f strings helpful for this!):
      ```
      Name: XXXX
      Infected: XXX, Recovered: XXX, Deaths: XXX
      ```
3. Create a class named `Pandemic` with the following:
    - An `init` method that does not take any parameters and initializes an attribute named `cities` to an empty list.
         - Uncomment the two import statements at the top of the `test_pandemic.py` file. 
         - Uncomment and run the first test and the setup method for the class. Remove the pass keyword.
    - A method named `add_city` that takes a string as a parameter and adds a city object to the `cities` attribute (don't forget to import 
      the `City` class!). If the city is already in the list, raise a `ValueError` with the message `"City already added"`. 
         - Uncomment and run the `test_add_city_new` and `test_add_city_fail` tests. Remove the pass keyword.
    - A method named `edit_city` that takes a string and 3 integers as parameters. If the city exists in the list, the method
    should update the city with the integers. If the city is not in the list it should raise a `ValueError` with the
    message `"City not in list"`.
         - Uncomment and run the `test_edit_city_existing` and `test_edit_city_not_existing` tests. Remove the pass
           keyword.
    - A method named `display_city` that takes a string as a parameter. If the city exists in the list, the method should print out
    the city to the console (just use the print function), otherwise it should print out `"City not in list"`.
         - Uncomment and run the `test_display_city_existing` and `test_display_city_none` tests.
    - A method named `display_all_city_stats` that consumes a string that represents the name of one of the attributes
    from the `City` class. The method should sort cities based on the attribute. To do this, you may find the [attrgetter function](https://docs.python.org/3/library/operator.html#operator.attrgetter) from the operator module (imported above) helpful. 
    The method should then print out all the values in the sorted cities list. You may also find [this resource](https://docs.python.org/3/howto/sorting.html) on using a lambda to sort a list helpful.
        - Uncomment and run the `test_display_all_city_stats_by_name` and `test_display_all_city_stats_by_infected` 
          tests.
 