#№ Задание

Представим себе дом, у которого основания стен образуют треугольник и имеют одинаковую длину. Чертеж такого дома можно представить равносторонним треугольником с координатами вершин **(x1, y1), (x2, y2), (x3, y3)**.

Требуется написать программу, которая расставит на чертеже разрезы всех трех стен. Для простоты можно считать, что разрез - это отрезок, который перпендикулярен отрезку стены и разделяется им на две равные части. Длина разреза фиксирована и равна **L**.
Расставленные разрезы не должны пересекаться друг с другом и с другими стенами (разрез должен пересекаться только со своей стеной, см. картинку).

- Задача 1
Написать программу на любом языке программирования, которая скажет, возможно ли так расставить разрезы.

- Задача 2
Дополнить программу, чтобы она выводила координаты концов разрезов, если их так можно расставить.

- Задача 3 (optional)
Попробовать решить данную задачу не для равностороннего треугольника, а для произвольного треугольника.

![example](https://github.com/vjkuznetsov/csc_ams1_test/blob/master/img/example.png)

## Решение

1. Переформулируем задачу в терминах аналитической геометрии: Требуется найти геометрическое место трех точек, таких чтобы каждая из них была удалена от одной из сторон треугольника на величину **L/2** и при этом перпендикуляры, опущенные из этих точек на соответствующие стороны треугольника не пересекались.

Заметим сходство задачи с определением местоположения центра вписанной в треугольник окружности (точка, равноудаленная от всех сторон треугольника), и, очевидно, что, если **L/2** больше или равно радиусу вписанной в треугольник окружности, то задача не имеет решения. 

Радиус окружности, вписанной в треугольник, рассчитаем по формуле, известной из школьного курса геометрии.

2. По условию, требуется найти только одну тройку отрезков/сечений, построим отрезки, проходящие через точки - проекции центра окружности, вписанной в треугольник, на стороны треугольника.

- запишем уравнения сторон треугольника в виде ```Ax + By + C = 0```

- найдем уравнения биссектрис углов треугольника (потребуется проверка на биссектрису внутреннего/внешнего угла);

- решив систему уравнений из двух уравнений биссектрис, найдем координаты центра окружности;

- построим прямые, перпендикулярные сторонам треугольника, проходящие через центр окружности;

- найдем точку пересечения вышеуказанных прямых и сторон треугольника;

- найдем концы искомых отрезков воспользовавшись пропорцией длин отрезков.

3. Для проверки корректности решения визуализируем ответ.






