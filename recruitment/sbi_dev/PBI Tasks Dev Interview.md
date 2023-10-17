# Senior Power BI Developer Dashboarding Tasks

Hi there, first of all congratulations for making it until here! The second part of this technical interview is to **develop from scratch a Power BI Dashboard for a Swedish furniture company from scratch using a dataset that we will provide to you**. This dataset contains **sales data** by **segment**, **country** and **product** among other variables. In order to get started, follow the steps listed below:

 1. **Make sure you have Power BI Desktop downloaded**
 2. **Proceed to download the dataset by accessing this [link](https://drive.google.com/drive/folders/1O1nEF63GoECnuFCRGD0KtZZOuFu_Z4IA)**
 3. **Open a new .pbix file and proceed to complete the tasks listed below**
  
## Query Editor

1. **: Import the two tables, "ams" and "emea", and create a new table that appends the two tables into a single table named "ww", from now on, the tables "ams" and "emea" will not be needed**

2. **: Convert "Segment" to UPPERCASE**

3. **: Change "Month_Name" to "Month"**

4. **: We know the '"Masterby"' product was discontinued last month, so we want to filter out this data from our report to avoid confusion**

## Data Modelling

1. **Leave only the 'ww' table visible**

2. **In "ww" table, create a measure, "Total_Units_Sold" that calculates the sum of "quantity"**

3. **Create a new date table, named "Calendar" containing all datest between Janary 1 2013 and December 31 2014**

4. **Make a relationship between the new "Calendar" table and the "ww" table**

## Visuals

When completing the tasks from this section keep in mind that the End User expects some visual coherence among visualization as well as meaningful titles for each visualization.

1. **Add a date slicer on the extreme left, using the date in the "Calendar" table.**
2. **If Quarter and Day are present in the slicer, please remove them**
3. **Change the font size to 10**
4. **Filter the "blank" year in the slicer.**

5. **Create a line chart to see which month and year had the highest profit**

6. **Create a map to display where the profits were made**

7. **Create a bar chart to determine which products and segments to invest in (highest sales of all time)**

