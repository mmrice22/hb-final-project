// CREATE A FAVORITE BY CLICKING HEART BUTTON

const disableFaveButton = () => {
    if ($(".favorite-button").hasClass("clicked")){
        $(".favorite-button").attr('disabled', true)
    };
};


$('.favorite-button').on('click', (evt) => {
    evt.preventDefault();
    $('.favorite-button').addClass("clicked")
    console.log("button clicked!")
    const clickedBtn = evt.target;
    disableFaveButton(clickedBtn)
});
