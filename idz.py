#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "h","k"}
    b = {"c", "d", "h", "p", "r"}
    c = {"h", "i", "s"}
    d = {"c", "g", "j", "v", "w"}
    x = (a.intersection(c)).union(b)
    print(f"x = {x}")
    # Найдем дополнения множеств
    an = u.difference(a)
    bn = u.difference(b)
    y = (an.intersection(bn)).difference(c.union(d))
    print(f"y = {y}")