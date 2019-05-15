# matplot-service
matplotlib service


## 柱状图
columnInRequest
```js
{
    'coordinate' : {'x': ['1950', '1960', '1970', '1980', '1990', '2000', '2010年'], 'y': '金额'}
    'data' : [
        {'value': [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3], 'label': '平均值'},
        {'value': [30.2, 53.3, 75.9, 5862.5, 979.6, 1289.7, 1958.3], 'label': '最大值'}
        ]
}
```
columnInResponse
```python
bytes
```
