#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

def main():
    df = pd.read_csv("data.csv",engine='python',encoding='shift-jis')#ファイル名は、クオテーションで囲んでください。もしtest.csvという名前なら、"hogehoge.csv"は、"test.csv"です
    print(df)#読み込んだデータをすべて表示
    print(df.head())#最初の5行程度を表示
    print(df.shape)#読み込んだデータの行数と列数を表示。100行2列なら(100,2)です

if __name__ == '__main__':
    main()
    
