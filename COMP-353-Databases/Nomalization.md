# Normalization 


## Simple definitions for derivining normal forms:
- 1NF : The Key (remove repeating groups)
- 2NF : THe Whole key (remove partial depende)
- 3NF : And nothing but the key

## Normalization steps

## Second Normal Form 2NF 
Achieved by first making sure the table is in first normal form, and then removing attributes that only partially depend on the key by creating new tables. So the steps are: 
- The Databse is in 1NF.
- For every non-trivial dependency X → A either
  - X is not a proper subset of any candidate key OR
  - A is a key attribute

## Third Normal Form 3NF
Achieved by first making sure the table is in second normal form, and
making sure that there are no non-key attributes that are transitively dependent on any candidate
key.So the steps are :
• The Relation is in 2NF
• If it’s in 2NF and it’s non-key attributes are fully and directly dependent on the key, then it is
also in 3NF
• For every non-trivial dependency X → A either
– X is a superkey or
– A is a key attribute


Boyce-Codd Normal Form BCNF: achieved by first making sure the table is in third normal
form. So the steps are :
• The Relation is in 3NF
• For every non-trivial dependency X → A, A is a superkey