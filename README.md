## Benford's law Validation App

### Overview and Requirements
In 1938, Frank Benford published a paper showing the distribution of the leading digit in many disparate sources of data. In all these sets of data, the number 1 was the leading digit about 30% of the time. Benford's law has been found to apply to population numbers, death rates, lengths of rivers, mathematical distributions given by some power law, and physical constants like atomic weights and specific heats.Create a python-based web application (use of tornado or flask is fine) that:

1) can ingest the attached example file (census_2009b) and any other flat file with a viable target column. Note that other columns in user-submitted files may or may not be the same as the census data file and users are known for submitting files that don't always conform to rigid expectations. How you deal with files that don't conform to the expectations of the application is up to you, but should be reasonable and defensible.

#### The included file is validated successfully with values displayed on a graph with overlay of expected values. Server-side validation checks for .csv extension or tabbed files without extension and errors out with a custom error page template if another file type is uploaded. In future I will expand this to handle more valid file extensions including excel, and provide a better frontend experience for the user to guide them.

2) validates Benford's assertion based on the '7_2009' column in the supplied file

#### Screen shot

3) Outputs back to the user a graph of the observed distribution of numbers with an overlay of the expected distribution of numbers. The output should also inform the user of whether the observed data matches the expected data distribution.

#### See above screen shot

### Notes and next steps
This was a quick proof-of-concept application and can be expanded to include more validation and further unit testing (a very basic unit test is included). The frontend experience will be enriched, the user will be able to calibrate how close to the expected values they will consider a match, and users will be able to persist and retrieve datasets. Utils could be refactored as an object class, something like BenfordValues, with methods that perform the calculations and store the results as fields on the instantiated object. Object can then be passed up and down between dao and view layers of the app. 