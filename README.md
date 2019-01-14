Docpy
===========================
Docpy is a library that is meant to be used in order to process files, arrays or handle data.

### Currently it has this functions:
* file_to_dicc(route, splitBy=',', nameKey=[], hasTop=False, idxKey=[], groupBy={})
* arrayPrinter(array,TopText = [],SideText = [], divider = '',offset = 2)
* dataVerifier(data,restrains = {},needsToHave = {})

file_to_dicc(route, splitBy=',', nameKey=[], hasHeader=False, idxKey=[], groupBy={})
-------------

| parameter | function |
| ------ | ------ |
| route | Is the route for the file or the name of the file if it is in the same folder(Currently supports .txt and .csv) |
| splitBy | Is the character that every line in the document will be splited by (default is ',') |
| namekey | It shall contain the name of what data you need to be saved in the dict according to the header, the first element of this list will be the main key (Needs to make hasHeader True) |
| idxKey | If there is no header it will save the data of the file in order according to the index, the first element of this list will be the main key |
| groupBy | groupBy = {'name of category' : {'key':"name",'data':[]}} |

| groupBy Component | function |
| ------ | ------ |
| name of category | Here is the key that will be asigned to this group |
| key | Here you select 'name' or 'idx' depending on 'data' |
| data | Here you can put the name according to the header or put the indexes of the data that you want to group in the file|


### Example

#### candy.txt

```
competitorname,chocolate,fruity,caramel,peanutyalmondy,nougat,crispedricewafer,hard,bar,pluribus,sugarpercent,pricepercent,winpercent
100 Grand,1,0,1,0,0,1,0,1,0,.73199999,.86000001,66.971725
3 Musketeers,1,0,0,0,1,0,0,1,0,.60399997,.51099998,67.602936
One dime,0,0,0,0,0,0,0,0,0,.011,.116,32.261086
One quarter,0,0,0,0,0,0,0,0,0,.011,.51099998,46.116505
Air Heads,0,1,0,0,0,0,0,0,0,.90600002,.51099998,52.341465
Almond Joy,1,0,0,1,0,0,0,1,0,.465,.76700002,50.347546
Baby Ruth,1,0,1,1,1,0,0,1,0,.60399997,.76700002,56.914547
Boston Baked Beans,0,0,0,1,0,0,0,0,1,.31299999,.51099998,23.417824
Candy Corn,0,0,0,0,0,0,0,0,1,.90600002,.32499999,38.010963
Caramel Apple Pops,0,1,1,0,0,0,0,0,0,.60399997,.32499999,34.517681
Charleston Chew,1,0,0,0,1,0,0,1,0,.60399997,.51099998,38.975037
Chewey Lemonhead Fruit Mix,0,1,0,0,0,0,0,0,1,.73199999,.51099998,36.017628
Chiclets,0,1,0,0,0,0,0,0,1,.046,.32499999,24.524988
Dots,0,1,0,0,0,0,0,0,1,.73199999,.51099998,42.272076
Dum Dums,0,1,0,0,0,0,1,0,0,.73199999,.034000002,39.460556
```
#### Example 1

```
>>>dicc = file_to_dicc('candy.txt', splitBy=',', nameKey=['competitorname','sugarpercent','pricepercent','winpercent'], hasHeader=True, groupBy={'category' : { 'key' : 'name', 'data':['chocolate','fruity','caramel','peanutyalmondy','nougat','crispedricewafer','hard','bar'] }})
>>>print(dicc)
{'100 Grand': {'sugarpercent': '.73199999', 'pricepercent': '.86000001', 'winpercent': '66.971725', 'category': ['1', '0', '1', '0', '0', '1', '0', '1']}, '3 Musketeers': {'sugarpercent': '.60399997', 'pricepercent': '.51099998', 'winpercent': '67.602936', 'category': ['1', '0', '0', '0', '1', '0', '0', '1']}, 'One dime': {'sugarpercent': '.011', 'pricepercent': '.116', 'winpercent': '32.261086', 'category': ['0', '0', '0', '0', '0', '0', '0', '0']}, 'One quarter': {'sugarpercent': '.011', 'pricepercent': '.51099998', 'winpercent': '46.116505', 'category': ['0', '0', '0', '0', '0', '0', '0', '0']}, 'Air Heads': {'sugarpercent': '.90600002', 'pricepercent': '.51099998', 'winpercent': '52.341465', 'category': ['0', '1', '0', '0', '0', '0', '0', '0']}, 'Almond Joy': {'sugarpercent': '.465', 'pricepercent': '.76700002', 'winpercent': '50.347546', 'category': ['1', '0', '0', '1', '0', '0', '0', '1']}, 'Baby Ruth': {'sugarpercent': '.60399997', 'pricepercent': '.76700002', 'winpercent': '56.914547', 'category': ['1', '0', '1', '1', '1', '0', '0', '1']}, 'Boston Baked Beans': {'sugarpercent': '.31299999', 'pricepercent': '.51099998', 'winpercent': '23.417824', 'category': ['0', '0', '0', '1', '0', '0', '0', '0']}, 'Candy Corn': {'sugarpercent': '.90600002', 'pricepercent': '.32499999', 'winpercent': '38.010963', 'category': ['0', '0',
'0', '0', '0', '0', '0', '0']}, 'Caramel Apple Pops': {'sugarpercent': '.60399997', 'pricepercent': '.32499999', 'winpercent': '34.517681', 'category': ['0', '1', '1', '0', '0', '0', '0', '0']}, 'Charleston Chew': {'sugarpercent': '.60399997', 'pricepercent': '.51099998', 'winpercent': '38.975037', 'category': ['1', '0', '0', '0', '1', '0', '0', '1']}, 'Chewey Lemonhead Fruit Mix': {'sugarpercent': '.73199999', 'pricepercent': '.51099998', 'winpercent': '36.017628', 'category': ['0', '1', '0', '0', '0', '0', '0', '0']}, 'Chiclets': {'sugarpercent': '.046', 'pricepercent': '.32499999', 'winpercent': '24.524988', 'category': ['0', '1', '0', '0', '0', '0', '0', '0']}, 'Dots': {'sugarpercent': '.73199999', 'pricepercent': '.51099998', 'winpercent': '42.272076', 'category': ['0', '1', '0', '0', '0', '0', '0', '0']}, 'Dum Dums': {'sugarpercent': '.73199999', 'pricepercent': '.034000002', 'winpercent': '39.460556', 'category': ['0', '1', '0', '0', '0', '0', '1', '0']}}
```
