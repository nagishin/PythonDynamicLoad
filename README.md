# PythonDynamicLoad
importlibを使用したpythonの動的モジュールの読み込みサンプル<br>
入力で与えられる<b>計算タイプ(add/sub/mul/div)</b>によって読み込むモジュールを切り替える<br>
（各計算タイプのモジュールを同一インターフェースで定義しておくことでプラグイン化）<br>

## 実行結果
```
Input calculate type. (add/sub/mul/div)
add
Input arg1.
10
Input arg2.
2.5
Result: 10.0 + 2.5 = 12.5
```

## main.py
```
import importlib

# 指定されたプラグインモジュール実行
def execute_plugin(plugin_name, arg1, arg2):

    # インポートするモジュールパス
    import_path = 'plugin.' + plugin_name

    # モジュールをインポート
    module = importlib.import_module(import_path)

    # インポートとしたモジュールを実行
    return module.Calculator.calc(arg1, arg2)

if __name__ == '__main__':

    print('Input calculate type. (add/sub/mul/div)')
    calc_name = input()

    print('Input arg1.')
    arg1 = float(input())

    print('Input arg2.')
    arg2 = float(input())

    # プラグインの実行
    formula, result = execute_plugin(calc_name, arg1, arg2)
    print(f'Result: {formula} = {result}')
```

## add.py
```
class Calculator:
    @classmethod
    def calc(cls, arg1, arg2):
        return f'{arg1} + {arg2}', arg1 + arg2
```

## sub.py
```
class Calculator:
    @classmethod
    def calc(cls, arg1, arg2):
        return f'{arg1} - {arg2}', arg1 - arg2
```

## mul.py
```
class Calculator:
    @classmethod
    def calc(cls, arg1, arg2):
        return f'{arg1} * {arg2}', arg1 * arg2
```

## div.py
```
class Calculator:
    @classmethod
    def calc(cls, arg1, arg2):
        return f'{arg1} / {arg2}', arg1 / arg2 if arg2 != 0 else 0
```
