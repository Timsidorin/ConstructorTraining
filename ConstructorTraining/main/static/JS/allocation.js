<script>
document.addEventListener('DOMContentLoaded', function () {
    // Check if the user is authenticated to add interactivity only when needed
    {% if user.is_authenticated %}
        var rightButton = document.querySelector('.right_buttom');
        if (rightButton) {
            rightButton.addEventListener('click', function () {
                var newObj = document.querySelector('.new_object');
                if (newObj.style.display === 'none' || newObj.style.display === '') {
                    newObj.style.display = 'block';
                } else {
                    newObj.style.display = 'none';
                }
            });
        }
    {% endif %}
});
</script>
