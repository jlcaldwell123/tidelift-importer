# tidelift-importer
# Summary
This is a python script that takes in a dependency file and requests the dependencies to be added to a Tidelift Catalog. Please reach out to your Tidelift contact to receive the appopriate dependency file.

# Format
python importer.py [dependency-file.csv]

# Requirements
1. A ".tidelift" file in the directory where the python script is run. The tidelift file should contain the following information:  
TIDELIFT_ORGANIZATION=[Your Orginization Name]  
TIDELIFT_PROJECT=[Your Project Name]  
TIDELIFT_API_KEY=[Project's API Key]
2. A relative pathway of a dependency file passed into the python script as an argument. The CSV file must have the following format (with the delimiter being a tab character):  
Platform  Package Version ...
3. A project created that is linked to the Catalog that you wish to populate with the dependencies in the file. These project crednetials will go in the ".tidelift" file.

# Outcome
1. The console will output each package as it is requested to the Catalog
2. The task will be created in the catalog to approve the package (should be automatically approved if manual review is turned off)
