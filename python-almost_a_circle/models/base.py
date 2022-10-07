#!/usr/bin/python3
""" Class base"""
import json
import csv
import os.path


class Base:
        """ main class called Base"""
        __nb_objects = 0

        def __init__(self, id=None):
                """ initializer method"""
                if id is not None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = self.__nb_objects

        @staticmethod
        def to_json_string(list_dictionaries):
            """ List to JSON string """
            if list_dictionaries is None or list_dictionaries == "[]":
                return "[]"
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """ Save object in a file """
            filename = "{}.json".format(cls.__name__)
            list_dic = []

            if not list_objs:
                pass
            else:
                for i in range(len(list_objs)):
                    list_dic.append(list_objs[i].to_dictionary())

            lists = cls.to_json_string(list_dic)

            with open(filename, 'w') as f:
                f.write(lists)
