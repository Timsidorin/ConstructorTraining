// Находим нужные элементы
var createTrainingBtn = document.querySelector('.create-training');
var modal = document.getElementById("myModal");
var closeModalBtn = document.getElementsByClassName("close")[0];
var body = document.getElementById("body");

// При клике на кнопку "Создать тренинг" открываем модальное окно
createTrainingBtn.addEventListener('click', function() {
    modal.style.display = "block";
    body.style.background = "rgba(0,0,0,1)";

});

// При клике на кнопку закрытия, закрываем модальное окно
closeModalBtn.addEventListener('click', function() {
    modal.style.display = "none";
    body.style.background = "rgba(0,0,0,0)";
});

// Если пользователь кликает вне модального окна, закрываем его
window.addEventListener('click', function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        body.style.background = "rgba(0,0,0,0)";
    }
});