def enum_(cls):
    from enum import Enum
    return Enum(cls.__name__, cls.__dict__)

@enum_
class AccountType:
    savings = "Savings"
    current = "Current"


print(AccountType.savings.value)
