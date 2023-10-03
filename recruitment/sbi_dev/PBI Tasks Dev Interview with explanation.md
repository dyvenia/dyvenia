
# Query Editor

1. **: Import the two tables, "ams" and "emea", and create a new table that combines the two tables into a single table named "ww". The other two tables can be deleted**
Use the "Get Data" function to import the excel files, and use "Append Queries as New" function to generate the "ww" table. 


2. **: Change the data type of "quantity" to the correct type.**
*In this case, the quantity is in decimal form. It doesn’t make sense to have 0.2 or 0.5 of a unit sold, does it? So let’s change that to whole number.*

3. **: Convert "Segment" to UPPERCASE**
*On the **Transform** tab, select **Format**, then select **UPPERCASE***

4. **: Change "Month_Name" to "Month"**
*Double-click the **Month Name** column, and rename to just **Month***

5. **: We know the '"Masterby"' product was discontinued last month, so we want to filter this data from our report to avoid confusion**
*In **Query Editor** filter out "Masterby" using test filters.*

# Close & Apply


1. Hide the "ams" and "ww" tables
 ![[Pasted image 20230926172143.png]]
 
1. **In "ww" table, create a measure, "Total_Units_Sold" that calculates the sum of "quantity"**
*DAX: Total_Units_Sold = SUM(ww[Quantity])*

3. **Create a new date table, named "Calendar" containing all datest between Janary 1 2013 and December 31 2014**
![[Pasted image 20230926172657.png]]

4. **Make a relationship between the new "Calendar" table and the "ww" table**
 ![[Pasted image 20230926172825.png]]

# Visuals

1. **Add a date slicer on the extreme left, using the date in the "Calendar" table.**
2. **Remove the Quarter and Day**
3. **Change the font size to 10**
4. **Filter the "blank" year in the slicer.**
 ![[Pasted image 20230926174039.png]]

5. **Create a line chart to see which month and year had the highest profit**
*From the Fields pane, drag the **Profit** field to a blank area on the report canvas. By default, Power BI displays a column chart with one column, Profit and drag the **Date** field from your Calendar table*
![[Pasted image 20230926180538.png]]

6. **Create a map to see which country/region had the highest profits.**
![[Pasted image 20230926180652.png]]

7. **Create a bar chart to determine which products and segments to invest in (highest sales all time)**
![[Pasted image 20230926180915.png]]

*Answer should be Rimforsa - Small Business and Government*

_____________________________

Developer should be able to produce a PBIX as good as PBI_ww or better.
Attention to details can be spotted if:
	- He selects a theme for the View menu; that makes all colors and styles match across visuals.
	- He changes the visual title and they're not prefixed as default with "sum of.."
	- He fixes the issue with the date being formatted as text in the ww table, and switches the date in the Calendar to Date instead of Date/Time.
	- Report looks appealing


# DAX

