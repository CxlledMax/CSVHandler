# CSVHandler
This code allows you to work intelligently with CSV files. A file in CSV syntax is converted into several lists, which are combined in a top list and so you can easily **add new rows**, **delete rows** and **edit existing rows**.

## Version
You can use this program from **Python version 2.5**.

## Methods
### CSVHandler.load()
_Returns a list._ <br>
Example:
```py
data = CSVHandler.load("file path as string")
```

### CSVHandler.parse()
_Returns nothing_ <br>
Example:
```py
a_list = [["row1"], ["row2"]]
CSVHandler.load("file path as string", a_list)
```

## Changelog
**27.11.2021**, 23:39 (UTC+01:00) -> Added some if-statements to check if the path is a CSV-File. <br>
**27.11.2021**, 23:46 (UTC+01:00) -> Optimized return statement in the `CSVHandler.load()` method.
