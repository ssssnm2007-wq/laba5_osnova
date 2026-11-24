<!DOCTYPE html>
<!-- Объявляем тип документа HTML5 -->
<html lang="ru">
<!-- Корневой элемент, язык русский -->
<head>
    <!-- Кодировка символов -->
    <meta charset="UTF-8">
    <!-- Адаптивность для мобильных -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Заголовок вкладки -->
    <title>Лаб. №5 — Позиционирование</title>
    <!-- Подключение внешнего файла стилей -->
    <link rel="stylesheet" href="positioning.css">
</head>
<body>
<!-- Тело документа -->

    <!-- Статичные блоки (position: static — по умолчанию) -->
    <div class="box-static">Static</div>
    <!-- Первый статичный блок: идёт в обычном потоке -->
    <div class="box-static">Static</div>
    <!-- Второй статичный блок: идёт под первым -->

    <!-- Относительно позиционированные блоки -->
    <div class="box-relative-1">Relative 1</div>
    <!-- position: relative — смещается относительно своего обычного места -->
    <div class="box-relative-2">Relative 2</div>
    <!-- Второй relative-блок, перекрывает первый -->

    <!-- Контейнер с абсолютно позиционированными блоками -->
    <div class="container">
        <!-- position: relative — точка отсчёта для absolute-потомков -->
        <div class="box-absolute-1">Absolute 1</div>
        <!-- absolute — позиционируется относительно .container -->
        <div class="box-absolute-2">Absolute 2</div>
        <!-- absolute — второй слой -->
        <div class="box-absolute-3">Absolute 3</div>
        <!-- absolute — третий слой -->
    </div>

    <!-- Блоки с наложением через z-index -->
    <div class="box-z-index-1">Z-Index 5</div>
    <!-- z-index: 5 — перекрывает блок с z-index: 4 -->
    <div class="box-z-index-2">Z-Index 4</div>
    <!-- z-index: 4 — находится под блоком с z-index: 5 -->

    <!-- Фиксированные блоки -->
    <div class="box-fixed-1">Fixed Top-Right</div>
    <!-- position: fixed — прижат к правому верхнему углу окна -->
    <div class="box-fixed-2">Fixed Bottom-Left</div>
    <!-- position: fixed — прижат к левому нижнему углу окна -->

</body>
</html>