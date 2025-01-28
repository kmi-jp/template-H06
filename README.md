# H06: Data 3
Balíček `data` z minulého semináře rozšiřte o následující funkcionalitu. Ve zdrojovém kódu urdžujte pořádek a metody seskupujte dle významu.

## Refaktorování kódu na *comprehension* 

Přepište `for` cyklus pomocí **comprehension**, kdekoli to je ve stávájícím kódu možné a vhodné.

## Třída `Index`
* `Index.__iter__(self)` - metoda pro podporu iterování, musí vracet generátor hodnot z `Index.labels`

```python
from data.index import Index


users = Index(["user 1", "user 2", "user 3", "user 4"], name="names")

assert [label for label in users] == ["user 1", "user 2", "user 3", "user 4"]
```

## Třída `IndexedContainer`
* `IndexedContainer.items(self)` - metoda pro podporu iterování přes dvojice `(key, value)`, musí vracet iterator (`zip`). Funguje totožně jako `.items()` u slovníku 
* `IndexedContainer.__getitem__(self, key)` - podpora operátoru `[]`, funkcionalita jako u slovníku, pokud `key` neexistuje, vyvolá `KeyError`. Upravte metodu `IndexedContainer.get(self, key)`, aby používala nově implementovaný operátor `[]`

## Třída `Series`
* `Series.__iter__(self)` - metoda pro podporu iterování, musí vracet generátor hodnot z `Series.values`
*  `Series.iterate_over(self)` - metoda, která vrátí nekonečný generátor hodnot z `Series.values`; pokud dojde nakonec seznamu, tak pokračuje při další iteraci zase od začátku

## Třída `DataFrame`
* `DataFrame.__iter__(self)` - metoda pro podporu iterování, musí vracet generátor klíčů z `DataFrame.index`

## Příklady použití

Zde uvedené příklady jsou demonstrovány na třídách `Series` a `DataFrame` (metody definované pro `IndexedContainer` by i pro ní fungovali obdobně)

```python
from data.series import Series
from data.index import Index

users = Index(["user 1", "user 2", "user 3", "user 4"], name="names")

salaries = Series([20000, 300000, 20000, 50000], index=users)

assert [value for value in salaries] == [20000, 300000, 20000, 50000]
assert salaries["user 2"] == 300000

gen = salaries.iterate_over()

for i  in range(10):
    assert next(gen) == salaries.values[i % 4]
```

```python
from data.series import Series
from data.index import Index
from data.dataframe import DataFrame

users = Index(["user 1", "user 2", "user 3", "user 4"], name="names")

salaries = Series([20000, 300000, 20000, 50000], index=users)
names = Series(["Lukas Novak", "Petr Pavel", "Pavel Petr", "Ludek Skocil"], index=users)
cash_flow = Series([-100, 10000, -2000, 1100], index=users)

data = DataFrame([names, salaries, cash_flow], index=Index(["names", "salary", "cash flow"]))

assert [key for key in data] == ["names", "salary", "cash flow"]

assert [pair for pair in data.items()] == list(zip(["names", "salary", "cash flow"], [names, salaries, cash_flow]))
```
