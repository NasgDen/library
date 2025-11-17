function updateTime() {
    // Создаем новый объект Date, чтобы получить текущее время
    const now = new Date();

    // Получаем часы, минуты и секунды
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    const month = now.getMonth();
    const day = now.getDate();
    const year = now.getFullYear();

    // Форматируем время, добавляя ведущие нули при необходимости
    const formattedTime =
      (hours < 10 ? '0' : '') + hours + ':' +
      (minutes < 10 ? '0' : '') + minutes + ':' +
      (seconds < 10 ? '0' : '') + seconds + " " +
      (day < 10 ? '0' : '') + day + "." + 
      (month < 10 ? '0' : '') + month + "." + year;


    // Находим HTML-элемент по его id и обновляем его содержимое
    document.getElementById('current-time').textContent = formattedTime;
  }

  // Вызываем функцию сразу при загрузке страницы
  updateTime();

  // Обновляем время каждую секунду (каждую 1000 миллисекунд)
  setInterval(updateTime, 1000);