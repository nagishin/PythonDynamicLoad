# -*- coding: utf-8 -*-
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
