#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import prevind
import sqlite3
import unittest
import pathlib


def created_bd(name_bd):
    file_path = pathlib.Path.cwd() / name_bd

    if file_path.exists and file_path.is_file:
        return True
    return False


def added_product(name_bd, name, market, count):
    conn = sqlite3.connect(name_bd)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT products.product_name, markets.market_title, products.product_count
            FROM products
            INNER JOIN markets ON markets.market_id = products.market_id
            WHERE 
            products.product_name = ? and 
            markets.market_title = ? and 
            products.product_count = ?
        """,
        (name, market, count),
    )
    rows = cursor.fetchall()
    conn.close()

    return bool(rows)


class indTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("Проверка работы операций с базами данных")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("Конец")

    def test_create_bd(self):
        self.assertEqual(prevind.create_db("test_bd"), created_bd("test_bd"))

    def test_add_product(self):
        self.assertEqual(
            prevind.add_product("test_bd", "Sugar", "Magnit", 5),
            added_product("test_bd", "Sugar", "Magnit", 5),
        )

    def test_select_all_last(self):
        self.assertEqual(len(prevind.select_all("test_bd")[-1]), 3)

    def test_select_all_first(self):
        self.assertEqual(len(prevind.select_all("test_bd")[0]), 3)
