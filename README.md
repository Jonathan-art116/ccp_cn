## How To Run
```shell
uvicorn main:app --reload
```
## Swagger Url
Uvicorn running on http://127.0.0.1:8000
```shell 
http://127.0.0.1:8000/docs#/
```


### Q1: 个人所得税计算器
说明：请找出所在城市有关五险一金和个人所得税规定，按此要求，开发程序
参数：税前工资
结果：税后工资、五险一金、个人所得税

### Q2：银行贷款计算器
参数：贷款金额、贷款年限、贷款利息、还款方式（等额本金、等额本息）
结果：总利息、每月还款本金和利息
### Q3：逻辑计算器
说明：从1到9的任意整数中取三个数，能通过加减乘除任意组合得到24。不考虑顺序，找出所有的符合要求的组合。
例如：(1 + 3) * 6、1 * 3 * 8