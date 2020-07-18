# Standard number validation


[![CircleCI](https://circleci.com/gh/lgrabowski/std-number-validation.svg?style=shield)](https://circleci.com/gh/lgrabowski/std-number-validation)

Among different day to day life activities we approach all kind of numbers
from social security numbers to credit card numbers. 
Following simple library helps in validation numbers against different algorithms and strategies.


Standard number/code validation library. 

# Example of usages

```@python
from std_number_validation import validate 
validate.validation(79927398713).is_valid()
```
validator works as a context to:


```@python
from std_number_validation import validate 
with validate.contextual_validation(79927398713) as validator:
    # do stuff
    pass
```


```more example in std_number_validation/tests/integration_tests.py```

# Requirements:
python 3.8+ 
editor which respects editor config (vim powaaa!)



# Classic TODO list:
- tox ? - version up from 3.7 (maybe)
- Damn algorithm - fun to implement




        
