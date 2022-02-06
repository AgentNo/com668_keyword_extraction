# CHANGELOG

# v.1.3 [6th February 2022]
- Fixed a variable typo
- Fixed an issue in main logic which incorrectly referenced the wrong dictionary, causing a crash on write
- Added output bindings and associated logic for Cosmos DB

# v.1.2 [5th February 2022]
- Completely restructured the main logic to retrieve keywords and linked entites
- Improved error handling to fix a crash relating to lack of entities
- Reduced the amount of logging - keywords and entites are now shown in one log rather than a unique log per item
- Fixed a comment typo 

# v.1.1.1 [4th February 2022]
- Added an addition log at the end of execution
- Fixed a missing bracket which was causing a runtime error
- Removed root requirements.txt file

# v.1.1 [4th February 2022]
- Slightly changed formatting on README.md
- Added logic to get keywords and entity links to request body. Next version will focus on changing models and writing output to Cosmos

# v.1.0 [2nd February 2022]
- Added initial test implementation
